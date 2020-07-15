# Rapport sold-out
Bot pour solebox.com, il permet de créer un compte, s'y login et d'ajouter un article dans son panier

## Utilisation du bot 
1. Changer les informations de connexion (user) dans l'en-tête du code
2. Executer le code
3. Vérifiez que notre compte a bien été crée et que l'article a bien été rajouté au panier

## Démarche
### Nombre d’heures 
Entre 1 et 2h par jour après ma journée de stage, j’ai pris en tout 15h environ de la recherche jusqu’à la réalisation du rapport.

### Recherche et analyse : 
J’ai au départ analysé le code de requet.py et example.py puis tester le code d’exemple. J’ai ensuite fait des recherches internet sur l’analyse de tram/paquets et regardé plusieurs vidéos youtube qui explique comment faire un sneakerbot en python (générer des URLs, web Scraping, automatisation etc..), cela m’a permis de comprendre en utilisant la librairie request (pas requet).

### Requêtes :
Pour capturer les requêtes j’ai au départ utilisé l’analyseur réseau intégré à Firefox pour visualiser les requêtes http/https. Après avoir envoyé un mail au dev de sol-out, j’ai fini par utiliser BurpSuite parce que l’interface était plus intuitive que mitmproxy et firefox.
Je me suis ensuite manuellement connecté au site solebox, puis j’ai créé un compte/login et j’ai ajouté un article dans mon panier en activant l’intercepteur de burpsuite. J’ai ensuite ajouté les url des requêtes https les plus importantes dans le repeater et j’ai analysé le code, le header, les paramètres et fait des tests.

### Réalisation du script : 
J’avais au départ 8 requêtes et des erreurs dans mon code (erreurs code 302, 403 Forbidden etc). Je me suis ensuite rendu compte en analysant la requête post qui permettait de créer le compte que je ne récupérais pas un crsf token, j’ai donc passé pas mal de temps à trouver un moyen de le récupérer, j’ai essayé plusieurs fonctions python comme split(), find() et « BeautifulSoup » après plusieurs recherches sur internet mais aucune n’a vraiment fonctionné parce que je devais retirer le ‘=’ du token. J’ai trouvé le module re qui fournit des expressions régulières, ayant déjà utilisé des expressions régulières en cours, j’ai utilisé l’opération search() qui permet de rechercher une correspondance dans un code et de supprimer le caractère que je voulais.

Je n’ai pas eu de soucis particuliers avec les headers des requêtes mais j’ai passé du temps à optimiser le temps et le nombre de requêtes et j’ai fini avec 4 requêtes.
J’avais au départ séparé la création et le login/ajout de chaussure dans 2 fichiers différents mais j’avais beaucoup trop de requêtes qui se répétait (notamment connexion au compte et à la page login), j’ai donc mis tout dans un seul fichier et sachant que solebox, lorsque l’on crée un compte, nous login directement, je n’avais pas besoin de passer par cette étape et il fallait simplement créer un compte, chercher le produit et l’ajouter.

J’ai rajouté des « time.sleep » à la fin pour "simuler" un utilisateur normal et éviter que le site me soupçonne d’être un bot (grâce à un tuto sneakerbot) 

#### Ordre d’exécution des requêtes au début du projet: 
- ~~Requête GET : Connexion au site solebox (Supprimé car non nécessaire)~~
- ~~Requête GET : Connexion à la page login (Non nécessaire quand on met tout dans 1 seul fichier)~~
- Requête GET : Demande de la page d’inscription (Récupération du csrf token)
- Requête POST : Envoi d’une demande d’inscription avec les informations de l’utilisateur (Vérification du résultat via la réponse du serveur)
- Requête GET : Recherche de l’article (Récupération du PID de l’article)
- Requête POST : Ajout de l’article au panier

On garde donc ces 4 requêtes.

### Optimisation possible et bonus : 

-Pour choisir une paire de chaussures, il faut ajouter manuellement et copier la requête https (le PID du produit). On pourrait tenter de trouver automatiquement le PID d’une chaussure avec le lien à l’aide d’une fonction.

-J’ai regardé un peu le site Snipes et le site a la même structure que Solebox (sûrement parce qu’ils ont le même hébergeur demandware),il y a pratiquement les mêmes requêtes à utiliser, j’aurais pu coder un script pour le site mais je manque de temps malheureusement.



