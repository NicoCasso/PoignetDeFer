from sqlmodel import Session, select, delete
from sqlalchemy import Engine
from typing import cast
from models import * 

#______________________________________________________________________________
#
# region Coach
#______________________________________________________________________________

def get_coach_list(engine : Engine) -> list[Coach]:
    return_list = []
    with Session(engine) as session:
        statement = select(Coach)
        result = session.exec(statement)
        return list(result)
    
def create_coach(engine : Engine, coach : Coach) -> bool:
    with Session(engine) as session:
        session.add(coach)
        session.commit()
        return True
    
    return False

def get_coach_by_id(engine : Engine, id_coach: int) -> Coach:
    return_value = None
    with Session(engine) as session:
        statement = select(Coach).where(Coach.id_coach == id_coach) #.where(Coach.id_coach == Cours.coach_id)
        results = session.exec(statement)
        return_value = results.one()

    return return_value

def update_coach(engine : Engine, coach : Coach) -> bool:
    with Session(engine) as session:
        statement = select(Coach).where(Coach.id_coach == coach.id_coach)
        results = session.exec(statement)
        linked_coach = results.one()
        linked_coach.nom_coach = coach.nom_coach
        linked_coach.specialite = coach.specialite
        session.add(linked_coach)
        session.commit()
        return True
    
    return False
    
def delete_coach(engine : Engine, coach_id: int) -> bool:
    with Session(engine) as session:
        statement = select(Coach).where(Coach.id_coach == coach_id)
        results = session.exec(statement)
        linked_coach = results.one()
        session.delete(linked_coach)
        session.commit()
        return True
    
    return False

#______________________________________________________________________________
#
# region Cours
#______________________________________________________________________________


def get_cours_list(engine : Engine) -> list[Cours]:
    list_cours = []
    with Session(engine) as session:
        statement = select(Cours)
        results = session.exec(statement)
        list_cours = list(results)
        
    return list_cours

def get_cours_by_id(engine : Engine, id_cours: int) -> Coach:
    return_value = None
    with Session(engine) as session:
        statement = select(Cours).where(Cours.id_cours == id_cours) 
        results = session.exec(statement)
        return_value = results.one()

    return return_value

def create_cours(engine : Engine, cours : Cours) -> bool:
    with Session(engine) as session:
        statement = select(Cours)
        results = session.exec(statement)
        cours_list = list(results)
        for autre_cours in cours_list :
            if autre_cours.id_cours == cours.id_cours :
                continue

            if autre_cours.heure == cours.heure and autre_cours.jour==cours.jour :
                return False  
            
        session.add(cours)
        session.commit()
        return True
    
    return False

def update_cours(engine : Engine, cours : Cours) -> bool:
    with Session(engine) as session:
        statement = select(Cours)
        results = session.exec(statement)
        cours_list = list(results)
        selected = None
        for autre_cours in cours_list :
            if autre_cours.id_cours == cours.id_cours :
                selected = autre_cours
                continue

            if autre_cours.heure == cours.heure and autre_cours.jour==cours.jour :
                return False
            
        if selected == None:
            return False
            
        selected.nom_cours = cours.nom_cours
        selected.coach_id = cours.coach_id
        selected.jour = cours.jour
        selected.heure = cours.heure
        selected.capacite_max = cours.capacite_max
            
        session.add(selected)
        session.commit()
        return True
    
    return False
    
def delete_cours(engine : Engine, cours_id: int) -> bool:
    with Session(engine) as session:
        statement = select(Cours).where(Cours.id_cours == cours_id)
        results = session.exec(statement)
        linked_cours = results.one()
        session.delete(linked_cours)
        session.commit()
        return True
    
    return False

def validate_cours(nom_cours :str, nom_coach:str, coach_list: list[Coach], jour:str, heure:str, capacite:str, id_cours : int = -1) -> Optional[Cours] :
    if nom_cours== "" or nom_cours not in get_nom_cours_options() : return None
    if nom_coach not in list(map(lambda c: c.nom_coach, coach_list)) : return None
    if jour == "" or jour not in get_jour_options() : return None
    if heure =="0" or heure not in get_heure_options() : return None
    if not capacite.isdecimal() : return None
    capacite = int(capacite) 
    if capacite <1 or capacite > 42 : return None
    
    id_coach = list(filter(lambda c: c.nom_coach==nom_coach, coach_list))[0].id_coach
    heure = int(heure.replace(" h", ""))

    if id_cours == -1 :
        cours = Cours(nom_cours=nom_cours, jour=jour, heure = heure, capacite_max=capacite, coach_id =id_coach)
    else :
        cours = Cours(id_cours = id_cours, nom_cours=nom_cours, jour=jour, heure = heure, capacite_max=capacite, coach_id =id_coach)

    return cours

def get_coach_options(coach_list: list[Coach]):
    coach_options = [""]
    for nom in map(lambda c : c.nom_coach, coach_list):
        coach_options.append(nom)

    return coach_options

def get_nom_cours_options() :
    return ["", "Yoga et Pilates", "CrossFit et Pump", "Musculation ", "Boxe et Body Combat" ]

def get_jour_options() :
    return ["", "lundi", "mardi", "mercredi", "jeudi", "vendredi"]

def get_heure_options() :
    return ["", "9 h", "10 h", "11 h", "12 h", "13 h", "14 h", "15 h", "16 h" ]

#______________________________________________________________________________
#
# region Inscriptions
#______________________________________________________________________________

def delete_inscription(engine : Engine, inscription_id: int) -> bool:
    with Session(engine) as session:
        statement = select(Inscription).where(Inscription.id_inscription == inscription_id)
        results = session.exec(statement)
        linked_inscription = results.one()
        session.delete(linked_inscription)
        session.commit()
        return True
    
    return False

#______________________________________________________________________________
#
# region maxime
#______________________________________________________________________________


def afficher_cours_dispo(engine : Engine) -> list[Cours]:
    cours = []
    with Session(engine) as session:
        statement = select(Cours)
        result = session.exec(statement)
        cours=list(result)
        
    return cours

def get_inscription_by_id(engine : Engine, cours_id:int) -> list[Inscription]: 
    inscriptions_list = []
    with Session(engine) as session:  
        statement = select(Inscription).filter(Inscription.cours_id == cours_id)
        results = session.exec(statement)
        inscriptions_list = list(results)

    return inscriptions_list

def create_inscription(engine : Engine, cours_id:int, id_membre) -> bool:
    return_value = False
    with Session(engine) as session:
        statement = select(Membre).where(Membre.id_membre == id_membre)  
        results = session.exec(statement)
        membre=cast(Membre, results)
        if membre:
            date1=dt.datetime.now()
        
            inscription=Inscription(membre_id=id_membre, cours_id=cours_id,date_inscription=date1)
            session.add(inscription)
            session.commit()
            return_value=True

    return return_value

def get_membres_by_nom(engine : Engine, nom:str) -> list[Membre]:
    list_membres = []
    with Session(engine) as session:
        statement = select(Membre).where(Membre.nom_membre == nom)  
        results = session.exec(statement)
        list_membres = list(results)

    return list_membres

def get_history_by_id_membre(engine : Engine, id_membre:int) -> list[Inscription]:
    list_inscription = []
    with Session(engine) as session:
        statement = select(
            Inscription
        ).where (
            Inscription.membre_id== id_membre
        ).order_by(
            Inscription.date_inscription
        )  
        results = session.exec(statement)
        list_inscription = list(results)

    return list_inscription

def get_cours_by_inscriptions(engine : Engine, inscription_ids:list[int]) -> list[Cours]:
    list_cours = []
    with Session(engine) as session:
        statement = select(
            Cours, Inscription
        ).join( 
            Inscription
        ).where(
            Inscription.id_inscription.in_(inscription_ids)
        )  
        results = session.exec(statement)
        list_membres = list(results)
        
    return list_cours