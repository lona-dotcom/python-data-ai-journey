message = [
    {"texte":"Bonjour, je suis un agent de modération pour les projets DeFi. Je suis ici pour vous aider à identifier et à signaler tout contenu inapproprié ou frauduleux dans l'écosystème DeFi. Veuillez fournir des détails sur le contenu que vous souhaitez signaler, et je ferai de mon mieux pour vous assister.", "longueur": 500, "contient_lien": True},
    {"texte": "Que puis-je faire pour vous aider aujourd'hui ? Veuillez fournir des informations sur le contenu que vous souhaitez signaler, et je vous guiderai à travers le processus de modération.", "longueur": 200, "contient_lien": False},
    {"texte": "Merci pour votre message. Je vais examiner le contenu que vous avez signalé et prendre les mesures nécessaires.", "longueur": 100, "contient_lien": True},
    {"texte": "Je suis désolé, mais je ne peux pas traiter votre demande sans plus de détails. Veuillez fournir des informations supplémentaires sur le contenu que vous souhaitez signaler.", "longueur": 350, "contient_lien": False},
    {"texte": "Je vous remercie de votre vigilance. Votre signalement a été pris en compte et sera examiné par notre équipe de modération.", "longueur": 150, "contient_lien": True}
]
nb_bloques = 0
for msg in message:
    if msg["longueur"] > 300 and msg["contient_lien"] == True:
        nb_bloques += 1
        print(f"{msg["texte"]}: --> 🚫 BLOQUÉ : message long avec lien suspect")
    elif msg["longueur"] > 300 or msg["contient_lien"] == True:
        print(f"{msg["texte"]}: --> ⚠️  À VÉRIFIER")
    else:
        print(f"{msg["texte"]}: --> ✅ AUTORISE, transmis au LLM")
print(f"Nous avons bloqué {nb_bloques} messages suspicieux")