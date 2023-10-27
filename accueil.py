import streamlit as st  # pip install streamlit


def accueilf():
    with st.form("form", clear_on_submit=True):

        st.write ("Remplir")
        name = st.text_input("Ton nom")
        age = st.number_input("Ton age")
        submitted = st.form_submit_button("Enregistrer")


#    deta=Deta(st.secrets["data_key"])
#    if submitted:
#        db.put({"name":name, "age":age})

#    db_content=db.fetch().items
#    st.write(db_content)
