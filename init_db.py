import sqlmodel as sm
from sqlalchemy import Engine

def get_engine() -> Engine :

    sqlitefile_name = "salle_de_sport.db"
    sqlite_url = f"sqlite:///{sqlitefile_name}"
    engine = sm.create_engine(sqlite_url, echo = True)

    return engine