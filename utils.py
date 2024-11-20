from sqlmodel import Session, select, where
from sqlalchemy import Engine

from models import * 

def get_coaches(engine : Engine):
    with Session(engine) as session:
        statement = select(Coach, Cours).where(Coach.id_coach == Cours.coach_id)