from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
import time
import random

app = FastAPI(title="SaaS User Manager API", description="API de démonstration pour architecture GitOps")

# Initialisation des métriques Prometheus
Instrumentator().instrument(app).expose(app)

# Base de données simulée en mémoire
users_db = []

@app.get("/health")
def health_check():
    """Endpoint utilisé par Kubernetes pour vérifier si l'app est en vie (Liveness Probe)."""
    return {"status": "healthy"}

@app.get("/users")
def get_users():
    """Retourne la liste des utilisateurs (avec une fausse latence pour les métriques Grafana)."""
    time.sleep(random.uniform(0.1, 0.3)) # Simule un temps de traitement
    return {"users": users_db, "count": len(users_db)}

@app.post("/users")
def create_user(name: str):
    """Ajoute un nouvel utilisateur."""
    user = {"id": len(users_db) + 1, "name": name}
    users_db.append(user)
    return {"message": "User created", "user": user}