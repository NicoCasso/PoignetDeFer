import streamlit as st

app_admin_coach_page = st.Page("app_admin_coach.py")

#app_admin_cours_page = st.Page("app_admin_cours.py")

pages = []
pages.append(app_admin_coach_page)
#pages.append(app_admin_cours_page)

pg = st.navigation(pages)

pg.run()