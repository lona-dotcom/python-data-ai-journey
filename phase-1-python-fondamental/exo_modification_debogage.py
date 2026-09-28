scores_confiance = [1.0, 0.5, 0.6, 0.95, 0.42, 0.7, 0.15]

for score in scores_confiance:
    if score > 0.9:
        print(f"{score} → réponse excellente, aucune vérification nécessaire")
    elif score > 0.8:
        print(f"{score} → réponse fiable, on l'affiche à l'utilisateur")
    elif score > 0.5:
        print(f"{score} → réponse moyenne, on demande confirmation")
    else:
        print(f"{score} → réponse rejetée, trop incertaine")