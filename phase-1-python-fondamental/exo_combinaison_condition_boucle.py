messages_utilisateur = ["quelle heure est-il ?", "calcule 5 + 3", "raconte une blague"]

for message in messages_utilisateur:
    if "calcule" in message:
        print(f"[{message}] → outil choisi : calculatrice")
    elif "heure" in message:
        print(f"[{message}] → outil choisi : horloge")
    else:
        print(f"[{message}] → outil choisi : réponse directe du LLM")

# le boucle va s'executer 3 fois
# message 1: Horloge car il contient "heure"
# message 2: calculatrice car il contient "calcul"
# message 3: réponse directe du LLM car c'est autre que calcul et heure