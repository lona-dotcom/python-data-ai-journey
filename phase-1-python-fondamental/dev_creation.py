# 1- Création fiche d'identité de l'agent
agent_info = {
    "nom": "MonPremierAgent",
    "actif": True,
    "version": 1.0,
    "outils": ["recherche", "calcul"]
}
print(agent_info["nom"])  # Affiche le nom de l'agent
print(type(agent_info))  # Affiche le type de la variable agent_info