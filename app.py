############### Paramétrages ###############

## Imports
from openai import OpenAI
import streamlit as st

from query_data import query_rag

## Force l'affichage plein écran sur Streamlit
def wide_space_default():
    st.set_page_config(layout='wide')
wide_space_default()

############### Paramétrages ###############


############### Introduction ###############

## Logo
st.image('Media/logo.png', width=80)

############### Introduction ###############


############### Upload des documents ###############

## Texte 1
st.markdown('''
             ## 1. Uploadez vos documents :
             ''')

############### Upload des documents ###############

############### Chat avec l'agent IA ###############

## Texte 2
st.markdown('''
             ## 2. Posez votre question :
             ''')
prompt = st.chat_input("Votre question")

def list_display(list):
    st.write(f"Source numéro {list[0]}, extrait du document {list[1]}, page {list[2]}, partie {list[3]} :")
    st.write(f"{list[4]}")
    st.write("test")

if prompt:
    response = query_rag(prompt)

    st.write(f"Voici la réponse à votre question : \n{response[1]}")

    st.write("Voici la liste des sources utilisées pour produire cet extrait généré par IA :")

    st.write(response[0])

    # for list in response[0]:
    #     st.write(list_display(list))


############### Chat avec l'agent IA ###############
