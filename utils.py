from sqlmodel import Session, select, delete
from sqlalchemy import Engine

from models import * 

def get_coaches(engine : Engine) -> list[Coach]:
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

    
def delete_coach(engine : Engine, coach: Coach) -> bool:
    with Session(engine) as session:
        statement = select(Coach).where(Coach.id_coach == coach.id_coach)
        results = session.exec(statement)
        linked_coach = results.one()
        session.delete(linked_coach)
        session.commit()
        return True
    
    return False