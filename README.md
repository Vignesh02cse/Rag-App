# ChatPDF with FAISS

ChatPDF is an assistant application built to provide question-answering functionality based on PDF documents stored in a FAISS-backed vector database. The assistant retrieves relevant answers from documents by embedding text using Hugging Face embeddings and storing them in FAISS for fast similarity search. The application uses Streamlit for the front-end interface.

## Features

- **Question Answering**: Users can ask questions related to the contents of PDFs.
- **FAISS Vector Store**: Utilizes FAISS for efficient similarity-based document retrieval.
- **Streamlit UI**: Simple web-based interface for interacting with the assistant.
- **Pre-Ingested PDF Support**: PDF documents are pre-ingested into the FAISS database, eliminating real-time document uploads.

## Technologies Used

- **FAISS**: A library for efficient similarity search and clustering of dense vectors.
- **LangChain**: A framework for building applications powered by language models.
- **Streamlit**: A Python framework for building interactive web apps.
- **Hugging Face Embeddings**: Pre-trained embeddings to represent the document contents as vectors.
- **Ollama**: Tool used to facilitate PDF ingestion and pre-process the documents for embedding generation.

## Getting Started

Follow the instructions below to set up and run this project on your local machine.

### Prerequisites

Before getting started, make sure you have the following installed:
- Python 3.7 or later
- `pip` (Python package manager)
- Virtual environment (recommended)
- **Ollama**: Used for document ingestion into the FAISS database (installation steps below).

### Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/Vignesh02cse/Rag-App.git
    cd Rag-App
    ```

2. **Create and activate a virtual environment**:

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows, use .venv\Scripts\activate
    ```

3. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Install Ollama**:
   Ollama is required for document ingestion. Follow the installation steps for your operating system:

    - **Windows**:
        1. Download the Ollama installer from [Ollama's official website](https://ollama.com).
        2. Run the installer and follow the on-screen instructions.

    - **Linux (Ubuntu)**:
        ```bash
        curl -fsSL https://ollama.com/install | sh
        ```

    - **MacOS**:
        ```bash
        curl -fsSL https://ollama.com/install | sh
        ```

5. **Download or Build the FAISS Database**:
   - **Option 1**: If you already have a pre-built FAISS database, place the FAISS index directory in the project directory.
   - **Option 2**: To build your own FAISS database, use Ollama to ingest your PDFs and store them in FAISS.

### Building the FAISS Database

To build the FAISS vector store from your PDF documents:
**Prepare your PDF documents**:
    ```bash
        ingest.py.
        ```


### Running the Application

Once you've set up the environment and ingested the PDFs into FAISS, you can run the Streamlit app to start interacting with the assistant:

```bash
streamlit run Main.py
