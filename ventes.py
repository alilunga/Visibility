import streamlit as st  # pip install streamlit


def ventesf():
    # --- INPUT & SAVE VALEURS DOUANE ---

    with st.form("ventes", clear_on_submit=True):

        st.write ("Ajouter un vente")
        vente_id = st.number_input("Entrez le numero du vente")
        vente_pro = st.text_input("Entrez le produit vente")
        vente_qte = st.text_input("Entrez la quantite de l'vente")
        vente_pa = st.number_input("Entrez le prix d'vente")
        submitted = st.form_submit_button("Enregistrer")



  
