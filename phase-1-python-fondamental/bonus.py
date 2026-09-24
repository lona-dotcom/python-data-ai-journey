# nb_tokens = "1500"
# correction
nb_tokens = 1500
cout_par_token = 0.002
cout_total = nb_tokens * cout_par_token # ne va pas fonctionner car nb_tokens est une chaîne de caractères, il faut la convertir en nombre entier
print(f"Coût estimé : {cout_total} centimes")