<h1>ACC Leaderboard</h1>
<p>Projet servant à enregistrer les temps des pilotes de notre serveur Assetto Corsa Competizione.<p>  
<p>Les temps des pilotes sont recupérés à chaque fin de session puis enregistrés dans une base de données sur le serveur. Les temps sont consultables grâce à un bot discord (et prochainement sur un site web ).</p>
 
<h2>Fonctionnement</h2>
 
<p> Un script bash (checkChanges.sh) surveille le dossier "results" du server et lance un script python (saveResults.py) lorsqu'un nouveau fichier est crée dans ce dossier.<p>
<p> Le script python (saveResults.py) va récupérer le dernier fichier (un fichier json) crée dans le dossier "results" du server et récupérer les informations qu'il contient (circuit, noms des pilotes, meilleurs temps au tour, modèle de voiture, s'il pleut ou non, etc...) et les enregistrer dans la base de données du serveur.<p>
<p> Les données sont ensuite consultables grâce à un bot discord en python. Le bot renvoie les 10 meilleurs temps du circuit demandé ($temps nom_du_circuit), ou le meilleur temps d'un pilote précis sur le circuit demandé($temps nom_du_circuit "prénom_pilote nom_pilote")</p>
