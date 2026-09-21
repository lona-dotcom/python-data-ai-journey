a="24" # a: str
b=24    # b: int
c=24.0 # c: int
d=True # d: bool
e=3.14 # e: float

print(a, "->", type(a))
print(b, "->", type(b))
print(c, "->", type(c))
print(d, "->", type(d))
print(e, "->", type(e))

nom_ai="freellmapi"
nombre_requete=50
temps_reponse=0.8
requete_ok=True

print(nom_ai, "->", type(nom_ai))
print(nombre_requete, "->", type(nombre_requete))
print(temps_reponse, "->", type(temps_reponse))
print(requete_ok, "->", type(requete_ok))

valeur=100
print(type(valeur))
valeur="cent"
print(type(valeur)) #Après la nouvelle assignation, le type de la variable change en str alors qu'avant c'est int

texte_question="Quelle est la météo aujourd'hui?"
code_http=200
temperature_modele=0.7
reponse_recue=True
print(texte_question, code_http, temperature_modele, reponse_recue)
print(type(texte_question))
print(type(code_http))
print(type(temperature_modele))
print(type(reponse_recue))


nombre_utilisateurs = "50" #type: str
nombre_admins = 5 #type: int
total = nombre_utilisateurs + nombre_admins # total: addition str+int, c'est ici le bug
print("Total :", total)
# la variable total est de type int. La solution c'est de convertir la variable nombre_utilisateur en int pour pouvoir l'additionner avec nombre_admins
nombre_utilisateurs=50
nombre_admins=5
total=nombre_utilisateurs+nombre_admins
print("Total:", total)

