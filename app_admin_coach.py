import streamlit as st
from init_db import get_engine
from sqlalchemy import Engine
import models
import utils

st.title("Administration Coach")

engine = get_engine()

left_side, right_side = st.columns(2)

coaches = utils.get_coaches(engine)

left_side.title("Liste des coaches")
current_line = left_side.container()
column_id, column_name, column_specialite, column_update, column_delete = current_line.columns(5, gap ="small")

column_id.write("id")
column_name.write("nom")
column_name.write("specialite")
column_update.write("action")
column_update.write("action")

for coach in coaches :
    column_id, column_name, column_specialite, column_update, column_delete = current_line.columns(5, gap ="small")                                             "small")
    column_id.write(coach.id_coach)
    column_name.write(coach.nom_coach)
    column_name.write(coach.specialite)
    if column_update.button("modifier"+str(coach.id_coach)) :
        pass
        
    if column_update.button("supprimer"+str(coach.id_coach)) :
        pass

with right_side.form("form_add", clear_on_submit=True) :
    right_side.title("Nouveau coach")
    current_line = right_side.container()
    column_label, column_textbox = current_line.columns(2)
    form_nom_coach = column_label.text("nom : ")
    column_textbox.text_input("", key = "nom_coach")
    column_label, column_textbox = current_line.columns(2)
    column_label.text("specialite :")
    form_specialite_coach = column_textbox.text_input("", key = "specialite_coach")
    if right_side.form_submit_button("Ajouter") :
        coach = models.Coach(nom_coach = form_nom_coach, specialite=form_specialite_coach)
        utils.update_coach(coach)
        st.rerun()




