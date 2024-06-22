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

if prompt:
    st.write(f"Votre question est la suivante :")
    st.write(f"{prompt}")

    #st.write(query_rag(prompt))

############### Chat avec l'agent IA ###############
