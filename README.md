# Application de Gestion de Calendrier des Cours et d'Inscription des Participants


## Version
    0.9.0

## Description

Cette application permet de gérer un calendrier de cours et d'inscrire des participants. Elle offre des fonctionnalités pour les administrateurs et les élèves :

- **Côté Administrateur** :
  - Créer des cours
  - Ajouter des coachs
  - Ajouter des élèves

- **Côté Élève** :
  - S'inscrire aux cours

## Fonctionnalités

### Côté Administrateur

1. **Créer des Cours** :
   - Ajouter des détails sur le cours, y compris le nom, l'heure de début, le jour de la semaine et la capacité maximale des élèves.
   - Associer un coach au cours.

2. **Ajouter des Coachs** :
   - Saisir le nom du coach et sa spécialité pour l'ajouter à la base de données.

3. **Ajouter des Élèves** :
   - Enregistrer les informations des élèves, y compris le nom, l'email et la carte d'accès.

### Côté Élève

1. **S'inscrire aux Cours** :
   - Parcourir la liste des cours disponibles.
   - S'inscrire aux cours de leur choix.

## Installation

1. **Cloner le dépôt** :
   ```bash
   git clone https://github.com/NicoCasso/PoignetDeFer.git
   cd votre-repo


2. **installer les dépendances** :
    pip install -r requirements.txt

3. **Créer la base de données** :

    Dans VSC, terminal, taper la commande 
    python3 populate_db.py 
   


## Lancer L’application

    streamlit run app_membre.py pour l’interface membre seulement
    streamlit run app_admin.py pour l’interface admin seulement
    streamlit run app_general.py interface globale

## Licence MIT












