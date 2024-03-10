# AI component of the program
The program runs by using local AI. 

Ollama is application allowing you to run LLM models 
To download see here:
https://python.langchain.com/docs/integrations/llms/ollama

Ollama currently supports llm models like msitral which is the one used for the program.
And we also use nomic-embed-text for the embedding which will also need to be installed via Ollama.
See here for all the models you can download:
https://ollama.com/library


For more explanations about the concepts behind the program please refer to this:
https://docs.llamaindex.ai/en/stable/getting_started/concepts.html

The vector embeddings are indexed using FAISS see more information here :
https://python.langchain.com/docs/integrations/vectorstores/faiss


## An explanation of what the program does:
- The program takes a file and turns into a string randomly splitting it into chunks. The chunks are then turned into vector embeddings and stored locally on the computer and indexed. The query is then also embedded and search for similarities with the chunks. Essentially I'm trying to implement a RAG. The context is all joined together. The LLM finally generates a response based on the query/prompt. The program generally works well for longer contexts although can be prone to miss stuff out due to the way the chunks are split. To yield better results properly parsing JSON files containing FHIR data will be best and splitting them up appropriately. Note that this program needs a powerful computer to run and all dependencies and things must be installed correctly for it to work.

