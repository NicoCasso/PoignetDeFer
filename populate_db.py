import sqlmodel as sm
from sqlalchemy import Engine

import datetime as dt
from models import *
import init_db as idb

def populate_db(engine : Engine) :
    echo_object = sm.SQLModel.metadata.create_all(engine)
    print(echo_object)

    with sm.Session(engine) as session :

        coach1 = Coach(nom_coach= "Maxime", specialite="Yoga et Pilates")
        coach2 = Coach(nom_coach= "Nicolas", specialite="Crossfit et Pump")
        coach3 = Coach(nom_coach= "Arnold", specialite="Musculation")
        coach4 = Coach(nom_coach= "Mike", specialite="Boxe et Body Combat")
        session.add(coach1)
        session.add(coach2)
        session.add(coach3)
        session.add(coach4)
        session.commit()

        horaire= dt.datetime(2024, 11, 19, 9,0,0)
        cours1 = Cours(nom_cours="Yoga et Pilates", 
            horaire_cours = horaire, 
            capacite_max=20,
            coach_id_cours = coach1.id_coach)
        
        session.add(cours1)
        session.commit()
        #session.refresh(coach1)
        #cours1.coach = coach1



if __name__ == "__main__":
    engine = idb.get_engine()
    populate_db(engine)
