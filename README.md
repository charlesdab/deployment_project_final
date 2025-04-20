
# 🚗 Getaround - Projet de déploiement Data Science

Ce projet répond à une étude de cas proposée par Getaround, une plateforme de location de voitures entre particuliers. Il comprend :
- Une **analyse exploratoire des retards** (EDA),
- Une **modélisation de prédiction de prix** de location journalière,
- Le **déploiement d’une API** pour prédire le prix,
- Et un **dashboard interactif Streamlit** en ligne.

---

## 🎯 Objectifs du projet

- Étudier les **retards à la restitution** des véhicules
- Comprendre l’impact de ces retards sur les locations suivantes
- Aider l’équipe produit à définir un **seuil de sécurité** entre deux locations
- Prédire le **prix optimal** de location via un modèle de machine learning
- Fournir une **API FastAPI** et un **dashboard Streamlit** exploitables

---

## 🚀 Démonstrations en ligne

### 🧠 Tester l'API en ligne

Accès rapide à l'interface Swagger (FastAPI) :
➡️ https://charld-getaround-deployment-project.hf.space/docs

Vous pouvez utiliser cet exemple de requête :

```json
{
  "input": [
    ["Citroën", 140411, 100, "diesel", "black", "convertible", true, true, false, false, true, true, true]
  ]
}
```

### 📊 Dashboard EDA (Streamlit)

Explorez les retards, l'impact des check-ins, et simulez des **seuils de sécurité** :
➡️ https://huggingface.co/spaces/charlD/getaround_streamlit_dashboard_final

---

## 🧱 Structure du projet

```
deployment_project/
├── api/
│   ├── app.py                  # API FastAPI
│   └── requirements.txt        # Dépendances API
├── streamlit/
│   ├── dashboard_streamlit_final.py  # Dashboard interactif
├── data/
│   ├── get_around_pricing_project.csv
│   ├── get_around_delay_analysis.xlsx
├── outputs/
│   └── best_model_v5.joblib    # Modèle entraîné
├── notebooks/
│   ├── model_v5_getaround.ipynb
│   └── EDA_getaround.ipynb
├── Dockerfile                  # Déploiement API
└── README.md                   # Ce fichier
```

---

## 🧠 Modèle de prédiction

- Modèle : `RandomForestRegressor` avec `GridSearchCV`
- Pipeline avec :
  - Encodage catégoriel (`OneHotEncoder`)
  - Standardisation (`StandardScaler`)
  - Imputation des valeurs manquantes
- Sauvegarde du meilleur modèle dans `/outputs`

---

## 📦 Installation et exécution locale

### ▶️ Lancer l'API FastAPI en local :
```bash
uvicorn app:app --reload
```

### ▶️ Lancer le Dashboard Streamlit en local :
```bash
streamlit run dashboard_streamlit_final.py
```

---

## 📌 Auteurs et projet

Projet réalisé dans le cadre de la certification Data Science (Jedha Bootcamp).

Toutes les étapes ont été réalisées par [charlesdab](https://github.com/charlesdab).

## 📁 Lien vers le dépôt GitHub

🔗 https://github.com/charlesdab/deployment_project_final

---
