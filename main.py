import streamlit as st

from streamlit_option_menu import option_menu
from deta import Deta


from accueil import accueilf
from clients import clientsf
from fournisseurs import fournisseursf
from produits import *
from achats import achatsf
from ventes import ventesf
from analytiques import analytiquesf

def creds_entered():
    if st.session_state["user"].strip()=="admin" and st.session_state["passwd"].strip()=="admin":
        st.session_state["authenticated"]=True

    else:
        st.session_state["authenticated"]=False
        if not st.session_state["passwd"]:
            st.warning("Entrez votre mot de passe.")
        elif not st.session_state["user"]:
            st.warning("Entrez votre nom d'utilisateur.")
        else:
            st.error("Nom d'utilisateur/ Mot de passe invalide")

def authenticate_user():
    if "authenticated" not in st.session_state:
        st.text_input(label="Nom d'utilisateur:", value="", key="user", on_change=creds_entered)
        st.text_input(label="Mot de passe:", value="", key="passwd", type="password", on_change=creds_entered)
        return False
    else:
        if st.session_state["authenticated"]:
            return True
        else:
            st.text_input(label="Nom d'utilisateur:", value="", key="user", on_change=creds_entered)
            st.text_input(label="Mot de passe:", value="", key="passwd", type="password", on_change=creds_entered)
            return False

if authenticate_user():
    st.set_page_config(
        page_title="Bailch Smart Visibility",
        )
    with st.sidebar:
        st.sidebar.title("Welcome")
        selected = option_menu(
            menu_title='Smart Visibility',
            options=['accueil','clients','fournisseurs','produits','achats','ventes','analytiques'],
            icons=['house','person-square','graph-up','tools','cart','share','send'],
            menu_icon="bricks", default_index=0,
            styles={
                    "container": {"padding": "5!important", "background-color": "#ffffe0"},
                    "icon": {"color": "red", "font-size": "16px"}, 
                    "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#ddd"},
                    "nav-link-selected": {"background-color": "#add8ff"},}

            )

    if selected == 'accueil':
        accueilf()
    if selected == 'clients':
        clientsf()
    if selected == 'fournisseurs':
        fournisseursf()
    if selected == 'produits':
        select_list=["Creer un produit", "Produits en stock", "Recetionner un produit", "Commander un produit", "Importer un produit"]
        ret = st.selectbox("Action", select_list)
        if ret == "Produits en stock":
            stockf()
        else:
            produitsf()
    if selected == 'achats':
        achatsf()
    if selected == 'ventes':
        ventesf()
    if selected == 'analytiques':
        analytiquesf()


