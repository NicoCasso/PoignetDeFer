import sqlmodel as sm
from sqlalchemy import Engine

import datetime as dt
from models import *
import init_db as idb

def populate_db(engine : Engine) :
    echo_object = sm.SQLModel.metadata.create_all(engine)
    print(echo_object)

    try: 
        session = sm.Session(engine) 

        coach1 = Coach(nom_coach= "Maxime", specialite="Yoga")
        session.add(coach1)
        session.commit()

        horaire= dt.datetime(2024, 11, 19, 9,0,0)
        cours1 = Cours(nom_cours="Yoga et Pilates", 
            horaire_cours = horaire, 
            capacite_max=20,
            coach_id_cours = coach1.id_coach)
        
        session.add(cours1)

        #session.refresh(coach1)
        #cours1.coach = coach1
        

    except:
        print("Erroe")


if __name__ == "__main__":
    engine = idb.get_engine()
    populate_db(engine)
