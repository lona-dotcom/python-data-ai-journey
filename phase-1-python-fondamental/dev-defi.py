# 1. Création de l'historique : une liste qui va contenir les messages
historique = [

    # 2. Premier message : l'utilisateur pose une question
    {
        "role": "user",
        "contenu": "Bonjour, peux-tu me dire quelle est la capitale de la France ?"
    },

    # 3. Deuxième message : l'assistant répond
    {
        "role": "assistant",
        "contenu": "La capitale de la France est Paris."
    },

    # 4. Troisième message : l'utilisateur rebondit
    {
        "role": "user",
        "contenu": "Et combien d'habitants y vivent ?"
    }
]

# 5. Afficher UNIQUEMENT le contenu du 2e message (index 1)
print(historique[1]["contenu"])
# → La capitale de la France est Paris.

# 6. Afficher le nombre total de messages
print(len(historique))
# → 3