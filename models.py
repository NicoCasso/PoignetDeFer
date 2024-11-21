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

class Membres(SQLModel, table = True):
    id_membres : int | None = Field(default=None, primary_key=True)
    nom_membres : str
    email : str
    
    
    carte_acces_id : int | None = Field(default=None, foreign_key="carte_d_acces.id_carte")
    carte__acces

class inscriptions(SQLModel, table = True):
    id_inscriptions : int | None = Field(default=None, primary_key=True)
    date_inscriptions : dt.datetime

    membre_id : int | None = Field(default=None, foreign_key="membres.id_membres")

    cours_id_inscription : int | None = Field(default=None, foreign_key="cours.id_cours" )


class carte_d_acces(SQLModel, table = True):
    id_carte : int | None = Field(default=None, primary_key=True)
    key : int


 



    
