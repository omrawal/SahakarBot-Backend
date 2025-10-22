from langchain_community.chat_models import ChatPerplexity
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
import os

def initialize_qa_system():
    load_dotenv()
    api_key = os.getenv('PERPLEXITY_API_KEY')

    # Use absolute path
    current_dir = os.path.dirname(os.path.abspath(__file__))
    pdf_path = os.path.join(current_dir, "assets", "MCS_Bare_Act_and_Rules.pdf")
    
    # Load and split PDF
    loader = PyPDFLoader(pdf_path)
    pages = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    documents = text_splitter.split_documents(pages)

    # Build embeddings and vector store
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectordb = Chroma.from_documents(documents, embedding=embeddings)

    # System prompt template
    TEMPLATE = """
    You are a legal assistant for society law queries. Always answer solely using the PDF context below.
    - Answers must be 80-100 words, direct, and never fabricated.
    - Answers can be shorter than 80 words if needed.
    - Keep the answers as short as possible.
    - If the answer is not in the PDF refer the IPC/Indian laws or context.
    - If the answer is not in the PDF or in IPC/Indian laws or context, reply only: "I don't know."
    - Never make up legal content.
    - Always cite the section or page number from the PDF if relevant and any IPC/Indian Laws if relevant.
    - When formulating the answers never address the pdf as pdf but address it as THE MAHARASHTRACO-OPERATIVE SOCIETIES ACT, 1960 as the contents of pdf are society laws.

    PDF Context:
    {context}

    Question: {question}
    Answer:
    """

    prompt = PromptTemplate(
        template=TEMPLATE, 
        input_variables=["context", "question"]
    )

    # Setup the Perplexity model
    llm = ChatPerplexity(
        model="sonar",
        temperature=0.2,
        pplx_api_key=api_key
    )

    # Setup RetrievalQA
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectordb.as_retriever(),
        chain_type="stuff",
        chain_type_kwargs={"prompt": prompt}
    )

    return qa_chain