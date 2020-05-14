# Projet science des données

Le projet consiste en l'application d'un modèle SIR les données covid françaises.

Le jeu de données utilisé est le csv data/covid/france/chiffres_cles.csv dont la source est https://www.data.gouv.fr/fr/datasets/chiffres-cles-concernant-lepidemie-de-covid19-en-france/

## Installation

Créer un environnement virtuel python, installer les dépendances de requirements.txt

`python3 -m virtualenv venv`

`source venv/bin/activate`

`python3 -m pip install -r requirements.txt`

`jupyter-notebook`

#### Notebook d'exploration : 

exploration_chiffres_cles.ipynb

#### Notebook de fitting : 

TestSIR_chiffres_cles.ipynb

#### Bonus

Des tests supplémentaires ont été réalisés avec le modèle SEIR dans le notebook SEIR_in_progress.ipynb