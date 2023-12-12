import streamlit as st  # pip install streamlit


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
  

