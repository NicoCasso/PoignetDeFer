from sqlmodel import Session, select, delete
from sqlalchemy import Engine
from typing import cast
from models import * 
import streamlit as st
import pandas as pd


def get_coaches(engine : Engine) -> list[Coach]:
    with Session(engine) as session:
        statement = select(Coach)
        result = session.exec(statement)
        return list(result)
    
def create_coach(engine : Engine, coach : Coach) -> bool:
    with Session(engine) as session:
        session.add(coach)
        session.commit()
        return True
    
    return False

def update_coach(engine : Engine, coach : Coach) -> bool:
    with Session(engine) as session:
        statement = select(Coach).where(Coach.id_coach == coach.id_coach)
        results = session.exec(statement)
        linked_coach = results.one()
        linked_coach.nom_coach = coach.nom_coach
        linked_coach.specialite = coach.specialite
        session.add(linked_coach)
        session.commit()
        return True
    
    return False

    
def delete_coach(engine : Engine, coach: Coach) -> bool:
    with Session(engine) as session:
        statement = select(Coach).where(Coach.id_coach == coach.id_coach)
        results = session.exec(statement)
        linked_coach = results.one()
        session.delete(linked_coach)
        session.commit()
        return True
    
    return False

#region maxime



def afficher_cours_dispo(engine : Engine) -> list[Cours]:
    cours = []
    with Session(engine) as session:
        statement = select(Cours)
        result = session.exec(statement)
        cours=list(result)
        
    return cours

def get_inscription_by_id(engine : Engine, cours_id:int) -> list[Inscription]: 
    inscriptions_list = []
    with Session(engine) as session:  
        statement = select(Inscription).filter(Inscription.cours_id == cours_id)
        results = session.exec(statement)
        inscriptions_list = list(results)

    return inscriptions_list

def create_inscription(engine : Engine, cours_id:int, id_membre) -> bool:
    return_value = False
    with Session(engine) as session:
        statement = select(Membre).where(Membre.id_membre == id_membre)  
        results = session.exec(statement)
        membre=cast(Membre, results)
        if membre:
            date1=dt.datetime.now()
        
            inscription=Inscription(membre_id=id_membre, cours_id=cours_id,date_inscription=date1)
            session.add(inscription)
            session.commit()
            return_value=True

    return return_value

def get_membres_by_nom(engine : Engine, nom:str) -> list[Membre]:
    list_membres = []
    with Session(engine) as session:
        statement = select(Membre).where(Membre.nom_membre == nom)  
        results = session.exec(statement)
        list_membres = list(results)

    return list_membres

def get_history_by_id_membre(engine : Engine, id_membre:int) -> list[Inscription]:
    list_inscription = []
    with Session(engine) as session:
        statement = select(
            Inscription
        ).where (
            Inscription.membre_id== id_membre
        ).order_by(
            Inscription.date_inscription
        )  
        results = session.exec(statement)
        list_inscription = list(results)

    return list_inscription

def get_cours_by_inscriptions(engine : Engine, inscription_id:list[int]) -> list[Cours]:
    list_cours = []
    with Session(engine) as session:
        statement = select(
            Cours, Inscription
        ).join( 
            Inscription
        ).where(
            Inscription.cours_id == inscription_id
        )  
        results = session.exec(statement)
        list_membres = list(results)

def creation_cours(engine : Engine, nom_cours, jour, heure, capacite_max, id_coach):
    list_creation_cours = []
    with Session(engine) as session:
        cours = Cours(nom_cours=nom_cours, jour=jour, heure=heure, capacite_max=capacite_max, coach_id=id_coach)
        session.add(cours)
        session.commit()
        return True
    return False


#affichage des donnée via Panda( optionnel,permet la visualisation)

# def charger_donnees():
#     with Session(engine) as session:
#         query = select(Cours, Coach).join(Coach)
#         results = session.exec(query).all()
#         data = [{ "Nom du cours": cours.nom_cours,
#                   "Heure de début": cours.heure_debut,
#                     "Jour": cours.jour,
#                       "Capacité": cours.capacite,
#                         "Coach": cours.coach.nom
#                 } for cours, coach in results]
#         df = pd.DataFrame(data)
#         return df
    
#  # Charger les données et afficher le DataFrame
#  df = charger_donnees()
#  st.subheader('Données des Cours')
#  st.dataframe(df)