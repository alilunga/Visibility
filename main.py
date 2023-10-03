import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
        page_title="Bailch Smart Visibility",
)

from accueil import accueilf
from requisitions import requisitionsf
from stocks import stocksf
from services import servicesf
from commandes import commandesf
from declarations import declarationsf
from contact import contactf


with st.sidebar:
        selected = option_menu(
            menu_title='Smart Visibility',
            options=['accueil','requisitions','stocks','services','commandes','declarations','contact'],
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
if selected == 'requisitions':
    requisitionsf()
if selected == 'stocks':
    stocksf()
if selected == 'services':
    servicesf()
if selected == 'commandes':
    commandesf()
if selected == 'declarations':
    declarationsf()
if selected == 'contact':
    contactf()
