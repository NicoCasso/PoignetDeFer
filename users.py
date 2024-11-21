import streamlit as st
from faker import Faker
from models import Membres, Cours, inscriptions, nom_membres
from sqlalchemy import query
from init_db import engine
from sqlmodel import Session
fake = Faker('fr_FR')

# Fonction pour créer des membres fictifs
def creation_membres(nombre_de_membres: int):
    membres = []
    for _ in range(nombre_de_membres):
        nom = fake.name()
        email = fake.email()
        membre = Membres(nom=nom, email=email)
        membres.append(membre)
    return membres

# Générer des membres fictifs et les enregistrer dans la base de données
def enregistrer_membres(nombre_de_membres: int):
    membres = creation_membres(nombre_de_membres)
    with Session(engine) as session:
        session.add_all(membres)
        session.commit()

# Interface utilisateur Streamlit
st.title("Inscription à un cours")

# Afficher les cours disponibles
with Session(engine) as session:
    cours = session.query(Cours).all()
    cours_disponibles = [(f"{c.nom} ({c.jour} à {c.heure})", c.id) for c in cours]
    cours_selectionne = st.selectbox("Choisissez un cours", cours_disponibles, format_func=lambda x: x[0])

    # Inscription à un cours
    nom = st.text_input("Nom")
    email = st.text_input("Email")
    if st.button("S'inscrire"):
        if nom:
            cours_id = cours_selectionne[1]
            inscriptions = session.query(inscriptions).filter(inscriptions.cours_id == cours_id).count()
            if inscriptions < 5:
                membre = session.query(Membres).filter(Membres.name == nom_membres).first()
                if not membre:
                    membre = Membres(nom=nom, email=email)
                    session.add(membre)
                    session.commit()
                inscription = inscriptions(membre_id=membre.id, cours_id=cours_id)
                session.add(inscription)
                session.commit()
                st.success(f"{nom} est inscrit au cours {cours_selectionne[0]}!")
            else:
                st.error("Le cours est complet. Veuillez choisir un autre cours.")
        else:
            st.error("Veuillez entrer votre nom.")

    # Afficher l'historique des cours pour chaque membre
    st.header("Historique des cours")
    name_historique = st.text_input("Entrez votre nom pour voir votre historique")
    if st.button("Voir l'historique"):
        membre = session.query(Membres).filter(Membres.name == name_historique).first()
        if membre:
            histo_inscriptions = session.Query(inscriptions).filter(inscriptions.membre_id == membre.id).all()
            if inscriptions:
                for inscription in histo_inscriptions:
                    cours = session.query(Cours).filter(Cours.id == inscription.cours_id).first()
                    st.write(f"Cours: {cours.nom}, Jour: {cours.jour}, Heure: {cours.heure}")
            else:
                st.write("Aucun cours inscrit.")
        else:
            st.write("Aucun membre trouvé.")