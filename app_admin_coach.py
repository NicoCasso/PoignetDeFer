import streamlit as st
from init_db import get_engine
from sqlalchemy import Engine
from utils import get_coaches

st.Title("Page Admin Coach")

engine = get_engine()

coaches = get_coaches(engine)

for coach in coaches :
    st.write(coach?)