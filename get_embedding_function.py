from langchain_community.embeddings import GPT4AllEmbeddings

def get_embedding_function():
    embeddings = GPT4AllEmbeddings()
    return embeddings
