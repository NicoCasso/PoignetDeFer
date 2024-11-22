import streamlit as st
from faker import Faker
from models import Membre, Cours, Inscription
from init_db import get_engine
import utils
from sqlalchemy import Engine
from sqlmodel import Session, select
from typing import cast


# Interface utilisateur Streamlit
engine = get_engine()
st.title("Inscription à un cours")

# Afficher les cours disponibles



cours_liste=utils.afficher_cours_dispo(engine)


cours_disponibles = {}
cours_disponibles[""] = -1
for c in cours_liste :  
    membre_key="{0} ({1} à {2})".format(c.nom_cours,c.jour,c.heure)
    cours_disponibles[membre_key]=c.id_cours

cours_selectionne = st.selectbox("Choisissez un cours", cours_disponibles)
                                     #format_func=lambda x:str(x[0]))

cours_id=cours_disponibles[cours_selectionne]

if cours_id != -1:
    membre_liste=utils.get_membre_list(engine)
    membre_disponibles = {}
    membre_disponibles[""] = -1
    for membre in membre_liste:
       membre_disponibles[membre.nom_membre]=membre.id_membre


    # Inscription à un cours
    nom = st.selectbox("Nom", options=membre_disponibles.keys())
    if st.button("S'inscrire"):
        if nom != "":
            id_membre = membre_disponibles[nom]

            inscription_list = utils.get_inscription_by_id(engine, cours_id)

            found=False
            for inscription in inscription_list:
                if inscription.membre_id==id_membre and inscription.cours_id==cours_id:
                    found=True
                    break

            if found==True:
                st.error("deja inscrit")

            else:    
                nb_inscriptions = len(inscription_list)
                capacite_max = utils.get_cours_by_id(engine, cours_id).capacite_max
                if nb_inscriptions < capacite_max:
                    if utils.create_inscription(engine, cours_id, id_membre):
                        cours_choisis=list(filter(lambda c: c.id_cours==cours_id,cours_liste))
                        if len(cours_choisis) != 0:
                            cours_choisi=cast(Cours,cours_choisis[0]).nom_cours
                            st.success(f"{nom} est inscrit au cours {cours_choisi}")
                        else:
                            st.error("impossible de retrouver le cours")   
                    else:
                        st.error("ajout impossible")
                else:
                    st.error("Le cours est complet. Veuillez choisir un autre cours.")
        else:
            st.error("Veuillez entrer votre nom.")

