import streamlit as st



app_membre_inscription_page = st.Page("app_membre_inscription.py", title="inscription à un cours")
app_membre_historique_page =st.Page("app_membre_historique.py", title="Historique des cours")
app_admin_coach_page = st.Page("app_admin_coach.py", title="Gestion des coaches")
app_admin_cours_page = st.Page("app_admin_cours.py", title="Gestion des cours")
app_admin_inscription_page = st.Page("app_admin_inscription.py", title="Gestion des Inscriptions")

pages = []

pages.append(app_membre_inscription_page)
pages.append(app_membre_historique_page)
pages.append(app_admin_coach_page)
pages.append(app_admin_cours_page)
pages.append(app_admin_inscription_page)

pg = st.navigation(pages)

pg.run()