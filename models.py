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
    jour : str
    heure : int 
    capacite_max : int

    coach_id : Optional[int]= Field(default=None, foreign_key="coach.id_coach")
    coach: Optional[Coach] = Relationship(back_populates="liste_cours")

    liste_inscriptions  : list["Inscription"] = Relationship(back_populates="cours")

class Membre(SQLModel, table = True):
    id_membre : int | None = Field(default=None, primary_key=True)
    nom_membre : str
    email : str
    
    carte_acces_id : int | None = Field(default=None, foreign_key="carte_d_acces.id_carte")
    #carte__acces

class Inscription(SQLModel, table = True):
    id_inscription : int | None = Field(default=None, primary_key=True)
    date_inscription : dt.datetime

    membre_id : int | None = Field(default=None, foreign_key="membre.id_membre")

    cours_id : int | None = Field(default=None, foreign_key="cours.id_cours" )
    cours: Cours | None = Relationship(back_populates="liste_inscriptions")


class carte_d_acces(SQLModel, table = True):
    id_carte : int | None = Field(default=None, primary_key=True)
    key : int


 



    
