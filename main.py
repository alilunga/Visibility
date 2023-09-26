import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="Bailch Smart Visibility"
)

with st.sidebar:
    choose = option_menu("Smart Visibility", ["Accueil","Réquisitions","Stocks","Services","Commandes","Déclarations de change","Contact"],
                         icons=['house','person-square','graph-up','tools','cart','share','send'],
                         menu_icon="bricks", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#ffffe0"},
        "icon": {"color": "red", "font-size": "16px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#ddd"},
        "nav-link-selected": {"background-color": "#add8ff"},
    }
    )

#if choose == "Accueil":
#    accueil

#if choose == "Réquisitions":
#    requisitions

#if choose == "Stocks":
#    stocks

#if choose == "Services":
#    services

#if choose == "Commandes":
#    commandes

#if choose == "Déclarations de change":
#    declarations

#if choose == "Contact":
#    contact
