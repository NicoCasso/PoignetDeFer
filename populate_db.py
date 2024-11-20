import sqlmodel as sm
from sqlalchemy import Engine

import datetime as dt
from models import *
import init_db as idb

def populate_db(engine : Engine) :
    echo_object = sm.SQLModel.metadata.create_all(engine)
    print(echo_object)

    horaire= dt.datetime(2024, 11, 19, 9,0,0)

    coach1 = Coach(nom_coach= "Maxime", specialite="Yoga")

    cours1 = Cours(nom_cours="Yoga", 
        horaire_cours = horaire, 
        capacite_max=20)

    with sm.Session(engine) as session:
        session.add(coach1)
        session.commit()

        session.refresh(coach1)
        cours1.coach = coach1
        session.add(cours1)

if __name__ == "__main__":
    engine = idb.get_engine()
    populate_db(engine)
