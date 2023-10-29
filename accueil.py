import streamlit as st  # pip install streamlit
from deta import Deta

def accueilf():
    with st.form("form", clear_on_submit=True):

        st.write ("Remplir")
        name = st.text_input("Ton nom")
        age = st.number_input("Ton age")
        submitted = st.form_submit_button("Enregistrer")

# comment
    hellof = ${{ secrets.DATA_KEY }}
    deta = Deta(hellof)
    db = deta.Base("visible")
    if submitted:
        db.put({"name":name, "age":age})

    db_content = db.fetch().items
    st.dataframe(db_content)
