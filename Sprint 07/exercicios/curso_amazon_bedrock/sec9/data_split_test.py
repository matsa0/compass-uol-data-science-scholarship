import os
from langchain_community.document_loaders import PyPDFLoader 
from langchain.text_splitter import RecursiveCharacterTextSplitter


# Data source and load
data_load = PyPDFLoader('https://www.upl-ltd.com/images/people/downloads/Leave-Policy-India.pdf')

# Split the text based on tokens, recursively
# Os chunks são os tamanhos das divisões do texto
data_split = RecursiveCharacterTextSplitter(separators=['\n\n', '\n', ' ', ' '], chunk_size=100,chunk_overlap=10)

sample = 'Welcome to the most comprehensive AWS Cloud Development Kit (CDK) - V2 on Udemy from an instructor with actual enterprise hands-on implementation experience migrating large number of workloads for Fortune 100 companies using AWS CDK V2.'

# Split in minor chunks
data_split_test = data_split.split_text(sample)
print(data_split_test)