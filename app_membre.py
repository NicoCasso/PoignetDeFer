import streamlit as st



app_membre_inscription_page = st.Page("app_membre_inscription.py")
app_membre_historique_page =st.Page("app_membre_historique.py")

#app_admin_cours_page = st.Page("app_admin_cours.py")

pages = []
pages.append(app_membre_inscription_page)
pages.append(app_membre_historique_page)
#pages.append(app_admin_cours_page)

pg = st.navigation(pages)

pg.run()