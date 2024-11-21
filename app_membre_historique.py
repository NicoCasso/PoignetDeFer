
import streamlit as st
from faker import Faker
from models import Membre, Cours, Inscription
from init_db import get_engine
import utils
from sqlalchemy import Engine
from sqlmodel import Session, select
from typing import cast
engine = get_engine()


st.title("Historique des cours")

# Afficher l'historique des cours pour chaque membre


name_historique = st.text_input("Entrez votre nom pour voir votre historique")
if st.button("Voir l'historique"):
    list_membres = utils.get_membres_by_nom(engine,name_historique)
    if len(list_membres)!=0:
        id_membre = cast(Membre, list_membres[0]).id_membre
        histo_inscriptions=utils.get_history_by_id_membre(engine, id_membre)
        if len(histo_inscriptions)!=0:
            inscription_ids=[]
            for inscription in histo_inscriptions:
                id_inscription=cast(Inscription,inscription).id_inscription
                inscription_ids.append(id_inscription)
                
            cours_list=utils.get_cours_by_inscriptions(engine,inscription_ids)
            for cours in cours_list:
                st.write(f"Cours: {cours.nom_cours}, Jour: {cours.jour}, Heure: {cours.heure}")
        else:
            st.write("Aucun cours inscrit.")
    else:
        st.write("Aucun membre trouvé.")
