import streamlit as st  # pip install streamlit
from deta import Deta
def accueilf():
  st.write("Station")
def utilisateursf():
    
   with st.form("utilisateurs", clear_on_submit=True):

        utilisateur_id = st.number_input("Entrez le numéro du utilisateur")
        utilisateur_nom = st.text_input("Entrez le nom de l'utilisateur")
        utilisateur_pass = st.text_input("Entrez le mot de pass de l'utilisateur")
        utilisateur_img = st.text_input("Télécharger la photo de l'utilisateur")
        submitted = st.form_submit_button("Enregistrer") 
       
   deta = Deta(st.secrets["data_key"])
   db = deta.Base("utilisateur")
   if submitted:
        db.put({"Numero": utilisateur_id, 
                "Nom": utilisateur_nom, 
                "Image": utilisateur_img,
                "Passwd": utilisateur_pass})
 
def utilisateurslstf():
   deta = Deta(st.secrets["data_key"])
   db = deta.Base("utilisateur")
   db_content = db.fetch().items
   st.dataframe(db_content)

def utilisateursupdf():
   deta = Deta(st.secrets["data_key"])
   db = deta.Base("utilisateur")
   db_content = db.fetch()
   st.dataframe(db_content)
