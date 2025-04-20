FROM python:3.10-slim

WORKDIR /app

# Copier le fichier requirements.txt du dossier app
COPY app/requirements.txt /app/

# Installer les dépendances
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copier tout le reste du projet dans le conteneur
COPY . /app/

# Démarrer le serveur avec uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]
