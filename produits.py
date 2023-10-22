import streamlit as st  # pip install streamlit

def produitsf():
    # --- INPUT & SAVE VALEURS DOUANE ---

   with st.form("produits", clear_on_submit=True):

        st.write ("Ajouter un produit")
        produit_id = st.number_input("Entrez le numero du produit")
        produit_nom = st.text_input("Entrez le nom du produit")
        produit_des = st.text_input("Entrez la description du produit")
        produit_img = st.text_input("Telecharger l'image du produit")
        produit_pa = st.number_input("Entrez le prix d'achat du produit")
        produit_pv = st.number_input("Entrez le prix de vente du produit")
        produit_stk = st.number_input("Entrez la quantite en stock du produit")
        produit_dmd = st.number_input("Entrez la quantite en demande du produit")
        submitted = st.form_submit_button("Enregistrer")  

