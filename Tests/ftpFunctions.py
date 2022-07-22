#!/usr/bin/python3
import sys
import ftplib
import datetime


def checkFtp(ip):
    with ftplib.FTP(str(ip)) as bFtp:  # Déclarer la connexion en tant que "bFtp" avec le paramètre donner au debut
        print(bFtp.getwelcome() + "- Vous êtes connecté(e)")
        try:
            bFtp.login()  # Initialiser la connexion avec bFtp.login('user', 'mdp'), si vide alors utilisateur anonyme
            bFiles = []  # Initialiser tableau vide
            bFtp.dir(bFiles.append)  # Ajouter dans le tableau bFiles la liste des fichiers
            for b in bFiles:  # Pour chaque élément b dans le tableau bFiles faire:
                print(b)
            print(bFtp.pwd())  # Avoir le chemin courant
            ts = datetime.datetime.now().timestamp()  # Avoir le timestamp (unique) de maintenant
            bFtp.mkd(str(ts))  # Création d'un dossier qui a pour nom le timestamp
            bFtp.cwd(str(ts))  # Changement de dossier au dernier dossier créé
            print(bFtp.pwd())
        except ftplib.all_errors as bError:  # Récupérer les erreurs dans bError
            print('FTP error:', bError)
