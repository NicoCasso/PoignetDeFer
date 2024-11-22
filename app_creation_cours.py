from sqlalchemy import Engine
import streamlit as st
from sqlmodel import Session, select
from models import Coach, Cours
from init_db import get_engine
from utils import creation_cours
engine = get_engine


#creation d’un cours

with st.form(key="nouveau_cours"):
    nom_cours = st.text_input("Nom du cours")
    jour = st.selectbox("jour", ["lundi", "mardi", "mercredi", "jeudi", "vendredi"])
    heure = st.selectbox("Horaire", [f"{i} h" for i in range(9, 17)])
    capacite_max = st.number_input("Capacité maximum", min_value=1, step=1)
    submit_button = st.form_submit_button(label="confirmer ajout cours")

    




    with Session(engine) as session:
        coaches = session.exec(select(Coach)).all()
        choix_coach = {coach.nom_coach: id.coach for coach in coaches}
    
    nom_coach = st.selectbox("coach", list(choix_coach.keys()))    
    id_coach = choix_coach[nom_coach]

    if submit_button:
        creation_cours(nom_cours, jour, heure, capacite_max, id_coach)
        st.success("cours ajouter au calendrier")



#AFFICHAGE DES COURS CREÉS

with Session(engine) as session:
    statement = select(Cours)
    results = session.exec(statement).all()

    if results:
        st.subheader("liste de cours")
        for cours in results:
            coach = session.get(Coach, cours.coach_id).nom_coach
            st.write(f"{cours.nom_cours}: {cours.jour}, {cours.heure}, Capacité: {cours.capacite_max}, coach: {nom_coach}")