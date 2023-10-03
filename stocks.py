import streamlit as st  # pip install streamlit


def stocksf():
    # --- INPUT & SAVE VALEURS DOUANE ---

    with st.form("Valeurs_Douane", clear_on_submit=True):

        st.write ("Remplir les valeurs douanieres")
        nbl = st.number_input("Entrer Numero bulletin de liquidation")
        nqc = st.number_input("Numero quittance")
        dtp = st.number_input("Date de paiement")
        ptf = st.number_input("Position tarifaire")
        ust = st.number_input("Unite statique")
        qte = st.number_input("Quantite")
        ndc = st.text_input("Nom du declarant")
        vld = st.number_input("Valeur en douane")
        submitted = st.form_submit_button("Enregistrer")

  

