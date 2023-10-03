import streamlit as st  # pip install streamlit

def accueilf():
    # --- CONNEXION ---

    with st.form("Connection", clear_on_submit=True):

        st.write ("Entrer vos coordonnees")
        user = st.text_input("Nom d'utilisateur")
        password = st.text_input("Mot de passe")
        submitted = st.form_submit_button("Se connecter")

  

