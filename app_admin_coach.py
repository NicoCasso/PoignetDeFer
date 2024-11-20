import streamlit as st
from init_db import get_engine
from sqlalchemy import Engine
from utils import get_coaches

st.title("Page Admin Coach")

engine = get_engine()

coaches = get_coaches(engine)

for coach in coaches :
    st.write("{0} {1} {2}".format(coach.id_coach, coach.nom_coach, coach.specialite))