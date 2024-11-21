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


cours=utils.afficher_cours_dispo(engine)
cours_disponibles = [(f"{c.nom_cours} ({c.jour} à {c.heure})", c.id_cours) for c in cours]
cours_selectionne = st.selectbox("Choisissez un cours", cours_disponibles)
                                     #format_func=lambda x:str(x[0]))

# Inscription à un cours
nom = st.text_input("Nom")
if st.button("S'inscrire"):
    list_membres = utils.get_membres_by_nom(engine,nom)
    if len(list_membres)!=0:
        id_membre = cast(Membre, list_membres[0]).id_membre
        cours_id = cours_selectionne[1]

        inscription_list = utils.get_inscription_by_id(engine, cours_id)
        nb_inscriptions = len(inscription_list)
        if nb_inscriptions < 5:
            if utils.create_inscription(engine, cours_id, id_membre):
                st.success(f"{nom} est inscrit au cours {cours_selectionne[0]}")
            else:
                st.error("Le cours est complet. Veuillez choisir un autre cours.")
        else:
            st.error("Veuillez entrer votre nom.")

