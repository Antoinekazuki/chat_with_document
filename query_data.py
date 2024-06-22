import argparse
from langchain.vectorstores.chroma import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from get_embedding_function import get_embedding_function

from openai import OpenAI
import os
import sqlite3

from dotenv import load_dotenv
load_dotenv()

api_key_low = os.getenv("openai_api_key")
os.environ["OPENAI_API_KEY"] = api_key_low

CHROMA_PATH = "chroma"

PROMPT_TEMPLATE = """
Answer the question based only on the following context:
{context}

---

Answer the question based on the above context: {question}
"""

def main():
    # Create CLI.
    parser = argparse.ArgumentParser()
    parser.add_argument("query_text", type=str, help="The query text.")
    args = parser.parse_args()
    query_text = args.query_text
    query_rag(query_text)

def query_rag(query_text: str):
    # Prepare the DB.
    embedding_function = get_embedding_function()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    # Search the DB.
    results = db.similarity_search_with_score(query_text, k=5)

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)

    #print(prompt)

    model = ChatOpenAI()
    response_text = model.invoke(prompt)

    response = f"Voici la réponse à votre question : \n{response_text.content}"
    print(response)
    print()

    sources = [doc.metadata.get("id", None) for doc, _score in results]

    print("Voici la liste des sources utilisées pour produire cet extrait généré par IA :")

    # Step 1: Connect to the database
    conn = sqlite3.connect('chroma/chroma.sqlite3')

    # Step 2: Create a cursor object
    cursor = conn.cursor()

    for index, source in enumerate(sources):

        query = "SELECT * FROM embedding_metadata WHERE string_value = ?"
        cursor.execute(query, (source,))
        rows = cursor.fetchall()
        cursor.execute(f"SELECT * FROM embedding_metadata WHERE id={rows[0][0]}")
        answer = cursor.fetchall()

        a = index + 1
        b = answer[1][2][:-4]
        c = answer[1][2][-3:-2]
        d = answer[0][2]

        print()
        print(f"Source numéro {index + 1}, extrait du document \033[1m{answer[1][2][:-4]}\033[0m, page \033[1m{int(answer[1][2][-3:-2]) + 1 }\033[0m, partie \033[1m{int(answer[1][2][-1]) + 1}\033[0m :")
        print()
        print(answer[0][2])

    return (index + 1), answer[0][2]


if __name__ == "__main__":
    main()
