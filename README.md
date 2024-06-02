# Moteur de Recherche de Documents avec Word Embeddings

Ce projet utilise Streamlit pour créer une interface utilisateur permettant de rechercher des documents basés sur les embeddings de mots avec spaCy et les vecteurs GloVe.

## Description

Ce moteur de recherche permet de trouver des documents pertinents en fonction d'une requête utilisateur. Il utilise des embeddings de mots pour calculer la similarité entre la requête et les documents disponibles, affichant les résultats qui dépassent un certain seuil de similarité.

## Fonctionnalités

- Chargement des données de papier depuis un fichier CSV.
- Recherche de documents basée sur les embeddings de mots et la similarité cosinus.
- Interface utilisateur interactive avec Streamlit.
- Affichage des résultats de recherche avec les titres, auteurs et résumés des documents.

## Prérequis

- Python 3.6 ou plus récent
- spaCy
- Streamlit
- pandas
- numpy

## Installation

1. Clonez ce dépôt :

   ```bash
   git clone https://github.com/votre-utilisateur/moteur-recherche-documents.git
   cd moteur-recherche-documents
2. Installez les dépendances :

  pip install -r requirements.txt
  Le fichier requirements.txt devrait contenir les lignes suivantes :

    ```bash
    -plaintext
    -Copier le code
    -streamlit
    -pandas
    -numpy
    -spacy

3. Téléchargez et installez le modèle spaCy avec les vecteurs de mots GloVe :

    python -m spacy download en_core_web_md

Utilisation
  -Placez votre fichier CSV nommé 2005.csv dans le même répertoire que le script Python.

  -Exécutez l'application Streamlit :
  
    streamlit run votre_script.py
  
  -Remplacez votre_script.py par le nom de votre fichier contenant le code Python.

  -Ouvrez votre navigateur web et accédez à http://localhost:8501 pour utiliser l'application.
