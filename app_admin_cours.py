import streamlit as st
from init_db import get_engine
from sqlalchemy import Engine
import models
import utils
from typing import cast
        
st.title("Administration Cours")