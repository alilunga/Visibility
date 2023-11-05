import streamlit as st  # pip install streamlit
from deta import Deta

def accueilf():
    with st.form("form", clear_on_submit=True):

        st.write ("Remplir")
        name = st.text_input("Ton nom")
        age = st.number_input("Ton age")
        submitted = st.form_submit_button("Enregistrer")

# comment
    deta = Deta(st.secrets["data_key"])
    db = deta.Base("visible")
    if submitted:
        db.put({"name":name, "age":age})


