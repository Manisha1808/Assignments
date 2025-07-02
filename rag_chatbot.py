import os
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain.chains import RetrievalQA
from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline

# Set Hugging Face download timeout for slow networks
os.environ["HF_HUB_DOWNLOAD_TIMEOUT"] = "60"

# 1️⃣ Load your local document for RAG
documents = TextLoader('docs.txt').load()
text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = text_splitter.split_documents(documents)

# 2️⃣ Create embeddings using HuggingFaceEmbeddings (no API key needed)
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# 3️⃣ Build FAISS local vector store
vectorstore = FAISS.from_documents(docs, embeddings)

# 4️⃣ Initialize a lightweight open LLM for generation
generator = pipeline("text-generation", model="gpt2", max_new_tokens=50)
llm = HuggingFacePipeline(pipeline=generator)

# 5️⃣ Create the RAG QA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever()
)

# 6️⃣ CLI interface for testing (safe for assignment)
if __name__ == "__main__":
    while True:
        query = input("\nAsk a question (or type 'exit' to quit): ")
        if query.lower() == 'exit':
            break
        result = qa_chain.invoke(query)
        print("\nAnswer:", result['result'])
