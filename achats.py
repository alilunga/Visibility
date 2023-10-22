import streamlit as st  # pip install streamlit

def achatsf():
    # --- INPUT & SAVE VALEURS DOUANE ---

    with st.form("achats", clear_on_submit=True):

        st.write ("Ajouter un achat")
        achat_id = st.number_input("Entrez le numero du achat")
        achat_pro = st.text_input("Entrez le produit achat")
        achat_qte = st.text_input("Entrez la quantite de l'achat")
        achat_pa = st.number_input("Entrez le prix d'achat")
        submitted = st.form_submit_button("Enregistrer")

  
