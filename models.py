from sqlmodel import Field, Relationship, SQLModel
import datetime as dt
from typing import Optional

class Coach(SQLModel, table = True):
    id_coach : Optional[int] = Field(default=None, primary_key=True)
    nom_coach: str
    specialite :str 

    liste_cours : list["Cours"] = Relationship(back_populates="coach")

class Cours(SQLModel, table = True):
    id_cours : Optional[int] = Field(default=None, primary_key=True)
    nom_cours: str
    horaire_cours : dt.datetime
    capacite_max : int

    coach_id : Optional[int]= Field(default=None, foreign_key="coach.id_coach")
    coach: Optional[Coach] = Relationship(back_populates="liste_cours")



    
