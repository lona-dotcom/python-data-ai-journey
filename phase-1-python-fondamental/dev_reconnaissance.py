nom_agent = "Jarvis"
version = 1
temperature_llm = 0.7
mode_debug = False
outils_disponibles = ["recherche_web", "calculatrice"]
config = {"modele": "claude-sonnet-4-6", "max_tokens": 1000}

# nom_agent = "jarvis"
# nom: nom_agent
# valeur: "jarvis"
# type: str
# C'est le nom de l'agent, en string, permettant d'appeler l'agent

# version = 1
# nom: version
# valeur: 1
# type: int
# permet d'identifier le numero de version de l'agent

# temperature_llm = 0.7
# nom: temperature_llm
# valeur: 0.7
# type: float
# C'est pour evaluer la performance de l'agent

# mode_debug = False
# nom: mode_debug
# valeur: False
# type: boolean
# C'est comme une interrupteur permettant de passer ou d'arrêter un processus

# outils_disponibles = ["recherche_web", "calculatrice"]
# nom: outils_disponibles
# valeur: ["recherche_web", "calculatrice"]
# type: list
# Permettant de contenir l'historique de discussion


# config = {"modele": "claude-sonnet-4-6", "max_tokens": 1000}
# nom: config
# valeur: {"modele": "claude-sonnet-4-6", "max_tokens": 1000}
# type: dict
# Enregiste les informations, reponses sur la configuration d'un llm