from sqlmodel import Session, select, where
from sqlalchemy import Engine

from models import * 

def get_coaches(engine : Engine) -> list[Coach]:
    with Session(engine) as session:
        statement = select(Coach)
        result = session.exec(statement)
        return list(result)