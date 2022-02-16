# OC_V2_P10
## Développement d'une API Rest Django "Softdesk"

# Description du projet :

L'API REST développée en Django propose de gérer des tickets ou problèmes associés à projet/application/produit

Pour ce faire, plusieurs endpoints ont été définis :

   * La création d'un utilisateur ;
   * L'authentification d'un utilisateur ;

    Puis l'accès des endpoints suivants est sécurisé : 
   * L'accès aux projets de l'utilisateur authentifié ;
   * La création ou modification de projet/application/produit ;
   * La suppression d'un projet/application/produit ;
   * La création, la modification ou suppression d'un problème
    à un projet/application/produit;
   * La consultation des problèmes d'un projet/application/produit ;
   * La consultation détaillée d'un problème
   * La création, la modification ou suppression d'un commentaire 
    à un problème d'un projet/application/produit;
   * La consultation de commentaires d'un problème d'un projet/application/produit. 
   * La consultation d'un commentaire

# Installation :

Dans votre répertoire de travail, créer un répertoire d'installation nommé "OC_V2_P10" et placez - vous sous ce répertoire de travail

   * Pour Linux : $ cd /home/user/OC_V2_P10
   * Pour Windows : cd C:/Users/user/OC_V2_P10 Puis entrer : git clone https://github.com/Lazuli22/OC_V2_P10.git

# Pré-requis :

Utilisation du fichier requirements.txt en vue de créer l'environnement des librairies du projet

   * Se placer dans le répertoire d'installation du projet
        Pour Linux : $ cd /home/user/OC_V2_P10
        Pour Windows : cd C:/Users/user/OC_V2_P10
   * pour le créer, lancer la commande : python -m venv env
   * Pour l'activer, lancer la commande :
        Pour Linux : env/bin/activate
        Pour Windows : .\env\Script\activate.bat
   * Pour l'alimenter, lancer la commande : pip install -r requirements.txt

# Lancement du projet :

1 - Lancer le serveur : python .\manage.py runserver.  
2 - Ouvrir un outil de type POSTMAN pour y définir des appels à requête.

# Autrice

* Dolores DIAZ alias Lazuli22


