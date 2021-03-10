# SpiderScienceDirect
Web scraping du site sciencedirect
L'objectif de ce module est de recuperer des articles du site scienceDirect 
La configuration se passe dans le fichier setting du dossier spider
Pour demarrer le robot il faut lancer la commande 
scrapy crawl  articleScienceDirect ### articleScienceDirect represente le nom du spider
scrapy crawl  articleScienceDirect  -o fic1.json  ### pour rediriger le resultat dans le fichier fic1.json
