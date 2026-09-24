# nb_message = "0"
# nb_message = nb_message + 1
# print("Nombre de messages echangés:", nb_message)

# ce code ne va pas fonctionner car nb_message est une string et on ne peut pas ajouter un int à une string. Il faut convertir nb_message en int avant de l'incrémenter.

nb_message = 0
nb_message += 1
nb_message += 1
print("Nombre de messages échangés:", nb_message)