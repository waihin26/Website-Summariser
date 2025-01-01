import dotenv
dotenv.load_dotenv()
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.document_loaders import WebBaseLoader
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
import streamlit as st

st.title("Summariser")

def get_text():
    input_text = st.text_input("Type in the url link below", key="input")
    return input_text

user_input = get_text()

if(user_input):
    loader = WebBaseLoader(user_input)
    data = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 0)
    all_splits = text_splitter.split_documents(data)

    vectorstore = Chroma.from_documents(documents=all_splits, embedding=OpenAIEmbeddings())

    question = "Summarise the main points of this article"
    docs = vectorstore.similarity_search(question)
    len(docs)

    template = """Use the following pieces of context to answer the question at the end. 
    If you don't know the answer, just say that you don't know, don't try to make up an answer. 
    Use three sentences maximum. Try to keep it concise and accurate.
    {context}
    Question: {question}
    Helpful Answer:"""
    QA_CHAIN_PROMPT = PromptTemplate.from_template(template)

    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
    qa_chain = RetrievalQA.from_chain_type(
        llm,
        retriever=vectorstore.as_retriever(),
        chain_type_kwargs={"prompt": QA_CHAIN_PROMPT}
    )

if(user_input):
    result = qa_chain({"query": question})
    result["result"]
