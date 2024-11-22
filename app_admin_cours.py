import streamlit as st
from init_db import get_engine
from sqlalchemy import Engine
from models import Cours, Coach
import utils
from typing import cast
from streamlit_modal import Modal
        
st.set_page_config(layout="wide")
st.title("Administration Cours")

edit_mode = False
edit_mode_key = st.session_state.get("edit_mode")
if edit_mode_key != None :
    edit_mode = bool(edit_mode_key)

engine = get_engine()

left_side, right_side = st.columns([0.7, 0.3])

cours_list = utils.get_cours_list(engine)

#______________________________________________________________________________
#
# region left side list
#______________________________________________________________________________  

left_side.text("Liste des cours")
current_line = left_side.container(border=True)

column_proportions =[1, 3, 2, 2, 3, 2, 3, 3 ]
column_id, column_name, column_coach, column_jour, column_heure, column_capacite, column_update, column_delete = current_line.columns(column_proportions, gap ="small")

column_name.write("nom")
column_coach.write("coach")
column_jour.write("jour")
column_heure.write("heure")
column_capacite.write("capacité")
column_update.write("action")
column_delete.write("action")

for cours in cours_list :
    column_id, column_name, column_coach, column_jour, column_heure, column_capacite, column_update, column_delete = current_line.columns(column_proportions, gap ="small")
    column_id.write(str(cours.id_cours))
    column_name.write(cours.nom_cours)
    if cours.coach_id != None :
        coach = utils.get_coach_by_id(engine, cours.coach_id)
        column_coach.write(coach.nom_coach)
    else : 
        column_coach.write("")

    column_jour.write(cours.jour)
    column_heure.write(f"{cours.heure} h")
    column_capacite.write(str(cours.capacite_max))
    button_key = "upd"+str(cours.id_cours)
    if column_update.button("modifier", key=button_key) :
        st.session_state["edit_mode"] = True
        st.session_state["button_key"] = button_key
        st.rerun()
        
    if column_delete.button("supprimer", key ="del"+str(cours.id_cours) ) :
        utils.delete_cours(engine, cours.id_cours)
        st.session_state.clear()
        st.rerun()

#______________________________________________________________________________
#
# region right side form
#______________________________________________________________________________    

updating_cours = None
if edit_mode : 

    id_cours = 0
    any_key = st.session_state.get("button_key") 
    if any_key != None :
        id_cours = int ( str(any_key).replace("upd", ""))

    updating_cours = None
    if id_cours != 0 :
        updating_cours = utils.get_cours_by_id(engine, id_cours)


if updating_cours != None : 
    updating_cours = cast(Cours, updating_cours)
    right_side.text("Modifier cours")
    edit_mode = True
else :
    right_side.text("Nouveau cours")

current_line = right_side.container(border=True)

right_side_proportions = [0.4, 0.6]
column_label, column_textbox = current_line.columns(right_side_proportions, vertical_alignment="center")
column_label.write("nom : ")
cours_options = utils.get_nom_cours_options()
if edit_mode :
    form_nom_cours = column_textbox.selectbox("", options=cours_options, value = updating_cours.nom_cours , key = "nom_cours")
else :
    form_nom_cours = column_textbox.selectbox("", options=cours_options, key = "nom_cours")

column_label, column_textbox = current_line.columns(right_side_proportions, vertical_alignment="center")
column_label.write("coach : ")

coach_list = utils.get_coach_list(engine)
coach_options = utils.get_coach_options(coach_list)
if edit_mode :
    updating_coach = None
    if updating_cours.coach_id != None :
        updating_coach = utils.get_coach_by_id(engine, updating_cours.coach_id)

    if updating_coach != None :
        form_nom_coach = column_textbox.selectbox("", options=coach_options, value = updating_coach.nom_coach , key = "nom_coach")
    else :
        form_nom_coach = column_textbox.selectbox("", options=coach_options, key = "nom_coach")
else :
    form_nom_coach = column_textbox.selectbox("", options=coach_options, key = "nom_coach")

column_label, column_textbox = current_line.columns(right_side_proportions, vertical_alignment="center")
column_label.write("jour : ")
jour_options = utils.get_jour_options() 
if edit_mode :
    form_jour_cours = column_textbox.selectbox("", options=jour_options, value = updating_cours.jour , key = "jour_cours")
else :
    form_jour_cours = column_textbox.selectbox("", options=jour_options, key = "jour_cours")

column_label, column_textbox = current_line.columns(right_side_proportions, vertical_alignment="center")
column_label.write("heure : ")
heure_options = utils.get_heure_options()
if edit_mode :
    form_heure_cours = column_textbox.selectbox("", options= heure_options, value = updating_cours.heure , key = "heure_cours")
else :
    form_heure_cours = column_textbox.selectbox("", options= heure_options, key = "heure_cours")

column_label, column_textbox = current_line.columns(right_side_proportions, vertical_alignment="center")
column_label.write("capacité : ")
if edit_mode :
    form_capacite_cours = column_textbox.text_input("", value = updating_cours.capacite_max , key = "capacite_cours")
else :
    form_capacite_cours = column_textbox.text_input("", key = "capacite_cours")
    

column_label, column_textbox = current_line.columns([0.45, 0.55], vertical_alignment="center")
if edit_mode :

    if column_label.button("Annuler") :
        st.session_state.clear()  
        st.rerun()

    if column_textbox.button("Modifier") : 
        cours = utils.validate_cours(
            str(form_nom_cours),
            str(form_nom_coach),
            coach_list,
            str(form_jour_cours),
            str(form_heure_cours),
            int(form_capacite_cours), 
            int(updating_cours.id_cours)
        )   
        if cours != None :
            utils.update_cours(engine, cours)
        else :
             with Modal(key="Impossible_upd", title="Modification impossible").container():
                st.markdown("Désolé, ça n'est pas possible")

        st.session_state.clear()   
        st.rerun()

else :

    column_label.write("")
    if column_textbox.button("Ajouter") :
        cours = utils.validate_cours(
            str(form_nom_cours),
            str(form_nom_coach),
            coach_list,
            str(form_jour_cours),
            str(form_heure_cours),
            int(form_capacite_cours)
        )   
        if cours != None :
            utils.create_cours(engine, cours)
        else :
            with Modal(key="Impossible_cre", title="Création impossible").container():
                st.markdown("Désolé, ça n'est pas possible")

        st.session_state.clear()  
        st.session_state["nom_cours"] = 0
        st.session_state["nom_coach"] = 0
        st.session_state["jour_cours"] = 0
        st.session_state["heure_cours"] = 0
        st.session_state["capacite_cours"] = 0

        st.rerun()      