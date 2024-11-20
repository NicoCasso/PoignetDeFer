from sqlmodel import select, delete
from sqlmodel import Session as SqlModelSession
from sqlalchemy import Engine

from models import * 

def get_coaches(engine : Engine) -> list[Coach]:
    return_list = []
    with SqlModelSession(engine) as session2:
        statement = select(Coach)
        result = session2.exec(statement)
        return_list = list(result)

    return return_list
    
def create_coach(engine : Engine, coach : Coach) -> bool:
    ended = False
    with SqlModelSession(engine) as session2:
        id = coach.id_coach
        session2.add(coach)
        try:
            session2.commit()
            ended = True
        except Exception as e:
            print("---------------->"+str(e))
    
    return ended

def update_coach(engine : Engine, coach : Coach) -> bool:
    with SqlModelSession(engine) as session2:
        statement = select(Coach).where(Coach.id_coach == coach.id_coach)
        results = session2.exec(statement)
        linked_coach = results.one()
        linked_coach.nom_coach = coach.nom_coach
        linked_coach.specialite = coach.specialite
        session2.add(linked_coach)
        session2.commit()
        return True
    
    return False

    
def delete_coach(engine : Engine, coach: Coach) -> bool:
    with SqlModelSession(engine) as session2:
        statement = select(Coach).where(Coach.id_coach == coach.id_coach)
        results = session2.exec(statement)
        linked_coach = results.one()
        session2.delete(linked_coach)
        session2.commit()
        return True
    
    return False