# 💻 Projet RansomTrack - Détection de Ransomwares sur la Blockchain Bitcoin

## 📖 Description

Ce projet vise à détecter les adresses Bitcoin utilisées par des ransomwares, en analysant leurs **comportements transactionnels** dans la blockchain.  
À partir du dataset **BitcoinHeist**, nous avons entraîné un modèle **XGBoost** capable de classifier une adresse comme **légitime (white)** ou **suspecte (ransomware)**.

L’ensemble du projet est intégré dans un **dashboard interactif Streamlit**, permettant :
- D’analyser les patterns globaux du dataset.
- De tester une **nouvelle transaction** pour savoir si elle est suspecte ou non.

---

## 📂 Structure du Projet

```text
📂 RansomTrack/
├──  BitcoinHeistData.csv             # Dataset source
├── app.py                            # Application Streamlit complète (Dashboard + Prédiction)
├── fraude_detection_bitcoin.ipynb    # Notebook EDA + Modélisation
├── xgboost_ransomware_model.joblib   # Modèle XGBoost entraîné
├── requirements.txt                  # Liste des packages nécessaires
├── README.md                         # Ce fichier
```

---

## 📊 Présentation du Dataset - BitcoinHeist

- **Source** : Article scientifique "BitcoinHeist: Topological Data Analysis for Ransomware Detection on the Bitcoin Blockchain" (IJCAI 2020).
- **Période** : Transactions de **janvier 2009 à décembre 2018**.
- **Taille** : Environ 3 millions de transactions.
- **Classes** : 
    - `white` (adresse légitime)
    - 24 familles de ransomwares connues (CryptoLocker, Locky, Cerber, etc.)

---

## 📊 Explication des Variables Clés

| Variable | Description |
|--|--|
| **address** | Adresse Bitcoin étudiée |
| **year / day** | Date de l’activité de l’adresse |
| **length** | Nombre total de transactions associées à cette adresse |
| **weight** | Indicateur de fusion de fonds (combien d’inputs sont fusionnés dans les sorties) |
| **count** | Nombre total d’entrées et de sorties |
| **looped** | Nombre de bouclages (réutilisation de fonds avec des adresses déjà connues) |
| **neighbors** | Nombre d’adresses directement connectées |
| **income** | Montant total reçu (en satoshis) |
| **label** | Famille de ransomware ou `white` si légitime |

---

## ⚙️ Setup du Projet (Installation)

1. **Cloner le projet** :
    ```bash
    git clone https://github.com/akdiOussama/RansomTrack.git
    cd RansomTrack
    ```

2. **Créer un environnement virtuel** :
    ```bash
    python -m venv env
    env\Scripts\activate   # (Windows) 
    ```

3. **Installer les dépendances** :
    ```bash
    pip install -r requirements.txt
    ```

4. **Lancer l’application Streamlit** :
    ```bash
    streamlit run app.py
    ```

---

## 📊 Ce que fait l’application

✅ Dashboard d’exploration :
- Distribution des labels (white vs ransomware)
- Analyse de la fréquence des transactions ransomwares
- Analyse des montants (log scale)
- Top 5 des montants les plus fréquents chez les ransomwares

✅ Prédiction :
- L’utilisateur entre les caractéristiques d’une nouvelle transaction.
- Le modèle XGBoost prédit si cette adresse est **légitime ou suspecte**.
- Résultat affiché directement à l’écran.

---

## 📈 Modèle Utilisé

- Modèle : **XGBoost Classifier**
- Séparation : Train/Test (70/30)
- Optimisation : GridSearchCV
- Métriques : 
    - Recall ransomware : 72%
    - Précision ransomware : 83%
    - F1-score ransomware : 77%

---

## ✅ Objectif final

Ce projet fournit une **première brique opérationnelle** pour surveiller les paiements en Bitcoin et détecter les **tentatives de ransomwares**, tout en offrant aux analystes un outil visuel pour comprendre l’évolution de la menace.

---
