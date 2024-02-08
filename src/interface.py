class Interface:
    """
    Interface du jeu de puissance 4 (affichage des menus, des résultats, etc.)
    """

    def afficherMessageBienvenue():
        """
        Affiche un message de bienvenue
        """

        MESSAGE_BIENVENUE = "Bienvenue sur ce jeu de puissance 4 !\n"

        print(MESSAGE_BIENVENUE)

    def afficherMenuPrincipal():
        """
        Affiche le menu principal : propose de jouer ou de quitter le jeu
        """

        MENU_PRINCIPAL = '—' * 30 + "\n\tMENU PRINCIPAL\n" + '—' * 30 + "\n\nEntrez 'J' pour jouer\nEntrez 'Q' pour quitter le jeu\n"

        print(MENU_PRINCIPAL)

        Interface.gererActionJoueur()

    def gererActionJoueur():
        """
        Attends et gère l'action du joueur sur la console texte
        """

        CMD_JOUER = 'j'
        CMD_QUITTER = 'q'

        TXT_COMMANDE = "Commande : "
        COMMANDE_INVALIDE = "\nLa commande entrée est invalide, souhaitez-vous jouer ?\n   Si oui, entrez 'J'\n   Sinon, entrez 'Q' pour quitter\n"

        commande = input(TXT_COMMANDE)
        commande = commande.lower().strip()

        if commande == CMD_QUITTER:
            Interface.quitterJeu()
        elif commande == CMD_JOUER:
            Interface.demarrerJeu()
        else:
            print(COMMANDE_INVALIDE)
            Interface.gererActionJoueur()


    def demarrerJeu():
        """
        Démarre le jeu
        """

        print("Démarrer jeu")

    def afficherResultat():
        """
        Affiche le résultat
        """

        print("Afficher résultat")

    def quitterJeu():
        """
        Quitte le jeu
        """
        
        MESSAGE_QUITTER = "\nMerci d'avoir joué !"

        print(MESSAGE_QUITTER)
        exit(0)