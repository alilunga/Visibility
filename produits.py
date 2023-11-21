import streamlit as st
from deta import Deta

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
       
   deta = Deta(st.secrets["data_key"])
   db = deta.Base("visible")
   if submitted:
        db.put({"Numero": produit_id, 
                "Nom": produit_nom, 
                "Description": produit_des, 
                "Image": produit_img,
                "PA": produit_pa,
                "PV": produit_pv,
                "Qte en stock": produit_stk, 
                "Qte en demande": produit_dmd})
        db_content = db.fetch().items
        st.write(db_content)

def importf():

      with st.form("import", clear_on_submit=True):

        st.write ("Remplir sa Déclaration d’Importation des biens")
        import_entree = st.number_input("Poste d'entree :")
        import_origin = st.text_input("Pays de provenance des biens")
        import_fournisseur = st.text_input("Nom du fournisseur etranger :")
        import_contact = st.text_input("Contact du fournisseur etranger:")
        import_beneficiaire = st.text_input("Nom du beneficiaire du paiement :")
        import_bcontact = st.text_input("Contact du beneficiaire du paiement")
        import_devise = st.number_input("Monnaie de la transaction :")
        import_fob = st.number_input("Montant FOB/CIF a repartir")
        import_fconnex = st.number_input("Frais connexes :")
        import_paiement = st.text_input("Modalites de paiement")
        import_autres = st.text_input("Autres informations utiles :")
        submitted_upd = st.form_submit_button("Enregistrer")  



