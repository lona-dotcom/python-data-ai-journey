taches = [
    {"nom": "etudier", "urgence": 10},
    {"nom": "danser", "urgence": 1} ,
    {"nom": "travailler", "urgence": 9},
    {"nom": "manger", "urgence": 6}
]
for tache in taches:
    if tache["urgence"] > 7:
        print(f"{tache["nom"]} est 🔴 URGENT")
    elif tache["urgence"] <= 7 and tache["urgence"] > 4:
        print(f"{tache["nom"]} est 🟡 Moyen")
    else:
        print(f"{tache["nom"]} est 🟢 Faible")