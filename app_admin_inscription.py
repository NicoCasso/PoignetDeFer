import streamlit as st
from init_db import get_engine
from sqlalchemy import Engine
from models import Cours, Coach, Inscription, Membre
import utils
from typing import cast
        
st.set_page_config(layout="wide")
st.title("Gestion des inscriptions")

engine = get_engine()
cours_list = utils.get_cours_list(engine)

cours_options = {}
cours_options[""] = -1
for cours in cours_list :
    if cours.coach_id !=  None :
        coach = utils.get_coach_by_id(engine, cours.coach_id)
        dict_key = "{0}, par {1}, le {2} à {3} h".format(
            cours.nom_cours,
            coach.nom_coach,
            cours.jour,
            cours.heure)
    else : 
        dict_key ="{0}, le {2} à {3} h".format(
            cours.nom_cours,
            cours.jour,
            cours.heure)
        
    cours_options[dict_key] = cours.id_cours

selected_cours = st.selectbox("sélectionner un cours", options = cours_options.keys()) 

#______________________________________________________________________________
#
# region list
#______________________________________________________________________________  

st.text("Inscriptions")
current_line = st.container(border=True)


column_proportions =[1,3,3,2]
column_id, column_date, column_member, column_delete = current_line.columns(column_proportions, gap ="small")

column_id.write("id")
column_date.write("date")
column_member.write("membre")
column_delete.write("action")

id_cours = cours_options[selected_cours]
    
if id_cours != -1 :

    inscription_list = utils.get_inscription_by_id(engine, id_cours)

    for inscription in inscription_list :
        column_id, column_date, column_member, column_delete = current_line.columns(column_proportions, gap ="small")
        column_id.write(str(inscription.id_inscription))
        column_date.write(inscription.date_inscription.date())
        member = utils.get_membre_by_id(engine, inscription.membre_id)
        column_member.write(member.nom_membre)
            
        if column_delete.button("annuler", key ="del"+str(inscription.id_inscription) ) :
            utils.delete_inscription(engine, inscription.id_inscription)
            st.session_state.clear()
            st.rerun()



