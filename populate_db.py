import sqlmodel as sm
from sqlalchemy import Engine
from faker import Faker
from typing import cast


import datetime as dt
from models import *
import init_db as idb

fake = Faker('fr_FR')

# Fonction pour créer des membres fictifs
def creation_membres(nombre_de_membres: int) -> list[Membre]:
    membres = []
    for _ in range(nombre_de_membres):
        nom = fake.name()
        email = fake.email()
        membre = Membre(nom_membre=nom, email=email)
        membres.append(membre)
    return membres

# Générer des membres fictifs et les enregistrer dans la base de données
def enregistrer_membres(nombre_de_membres: int, session: sm.Session):

    cartes = []
    for i in range(nombre_de_membres):
        current_carte = Carte_d_acces(key=fake.random_int(min=1000000, max=9999999))
        cartes.append(current_carte)
        session.add(current_carte)

    session.commit()

    membres = creation_membres(nombre_de_membres)

    for i in range(nombre_de_membres):
        membres[i].carte_acces_id = cast(Carte_d_acces, cartes[i]).id_carte
        session.add(membres[i])

    session.commit()

#creation des faux membres(10)
#def creation_membres()  :
    
#    for i in range(10):
#        membres = creation_membres()
#        print(f"membres{i+1}:membre:{membres[0]}, Email:{membres[1]}")
#    return (fake.name(), fake.email())  

def populate_db(engine : Engine) :
    echo_object = sm.SQLModel.metadata.create_all(engine)
    print(echo_object)

    with sm.Session(engine) as session :

        coach1 = Coach(nom_coach= "Maxime", specialite="Yoga et Pilates")
        coach2 = Coach(nom_coach= "Nicolas", specialite="Crossfit et Pump")
        coach3 = Coach(nom_coach= "Arnold", specialite="Musculation")
        coach4 = Coach(nom_coach= "Mike", specialite="Boxe et Body Combat")


        carte1 = Carte_d_acces(key=fake.random_int(min=1000000, max=9999999))
        carte2 = Carte_d_acces(key=fake.random_int(min=1000000, max=9999999))
        session.add(carte1)
        session.add(carte2)

        
        session.commit()

        membre1 = Membre(nom_membre= "edouard", email="eaeae")
        membre1.carte_acces_id=carte1.id_carte
        membre2 = Membre(nom_membre="Jean", email="eoeuu")
        membre2.carte_acces_id=carte2.id_carte

        session.add(membre1)
        session.add(membre2)

        session.commit()



        enregistrer_membres(10, session)

        session.add(coach1)
        session.add(coach2)
        session.add(coach3)
        session.add(coach4)
        
        session.commit()

        cours1 = Cours(nom_cours="Yoga et Pilates", 
            jour = "lundi",
            heure = 9,
            capacite_max=20,
            coach_id = coach1.id_coach)
        
        cours2 = Cours(nom_cours="Crossfit et Pump", 
            jour = "lundi",
            heure = 10,
            capacite_max=20,
            coach_id = coach2.id_coach)
        
        session.add(cours1)
        session.add(cours2)
        session.commit()

        date1=dt.datetime(2024, 11, 20)
        date3=dt.datetime(2024, 11, 19)
        date7=dt.datetime(2024, 11, 18)
        date9=dt.datetime(2024, 11, 2)

        inscription1=Inscription(date_inscription=date1,membre_id=membre1.id_membre,cours_id=cours1.id_cours)
        inscription2=Inscription(date_inscription=date3,membre_id=membre2.id_membre,cours_id=cours1.id_cours)
        inscription3=Inscription(date_inscription=date7,membre_id=membre1.id_membre,cours_id=cours2.id_cours)
        inscription4=Inscription(date_inscription=date9,membre_id=membre2.id_membre,cours_id=cours2.id_cours)

        session.add(inscription1)
        session.add(inscription2)
        session.add(inscription3)
        session.add(inscription4)

        session.commit()
        
        #session.refresh(coach1)
        #cours1.coach = coach1


if __name__ == "__main__":
    engine = idb.get_engine()
    populate_db(engine)
