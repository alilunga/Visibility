import streamlit as st  # pip install streamlit
from deta import Deta

def clientsf():

    with st.form("clients", clear_on_submit=True):

        client_id = st.number_input("Entrez le numero du client")
        client_adr = st.text_input("Entrez l'addresse du client")
        client_vil = st.text_input("Entrez la ville du client")
        client_pay = st.text_input("Entrez le pays du client")
        client_pho = st.number_input("Entrez le telephone du client")
        client_crl = st.text_input("Entrez l'email du client")
        submitted = st.form_submit_button("Enregistrer")

      
    deta = Deta(st.secrets["data_key"])
    db = deta.Base("client")
    if submitted:
        db.put({"Numero": client_id, 
                "Adresse": client_adr, 
                "Ville": client_vil, 
                "Pays": client_pay,
                "Telephone": client_pho,
                "Email": client_crl})
