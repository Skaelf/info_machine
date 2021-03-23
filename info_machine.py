#!/usr/bin/python
# coding: utf-8

import psutil       # Module permettant de récupérer les informations sur les composants de la machine ;
import os           # Module permettant d'exécuter une commande ;
import platform     # Module permettant de récupérer des informations sur la plateforme du système ;
import sys          # Module permettant de copier les résultats du script dans un fichier au format ".txt" ;


# La fonction "info_dns()" effectue trois ping vers le nom d'hôte "google.com" puis indique si le site est joignable ou non ;

def info_dns():
    print()
    print("1. COMMUNICATION VERS LE SITE WEB 'GOOGLE' ")
    print()

    hostname = "google.com"
    response = os.system("ping -c 3 " + hostname)

    print()

    if response == 0:
        print(hostname, 'connexion établie !')
    else:
        print(hostname, 'impossible à joindre !')

    print()

    return("")


# La fonction "info_cpu()" permet de récupérer des informations sur le fonctionnement du processeur ;

def info_cpu():
    print()
    print("2. INFORMATIONS CPU : ")
    print()

    print("- Nombre de Coeurs Physique/Logique Présent : ")
    print(psutil.cpu_count())
    print()

    print("- Pourcentage de l'utilisation du CPU : ")
    print(psutil.cpu_percent(interval=0.1))
    print()

    print("- Fréquence des CPU :")
    print(psutil.cpu_freq())
    print()

    print("- Charge système il y a 1, 5 et 15 minutes :")
    print(psutil.getloadavg())
    print()

    return("")


# La fonction "info_ram_swap()" permet de récupérer des informations sur le fonctionnement de la mémoire RAM et Swap ;

def info_ram_swap():
    print()
    print("3. INFORMATIONS MÉMOIRE RAM ET SWAP : ")
    print()

    print("- Mémoire RAM : ")
    print(psutil.virtual_memory())

    print()

    print("- Pourcentage mémoire RAM utilisée :")
    print(psutil.virtual_memory().percent)

    print()

    print("- Pourcentage mémoire RAM disponible :")
    print(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total)

    print()

    print("- Mémoire SWAP : ")
    print(psutil.swap_memory())

    print()

    print("- Pourcentage mémoire SWAP utilisée : ")
    print(psutil.swap_memory().percent)

    print()

    print("- Pourcentage mémoire SWAP disponible :")
    print(psutil.swap_memory().free * 100 / psutil.swap_memory().total)

    return("")


# La fonction "info_disques()" permet de lister les partitions et indique l'usage du disque dur à la racine ;

def info_disques():
    print()
    print("4. INFORMATIONS DISQUES DURS : ")
    print()

    print("- Partitions présentes sur la machine : ")
    print(psutil.disk_partitions())

    print()

    print("- Usage disque dur à la racine : ")
    print(psutil.disk_usage('/'))

    print()

    print("- Pourcentage mémoire disque dur utilisé (/) : ")
    print(psutil.disk_usage('/').percent)

    print()

    print("- Pourcentage mémoire disque dur disponible (/) : ")
    print(psutil.disk_usage('/').free * 100 / psutil.disk_usage('/').total)

    return("")


# La fonction "info_utilisateurs()" indique les utilisateurs qui sont connectés à la machine ;

def info_utilisateurs():
    print()
    print("5. INFORMATIONS UTILISATEURS : ")
    print()

    print("- Utilisateurs connectés au système :")
    print(psutil.users())

    return("")


# La fonction "info_processus()" liste les processus en cours sur la machine en indiquant le nom du processus, l'utilisateur qui l'exécute et son PID ;

def info_processus():
    print()
    print("6. INFORMATIONS PROCESSUS : ")
    print()

    print("- Liste des processus en cours sur le système :")
    print()
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        try:
            print(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return("")


# La fonction "info_reseaux" affiche l'adresse IP et l'adresse MAC des cartes réseaux présentes sur la machine et permet également de vérifier le statut des ...
# ... cartes réseaux "up" ou "down" ;

def info_reseaux():
    print()
    print("7. INFORMATIONS RÉSEAUX : ")
    print()

    print("- Adressage machine : ")
    print(psutil.net_if_addrs())

    print()

    print("- Informations cartes réseaux : ")
    print(psutil.net_if_stats())

    return("")

# La fonction "info_diverses()" donne des informations sur la plate-forme de la machine, sur le temps de démarrage du système, et sur la batterie ;

def info_diverses():
    print()
    print("8. INFORMATIONS DIVERSES : ")
    print()

    print("- Architecture : ", platform.architecture())
    print("- Type Machine : ", platform.machine())
    print("- Nom d'hôte : ", platform.node())
    print("- Informations plateforme : ", platform.platform())
    print("- Système d'exploitation : ", platform.system())
    print("- Temps nécessaire au démarrage du système : ", psutil.boot_time())

    def secs2hours(secs):
        mm, ss = divmod(secs, 60)
        hh, mm = divmod(mm, 60)
        return "%d:%02d:%02d" % (hh, mm, ss)

    battery = psutil.sensors_battery()
    print("- Pourcentage batterie restante = %s%%" % (battery.percent))
    print("- Temps restant = %s" % (secs2hours(battery.secsleft)))

    return("")

  
# La variable "choix_utilisateur" demande à l'utilisateur de saisir un nombre situé entre 1 et 9 pour afficher les informations souhaitées :

# La boucle "while" permet à l'utilisateur de récupérer des informations sur ce qu'il souhaite succesivement ;

choix_utilisateur = True
while choix_utilisateur:

    print("""
            1.Test DNS, communication vers site web
            2.Informations CPU
            3.Informations RAM
            4.Informations Disque Dur
            5.Informations Utilisateurs
            6.Liste Processus
            7.Informations Réseaux
            8.Informations Diverses
            9.Quitter le programme et sauvegarder les informations dans un fichier
                """)

    choix_utilisateur = input("Veuillez choisir les informations à récupérer : ")

# Exécute la fonction "info_dns()" ;

    if choix_utilisateur == "1":

        print(info_dns())

# Exécute la fonction "info_cpu()" ;

    elif choix_utilisateur == "2":

        print(info_cpu())

# Exécute la fonction "info_ram_swap()" ;

    elif choix_utilisateur == "3":

        print(info_ram_swap())

# Exécute la fonction "info_disques()" ;

    elif choix_utilisateur == "4":

        print(info_disques())

# Exécute la fonction "info_utilisateurs()" ;

    elif choix_utilisateur == "5":

        print(info_utilisateurs())

# Exécute la fonction "info_processus()" ;

    elif choix_utilisateur == "6":

        print(info_processus())

# Exécute la fonction "info_reseaux()" ;

    elif choix_utilisateur == "7":

        print(info_reseaux())

# Exécute la fonction "info_diverses()" ;

    elif choix_utilisateur == "8":

        print(info_diverses())

# Permet de terminer le script ;

    elif choix_utilisateur == "9":

        print()

        print("L'ensemble des informations seront copiés dans le fichier 'resultats_script.txt'. ")
        print()
        print("EXCTINCTION DU PROGRAMME !")
        choix_utilisateur = None

# Indique à l'utilisateur qu'il doit saisir un nombre situé entre 1 et 9 puis relance la boucle ;

    else:
        print()

        print("ERREUR : Veuillez choisir un nombre entre 1 ET 9 ! ")
        print()

        choix_utilisateur = input("Veuillez choisir les informations à récupérer : ")

# Lorsque l'utilisateur quitte le programme ("8"), le résultat de toutes les fonctions est copié dans un fichier nommé "resultats_script.txt". Si le fichier existe, ...
# ... alors les données sont écrasées sinon le fichier est automatiquement créé ;

sys.stdout = open("resultat_script.txt", "w")

(info_dns())
(info_cpu())
(info_ram_swap())
(info_disques())
(info_utilisateurs())
(info_processus())
(info_reseaux())
(info_diverses())

sys.stdout.close()
