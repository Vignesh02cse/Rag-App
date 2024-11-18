import streamlit as st
from Rag import ChatPDF

st.set_page_config(page_title="ChatPDF with FAISS")

# Initialize session state variables
if "messages" not in st.session_state:
    st.session_state["messages"] = []
if "assistant" not in st.session_state:
    # Initialize with the path to the pre-built FAISS database
    st.session_state["assistant"] = ChatPDF(faiss_path="./faiss_index")
if "user_input" not in st.session_state:
    st.session_state["user_input"] = ""

# Function to display chat messages
def display_messages():
    st.subheader("Chat History")
    for i, (msg, is_user) in enumerate(st.session_state["messages"]):
        st.write(f"{'User:' if is_user else 'Assistant:'} {msg}")

# Process user input and get response
def process_input():
    if st.session_state["user_input"].strip():
        user_text = st.session_state["user_input"].strip()
        with st.spinner("Thinking..."):
            assistant_text = st.session_state["assistant"].ask(user_text)

        # Append to chat history
        st.session_state["messages"].append((user_text, True))
        st.session_state["messages"].append((assistant_text, False))
        st.session_state["user_input"] = ""  # Clear input box after processing

# Main page content
def page():
    st.header("Chat with Your Documents (FAISS-backed)")

    st.subheader("Ask a Question")
    st.text_input(
        "Enter your query",
        key="user_input",
        on_change=process_input,
    )

    display_messages()

# Run the app
if __name__ == "__main__":
    page()
