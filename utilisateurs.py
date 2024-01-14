import streamlit as st  # pip install streamlit
from deta import Deta
def accueilf():
  st.write("Station")
def utilisateursf():
    
   with st.form("utilisateurs", clear_on_submit=True):

        utilisateur_id = st.number_input("Entrez le numéro du utilisateur")
        utilisateur_nom = st.text_input("Entrez le nom du utilisateur")
        utilisateur_des = st.text_input("Entrez la description du utilisateur")
        utilisateur_img = st.text_input("Télécharger l'image du utilisateur")
        utilisateur_pa = st.number_input("Entrez le prix d'achat du utilisateur")
        utilisateur_pv = st.number_input("Entrez le prix de vente du utilisateur")
        utilisateur_stk = st.number_input("Entrez la quantité en stock du utilisateur")
        utilisateur_dmd = st.number_input("Entrez la quantité en demande du utilisateur")
        submitted = st.form_submit_button("Enregistrer") 
       
   deta = Deta(st.secrets["data_key"])
   db = deta.Base("utilisateur")
   if submitted:
        db.put({"Numero": utilisateur_id, 
                "Nom": utilisateur_nom, 
                "Description": utilisateur_des, 
                "Image": utilisateur_img,
                "PA": utilisateur_pa,
                "PV": utilisateur_pv,
                "Qte en stock": utilisateur_stk, 
                "Qte en demande": utilisateur_dmd})
 
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
