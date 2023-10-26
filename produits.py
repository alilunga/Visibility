import streamlit as st  # pip install streamlit

def produitsf():
    
   with st.form("produits", clear_on_submit=True):

        st.write ("Ajouter un produit")
        produit_id = st.number_input("Entrez le numero du produit")
        produit_nom = st.text_input("Entrez le nom du produit")
        produit_des = st.text_input("Entrez la description du produit")
        produit_img = st.text_input("Telecharger l'image du produit")
        produit_pa = st.number_input("Entrez le prix d'achat du produit")
        produit_pv = st.number_input("Entrez le prix de vente du produit")
        produit_stk = st.number_input("Entrez la quantite en stock du produit")
        produit_dmd = st.number_input("Entrez la quantite en demande du produit")
        submitted = st.form_submit_button("Enregistrer")  

def importf():

      with st.form("produits", clear_on_submit=True):

        st.write ("Remplir sa Déclaration d’Importation des biens")
        produit_id = st.number_input("Poste d'entree :")
        produit_nom = st.text_input("Pays de provenance des biens")
        produit_id = st.number_input("Nom du fournisseur etranger :")
        produit_nom = st.text_input("Contact du fournisseur etranger:")
        produit_id = st.number_input("Nom du beneficiaire du paiement :")
        produit_nom = st.text_input("Contact du beneficiaire du paiement")
        produit_id = st.number_input("Monnaie de la transaction :")
        produit_nom = st.text_input("Montant FOB/CIF a repartir")
        produit_id = st.number_input("Frais connexes :")
        produit_nom = st.text_input("Modalites de paiement")
        produit_id = st.number_input("Autres informations utiles :")
        produit_nom = st.text_input("Pays de provenance des biens")
        submitted = st.form_submit_button("Enregistrer")  

