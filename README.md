# info_machine

## 1. Sommaire :

-	Objectif du script
-	Pré-requis
-	Fonctionnement du script
-	Améliorations possibles


## 2.	Objectif du script :

Ce script permet de récupérer de nombreuses informations sur une machine de manière interactive et permet également de sauvegarder automatiquement l’ensemble de ces informations dans un fichier au format « .txt » une fois que l’extinction du script. Voici la liste des informations que permet de récupérer le script :

-	Test DNS ;
-	Informations sur le CPU ;
-	Informations sur la mémoire RAM ;
-	Informations sur la mémoire SWAP ;
-	Informations sur le disque dur ;
-	Informations sur les utilisateurs ;
-	Informations sur les processus ;
-	Informations réseaux ;
-	Informations sur la plate-forme de la machine ;

L’intérêt du script est qu’il permet de récupérer un grand nombre d’informations de manière rapide et automatique sur une machine. Le script permet également de s’assurer du bon fonctionnement d’une machine, dans plusieurs cas de figures :

Par exemple, un puissant logiciel vient d’être installé sur la machine, on pourrait vérifier que la mémoire RAM n’est pas trop sollicitée, que le processeur n’est pas surchargé ou encore noter la différence sur la charge système lorsque le logiciel est actif et lorsqu’il éteint.

Dans un autre cas de figure, on pourrait également lancer le script de manière régulière par exemple 1fois par mois pour s’assurer du bon fonctionnement de la machine.
Ce script peut être utile dans de nombreux cas, et permet un gain de temps considérable pour récupérer des informations sur une machine.


## 3.	Pré-requis :

Pour que le script soit fonctionnel, il est nécessaire d’effectuer plusieurs actions :

-	Script applicable sur « Linux » ;
-	Installation de python3 ;
-	Vérifier que les modules suivants : « psutil », « os », « platform » et « sys » sont bien installés sur la machine ;


## 4.	Fonctionnement du script :

Le script fonctionne de manière interactive, cela signifie qu’à l’exécution du script, un menu apparaîtra dans le terminal et proposera à l’utilisateur de récupérer les informations qu’il souhaite. 
Par exemple si l’utilisateur saisit le nombre « 2 », le script affichera les informations relatives au CPU puis une fois les informations affichées, le menu apparaîtra à nouveau pour permettre à l’utilisateur de récupérer les informations qu’il souhaite.

Le fait d’avoir un script interactif et de proposer un menu, permet de laisser le choix à l’utilisateur concernant les informations qu’il souhaite récupérer. 
De plus, même si l’utilisateur décide d’afficher uniquement les informations relatives au processeur et au disque dur par exemple, le script une fois éteint sauvegardera l’ensemble des informations dans un fichier au format « .txt » nommé « resultats_script.txt ». 
Cela permettra à l’utilisateur de pouvoir lire toutes les informations de la machine ultérieurement. 

Dans le cas où l’utilisateur saisit autre chose qu’un nombre situé entre 1 et 9, le script affichera un message d’erreur en indiquant à l’utilisateur de saisir un nombre entre 1 et 9. Puis une fois qu’un nombre correct aura était saisi, le menu s’affichera à nouveau et l’utilisateur pourra récupérer les informations souhaitées. 
Pour mettre fin au script, il suffit à l’utilisateur de taper le nombre « 8 » et le script effectuera une sauvegarde comme je le disais des informations de la machine avant de se fermer. 


## 5.	Améliorations possibles :

Un autre avantage de ce script c’est qu’il a était conçu de manière à pouvoir évoluer et peut être exécuté sur plusieurs machines différentes sans avoir à changé quoi que ce soit au niveau du code. Comme vous l’imaginais les possibilités d’évolution sont nombreuses concernant la récupération d’informations d’une machine.
Voici quelques idées de ma part :

-	Modifier le script pour qu’il s’exécute sur de nombreuses machines et qu’il sauvegarde les informations de chaque machine dans des fichiers distincts. Par exemple info_poste1.txt, info_poste2.txt, info_poste3.txt, …

-	Si l’utilisateur ou si une entreprise dispose d’un site web, alors tenter de récupérer des informations pour s’assurer du bon fonctionnement du site web et récupérer les informations principales.

-	Etc… 

