# OpenClassroomsP7
 
-- BORDERON Julien  Mai 2022 --

Parcours Data Scientist

Projet n°7 : "Implémentez un modèle de scoring"

## Description du projet
* Classification supervisé sur un jeu de données déséquilibré 
* Choix d'une métrique adaptée à un problème métier de type bancaire à l'aide de la fonction F Beta Score
* Mise en place d'une API RESTFull pour appeler le modèle de prédiction hébergée sur Heroku
* Construction d'un dashboard interactif à l'aide de streamlit
* Utilisation de git et github pour versioning

Source des données : https://www.kaggle.com/c/home-credit-default-risk/data

## Vidéo du dashboard 
[Video dashboard](https://youtu.be/Xrx6LvBNug0)

## Jeux de données

df_pred_display.csv : jeu de données pour l'affichage des infos sur les clients dont on veut la prédiction

df_red_pred.csv : jeu de données réduit pour envoyer via l'API

df_red_train : jeu de données réduit pour l'affichage des infos sur les clients dont on connait déjà la valeur de la target
