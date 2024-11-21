import streamlit as st
from init_db import get_engine
from sqlalchemy import Engine
import models
import utils
from typing import cast
        
st.set_page_config(layout="wide")
st.title("Administration Coach")

edit_mode = False
edit_mode_key = st.session_state.get("edit_mode")
if edit_mode_key != None :
    edit_mode = bool(edit_mode_key)

engine = get_engine()

left_side, right_side = st.columns([0.7, 0.3])

coaches = utils.get_coaches(engine)

#______________________________________________________________________________
#
# region left side list
#______________________________________________________________________________  

left_side.text("Liste des coaches")
current_line = left_side.container(border=True)

column_proportions =[0.1,0.2,0.25,0.2,0.25]
column_id, column_name, column_specialite, column_update, column_delete = current_line.columns(column_proportions, gap ="small")

column_id.write("id")
column_name.write("nom")
column_specialite.write("specialite")
column_update.write("action")
column_delete.write("action")

for coach in coaches :
    column_id, column_name, column_specialite, column_update, column_delete = current_line.columns(column_proportions, gap ="small")
    column_id.write(str(coach.id_coach))
    column_name.write(coach.nom_coach)
    column_specialite.write(coach.specialite)
    button_key = "upd"+str(coach.id_coach)
    if column_update.button("modifier", key=button_key) :
        st.session_state["edit_mode"] = True
        st.session_state["button_key"] = button_key
        st.rerun()
        
    if column_delete.button("supprimer", key ="del"+str(coach.id_coach) ) :
        utils.delete_coach(engine, coach.id_coach)
        st.session_state.clear()
        st.rerun()

#______________________________________________________________________________
#
# region right side form
#______________________________________________________________________________    

updating_coach = None
if edit_mode : 

    id_coach = 0
    any_key = st.session_state.get("button_key") 
    if any_key != None :
        id_coach = int ( str(any_key).replace("upd", ""))

    updating_coach = None
    if id_coach != 0 :
        updating_coach = utils.get_coach_by_id(engine, id_coach)


if updating_coach != None : 
    updating_coach = cast(models.Coach, updating_coach)
    right_side.text("Modifier coach")
    edit_mode = True
else :
    right_side.text("Nouveau coach")

current_line = right_side.container(border=True)

right_side_proportions = [0.4, 0.6]
column_label, column_textbox = current_line.columns(right_side_proportions, vertical_alignment="center")
column_label.write("nom : ")
if edit_mode :
    form_nom_coach = column_textbox.text_input("", value = updating_coach.nom_coach , key = "nom_coach")
else :
    form_nom_coach = column_textbox.text_input("", key = "nom_coach")
    

column_label, column_textbox = current_line.columns(right_side_proportions, vertical_alignment="center")
column_label.write("specialite :")
if edit_mode :
    form_specialite_coach = column_textbox.text_input("", value = updating_coach.specialite, key ="specialite_coach")
else :
    form_specialite_coach = column_textbox.text_input("", key ="specialite_coach")

column_label, column_textbox = current_line.columns([0.45, 0.55], vertical_alignment="center")
if edit_mode :

    if column_label.button("Annuler") :
        st.session_state.clear()  
        st.rerun()

    if column_textbox.button("Modifier") :      
        if form_nom_coach != "" and form_specialite_coach != "" :
            coach = models.Coach(id_coach=updating_coach.id_coach, nom_coach = form_nom_coach, specialite=form_specialite_coach)
            utils.update_coach(engine, coach)

        st.session_state.clear()   
        st.rerun()

else :

    column_label.write("")
    if column_textbox.button("Ajouter") :
        if form_nom_coach != "" and form_specialite_coach != "" :
            coach = models.Coach(nom_coach = form_nom_coach, specialite=form_specialite_coach)
            utils.create_coach(engine, coach)

        st.session_state.clear()  
        st.session_state["nom_coach"] = ""
        st.session_state["specialite_coach"] = ""
        st.rerun()          
