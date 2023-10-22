import streamlit as st  # pip install streamlit

def clientsf():
    # --- INPUT & SAVE VALEURS DOUANE ---

    with st.form("clients", clear_on_submit=True):

        st.write ("Ajouter un client")
        client_id = st.number_input("Entrez le numero du client")
        client_adr = st.text_input("Entrez l'addresse du client")
        client_vil = st.text_input("Entrez la ville du client")
        client_pay = st.text_input("Entrez le pays du client")
        client_pho = st.number_input("Entrez le telephone du client")
        client_crl = st.number_input("Entrez l'email du client")
        submitted = st.form_submit_button("Enregistrer")

  

