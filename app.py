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

with st.form(key="Form :", clear_on_submit = True):
    pdf_file = st.file_uploader("Upload vos PDFs ici :", type="pdf")
    Submit = st.form_submit_button(label='Submit',disabled=True)

if pdf_file:
    Submit = st.form_submit_button(label='Submit',disabled=False)

# , accept_multiple_files=True

from pathlib import Path

if Submit:

    save_folder = '/Users/antoine/Desktop/Projets/Coding/chat_with_document/data'
    save_path = Path(save_folder, pdf_file.name)
    with open(save_path, mode='wb') as w:
        w.write(pdf_file.getvalue())
    if save_path.exists():
        st.success(f'Le PDF {pdf_file.name} a bien été ajouté dans la Base de données. Patientez quelques instants pour le temps de l\'embedding.')

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

    for list in response[0]:
        st.write(list_display(list))

############### Chat avec l'agent IA ###############
