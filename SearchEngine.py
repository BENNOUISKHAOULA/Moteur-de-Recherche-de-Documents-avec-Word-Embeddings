import streamlit as st
import pandas as pd
import numpy as np
import spacy

# Chargez le modèle spaCy avec des vecteurs de mots (GloVe)
nlp = spacy.load("en_core_web_md")

# Chargez vos données de papier depuis le CSV
@st.cache_data
def load_data():
    df = pd.read_csv('2005.csv')
    return df

data = load_data()

# Code Streamlit pour l'interface utilisateur
st.title('Moteur de recherche de documents avec Word Embeddings')
user_query = st.sidebar.text_input("Entrez votre requête de recherche : ")
search_results = []  # Initialisez search_results avant le bloc try

if st.sidebar.button('Rechercher'):
    with st.spinner('Recherche de documents...'):
        try:
            # Recherche de documents basée sur les embeddings de mots
            for index, row in data.iterrows():
                title = row['Title']
                abstract = row['Abstract']
                doc = nlp(title + " " + abstract)

                # Calculez le vecteur moyen des mots pour le document
                doc_vector = np.mean([token.vector for token in doc if token.has_vector], axis=0)

                # Si le document n'a pas de vecteur, passez au suivant
                if doc_vector is None:
                    continue

                # Calculez la similarité cosinus entre la requête utilisateur et le document
                similarity = np.dot(doc_vector, np.mean([token.vector for token in nlp(user_query) if token.has_vector], axis=0))
                similarity /= (np.linalg.norm(doc_vector) * np.linalg.norm(np.mean([token.vector for token in nlp(user_query) if token.has_vector], axis=0)))

                # Vous pouvez ajuster le seuil pour contrôler la sensibilité de la correspondance
                minimum_similarity = 0.6
                if similarity > minimum_similarity:
                    search_results.append({
                        'Titre': title,
                        'Auteurs': row['Authors'],
                        'Résumé': abstract
                    })

            # Affichez les résultats de la recherche
            if not search_results:
                st.error("Aucun document correspondant trouvé.")
            else:
                st.success(f"Trouvé {len(search_results)} documents correspondant à votre requête :")
                for result in search_results:
                    st.markdown(f"## {result['Titre']}")
                    st.markdown(f"*Auteurs :* {result['Auteurs']}")
                    st.markdown(f"*Résumé :* {result['Résumé']}\n")

        except Exception as e:
            st.error(f"Une erreur s'est produite : {e}")

# Affichez les informations de débogage
st.write("Requête de l'utilisateur :", user_query)
st.write("Résultats de la recherche :",search_results)