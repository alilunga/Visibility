import streamlit as st  # pip install streamlit
from deta import Deta

def fournisseursf():
   
   with st.form("fournisseurs", clear_on_submit=True):

        st.write ("Ajouter un fournisseur")
        fournisseur_id = st.number_input("Entrez le numero du fournisseur")
        fournisseur_adr = st.text_input("Entrez l'addresse du fournisseur")
        fournisseur_vil = st.text_input("Entrez la ville du fournisseur")
        fournisseur_pay = st.text_input("Entrez le pays du fournisseur")
        fournisseur_pho = st.number_input("Entrez le telephone du fournisseur")
        fournisseur_crl = st.number_input("Entrez l'email du fournisseur")
        submitted = st.form_submit_button("Enregistrer")

   deta = Deta(st.secrets["data_key"])
   db = deta.Base("fournisseur")
   if submitted:
      db.put({"Numero": fournisseur_id, 
              "Nom": produit_nom, 
              "Adresse": fournisseur_adr, 
              "Ville": fournisseur_vil,
              "Pays": fournisseur_pay,
              "Telephone": fournisseur_pho,
              "Email": fournisseur_crl})
 
def fournisseurslstf():
   deta = Deta(st.secrets["data_key"])
   db = deta.Base("produit")
   db_content = db.fetch().items
   st.dataframe(db_content)


