
# Installation de dépendences

Pour tracer des graphes, vous allez avoir besoin d'installer `matplotlib` :

    pip install matplotlib

# Données

Nous vous fournissons 100 000 agents, gracieusement créés grâce à [PPLAPI](http://pplapi.com). 
*Pensez à dézipper le document !*

    unzip agents-100k.zip

Si vous souhaitez en générer de nouveaux, entrez la commande suivante :

    ./download_agents -d agents-100k.json -c 100000

# Lancer le programme

    ./model.py agents-100k.json
