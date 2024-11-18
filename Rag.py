from langchain_community.vectorstores import FAISS
from langchain_community.chat_models import ChatOllama
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.schema.output_parser import StrOutputParser
from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda

embedding = HuggingFaceEmbeddings()

class ChatPDF:
    def __init__(self, faiss_path: str):
        self.faiss_path = faiss_path
        self.model = ChatOllama(model="mistral")
        self.prompt = PromptTemplate.from_template(
            """
            <s> [INST] You are an assistant for question-answering tasks. Use the following pieces of retrieved context 
            to answer the question. If you don't know the answer, just say that you don't know. Use three sentences
             maximum and keep the answer concise. [/INST] </s> 
            [INST] Question: {question} 
            Context: {context} 
            Answer: [/INST]
            """
        )
        self.vector_store = None
        self.retriever = None
        self.chain = None
        self._load_vector_store()

    def _load_vector_store(self):
        """Load the FAISS vector store if it exists."""
        if self.faiss_path:
            self.vector_store = FAISS.load_local(
                self.faiss_path, embedding, allow_dangerous_deserialization=True
            )
            self.retriever = self.vector_store.as_retriever(
                search_type="similarity_score_threshold",
                search_kwargs={"k": 3, "score_threshold": 0.2},
            )
        else:
            raise FileNotFoundError("FAISS vector store path is not specified or does not exist.")

        def combine_context_and_question(inputs):
            return {"context": inputs["context"], "question": inputs["question"]}

        # Chain setup
        combine_runnable = RunnableLambda(func=combine_context_and_question)
        self.chain = (
            combine_runnable
            | self.prompt
            | self.model
            | StrOutputParser()
        )

    def ask(self, query: str):
        if not self.chain:
            return "Vector store not loaded. Please ensure the FAISS database is available."

        # Retrieve relevant documents
        context_docs = self.retriever.get_relevant_documents(query)

        if not context_docs:
            return "No relevant documents found."

        # Extract text from the retrieved documents
        context_texts = "\n".join([doc.page_content for doc in context_docs])

        # Prepare the input for the chain
        inputs = {"context": context_texts, "question": query}

        try:
            response = self.chain.invoke(inputs)
            return response
        except Exception as e:
            return f"An error occurred: {e}"
