solde = 50
semaine = 1
while solde >= 15:
    print(f"Semaine {semaine}: Solde actuel est de {solde}€")
    solde -= 15
    semaine += 1
print(f"Retrait terminé, solde finale est de {solde}€")