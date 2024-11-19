import sqlmodel as sm
import datetime as dt
from models import *

horaire= dt.datetime(2024, 11, 19, 9,0,0)

coach1 = Coach(nom_coach= "Maxime", specialite="Yoga")

cours1 = Cours(nom_cours="Yoga", 
    horaire_cours = horaire, 
    capacite_max=20)

# /home/nicolascassonnet/Documents/WORK/LaPoigneDAcier/test_db.db
sqlitefile_name = "test_db.db"
sqlite_url = f"sqlite:///{sqlitefile_name}"
engine = sm.create_engine(sqlite_url, echo = True)

echo_object = sm.SQLModel.metadata.create_all(engine)
print(echo_object)

with sm.Session(engine) as session:
    session.add(coach1)
    session.commit()

    session.refresh(coach1)

    cours1.coach = coach1
    session.add(cours1)
    session.commit()


