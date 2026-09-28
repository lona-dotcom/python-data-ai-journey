historique = [
    {"role": "user", "nb_tokens": 120},
    {"role": "assistant", "nb_tokens": 50},
    {"role": "assistant", "nb_tokens": 110},
    {"role": "assistant", "nb_tokens": 90},
    {"role": "user", "nb_tokens": 80}
]
cout_total = 0.0
for message in historique:
    if message["role"] == "assistant":
        cout_total += message["nb_tokens"] * 0.00001
        print(f"Message {message["role"]}: +{message["nb_tokens"]} -> total actuel : {cout_total}")
    else:
        print()
print(f"Coût total des messages de l'assistant : {cout_total}")