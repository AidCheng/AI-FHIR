import os.path
import logging
import sys
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.llms import Ollama
import numpy as np
from langchain.vectorstores import FAISS
from langchain.docstore.document import Document
import json
from typing import List

import os.path
from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage,
)

from langchain.output_parsers import PydanticOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field, validator



llm = Ollama(model="mistral:latest", temperature=0)


from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))


with open("realtimehealth/testy.json", "r") as file:
    data = json.load(file)
with open("realtimehealth/doctornotes.txt", "r") as file2:
    data2 = file2.read()

# Convert the JSON data into a string
text = json.dumps(data)
#text = data2

# Split the text into chunks
chunk_size = 3000  # Adjust the chunk size as needed
chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

# Create an instance of the Ollama embedder
embedder = OllamaEmbeddings(model="nomic-embed-text")

# Create a folder to store the embeddings
embeddings_folder = "embeddings"
os.makedirs(embeddings_folder, exist_ok=True)

# Generate embeddings for the chunks and save them locally
for i, chunk in enumerate(chunks):
    embedding = embedder.embed_query(chunk)
    filename = os.path.join(embeddings_folder, f"embedding_{i}.npy")
    np.save(filename, embedding)

# Load the saved embeddings
embeddings = []
for i in range(len(chunks)):
    filename = os.path.join(embeddings_folder, f"embedding_{i}.npy")
    embedding = np.load(filename)
    embeddings.append(embedding)

# Create a FAISS index
documents = [Document(page_content=chunk) for chunk in chunks]
index = FAISS.from_documents(documents, embedder)

# Save the index locally
index.save_local("index_folder")

# Load the saved index
index = FAISS.load_local("index_folder", embedder)

# Generate query embeddings
query = "As a respectful and honest assistant specialised in the medical field scan through the patient information and provide a readable detailed comprehensive report on the patient including full family name and given name, gender, marital status, address, and full medical history from all encounters giving precise dates detailing each medical encounter including surgical history or vaccinations if it exists, and medicine prescribed, and then give detailed recomendations for further action based on information provided and general health tips."
query_embedding = embedder.embed_query(query)

# Query the index
docs = index.similarity_search_by_vector(query_embedding, k=4)  # Adjust the number of relevant documents (k) as needed

# Concatenate the retrieved documents into a single context string
context = " ".join([doc.page_content for doc in docs])


template = """
### System:
You are an respectful and honest assistant specialised in the medical field. You have to answer the user's \
questions/ prompts using only the context provided to you and are not allowed to make anything up. If you don't know the answer, \
just say you don't know. Don't try to make up an answer. You are to make a detailed record in readable terms for the patient in essay format with nice headings in 2000 words. Please format it well for the reader to understand and leave spaces between paragraphs.

"""

# Generate a response using the LLM
response = llm.generate(prompts=[f"Context: {context} Template: {template} Query: {query} Response:"])

if response.generations:
    generated_text = response.generations[0][0].text
    print(generated_text)
else:
    print("No generated text found.")

#print(response)









