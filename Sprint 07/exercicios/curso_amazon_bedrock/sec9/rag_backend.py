import os
from langchain_community.document_loaders import PyPDFLoader  
from langchain_aws import BedrockEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.indexes import VectorstoreIndexCreator
from langchain_aws import ChatBedrock

def hr_index():
    # Data source and load
    data_load = PyPDFLoader('https://www.upl-ltd.com/images/people/downloads/Leave-Policy-India.pdf')

    # Split the text based on tokens, recursively
    # Os chunks são os tamanhos das divisões do texto
    data_split = RecursiveCharacterTextSplitter(separators=['\n\n', '\n', ' ', ' '], chunk_size=100,chunk_overlap=10)

    # Client connection for create embeddings
    data_embeddings = BedrockEmbeddings(
        credentials_profile_name = 'default',
        model_id = 'amazon.titan-embed-text-v2:0'
    )

    # Creating Vector DB to store embeddings and indexes for search
    data_index = VectorstoreIndexCreator(
        text_splitter = data_split,
        embedding = data_embeddings,
        vectorstore_cls = FAISS
    )

    # Creating index for HR Policy Document
    db_index = data_index.from_loaders([data_load])
    
    return db_index

# Foundation model to
def hr_llm():
    llm = ChatBedrock(
        credentials_profile_name = 'default',
        model_id = 'anthropic.claude-3-haiku-20240307-v1:0',
        model_kwargs = {
            "max_tokens": 3000,
            "temperature": 0.1,
            "top_p": 0.9,
        }
    )
    return llm


# According to the user prompt, searches the best match from VectorDB and sends to LLM
def hr_rag_response(index, question):
    rag_llm = hr_llm()
    hr_rag_query = index.query(question = question,
                               llm=rag_llm)
    return hr_rag_query