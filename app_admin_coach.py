import streamlit as st
from init_db import get_engine
from sqlalchemy import Engine
import models
import utils

st.title("Administration Coach")

engine = get_engine()

left_side, right_side = st.columns([0.7, 0.3])

coaches = utils.get_coaches(engine)

left_side.text("Liste des coaches")
current_line = left_side.container()

column_proportions =[0.1,0.2,0.25,0.2,0.25]
column_id, column_name, column_specialite, column_update, column_delete = current_line.columns(column_proportions, gap ="small")

column_id.write("id")
column_name.write("nom")
column_specialite.write("specialite")
column_update.write("action")
column_delete.write("action")

for coach in coaches :
    column_id, column_name, column_specialite, column_update, column_delete = current_line.columns(column_proportions, gap ="small")
    column_id.write(coach.id_coach, )
    column_name.write(coach.nom_coach)
    column_specialite.write(coach.specialite)
    if column_update.button("modifier", key="upd"+str(coach.id_coach)) :
        pass
        
    if column_delete.button("supprimer", key="del"+str(coach.id_coach)) :
        pass


current_line = right_side.container()
current_line.text("Nouveau coach")

right_side_proportions = [1, 1]

column_label, column_textbox = current_line.columns(right_side_proportions, vertical_alignment="top")
column_label.text("nom : ")
form_nom_coach = column_textbox.text_input("", key = "nom_coach")

column_label, column_textbox = current_line.columns(right_side_proportions, vertical_alignment="top")
column_label.text("specialite :")
form_specialite_coach = column_textbox.text_input("", key = "specialite_coach")

if current_line.button("Ajouter") :
    coach = models.Coach(nom_coach = form_nom_coach, specialite=form_specialite_coach)
    #engine = get_engine()
    utils.create_coach(engine, coach)
    st.rerun()


