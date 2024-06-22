# from langchain_community.embeddings import GPT4AllEmbeddings
from langchain_openai import OpenAIEmbeddings

from openai import OpenAI
import os
import getpass

# from dotenv import load_dotenv
# load_dotenv()

# api_key_low = os.getenv("openai_api_key")
# os.environ["OPENAI_API_KEY"] = api_key_low

# os.environ["OPENAI_API_KEY"] = getpass.getpass()


# from langchain_community.embeddings import OpenAIEmbeddings
# openai = OpenAIEmbeddings(openai_api_key="my-api-key")

# def get_embedding_function():
#     embeddings = GPT4AllEmbeddings()
#     # embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
#     return embeddings
