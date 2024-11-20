from sqlmodel import Field, Relationship, SQLModel
import datetime as dt

class Coach(SQLModel, table = True):
    id_coach : int | None = Field(default=None, primary_key=True)
    nom_coach: str
    specialite :str 

    liste_cours : list["Cours"] = Relationship(back_populates="coach")

class Cours(SQLModel, table = True):
    id_cours : int | None = Field(default=None, primary_key=True)
    nom_cours: str
    horaire_cours : dt.datetime
    capacite_max : int

    coach_id : int | None = Field(default=None, foreign_key="coach.id_coach")
    coach: Coach | None = Relationship(back_populates="liste_cours")



    
