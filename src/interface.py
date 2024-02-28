from src.jeu import *

class Interface:
    """
    Interface du jeu de puissance 4 (affichage des menus, des résultats, etc.)
    """

    SEPARATION = '\n' + '—' * 60

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

        LONGUEUR_CONTENU_MENU = 39
        LIGNE_HAUT_BAS = '+' + '—' * LONGUEUR_CONTENU_MENU + '+'
        LIGNE_SEPARATION = "|" + '—' * LONGUEUR_CONTENU_MENU + "|"
        LIGNE_VIDE = "|" + ' ' * LONGUEUR_CONTENU_MENU + "|"

        print(LIGNE_HAUT_BAS)
        print("|" + ' ' * 13 + "MENU PRINCIPAL" + ' ' * 12 + "|")
        print(LIGNE_SEPARATION)
        print(LIGNE_VIDE)
        print("|  Entrez 'J' pour jouer contre une IA  |")
        print("|  Entrez 'Q' pour quitter le jeu       |")
        print(LIGNE_VIDE)
        print(LIGNE_HAUT_BAS + '\n')

        Interface.gererActionJoueur()

    def gererActionJoueur():
        """
        Attends et gère l'action du joueur sur la console texte
        """

        CMD_JOUER = 'j'
        CMD_IA = 'a'
        CMD_QUITTER = 'q'

        TXT_COMMANDE = "Commande : "
        COMMANDE_INVALIDE = "\nLa commande entrée est invalide, souhaitez-vous jouer ?\n   Si oui, entrez 'J'\n   Sinon, entrez 'Q' pour quitter\n"

        commande = input(TXT_COMMANDE)
        commande = commande.lower().strip()

        if commande == CMD_QUITTER:
            Interface.quitterJeu()
        elif commande == CMD_IA:
            Interface.demarrerJeuIA()
        elif commande == CMD_JOUER:
            Interface.demarrerJeu()
        else:
            print(COMMANDE_INVALIDE)
            Interface.gererActionJoueur()


    def demarrerJeu():
        """
        Démarre le jeu
        """

        pseudo = Interface.choisirPseudo()
        jeton = Interface.choisirJeton()
        print(Interface.SEPARATION + "\n")

        jeuEnCours = Jeu(pseudo, jeton)

        Interface.gererPartieCourante(jeuEnCours)

    def demarrerJeuIA():
        """
        Démarre le jeu en version IA
        """
        
        jeuEnCours = Jeu(None, None)
        jeuEnCours.configurerPartieIA()
        
        Interface.gererPartieCourante(jeuEnCours)

    def gererPartieCourante(jeuEnCours: Jeu):
        """
        Gère la partie en cours : les tours des joueurs, la fin de partie, etc.
        """

        partieTerminee = False

        print(jeuEnCours.getGrille())

        while not partieTerminee:
            jeuEnCours.gererTourJoueur()
            print(jeuEnCours.getGrille())

            partieTerminee = jeuEnCours.verifierFinPartie()

            if not partieTerminee:
                jeuEnCours.inverserJoueurJouant()

        Interface.afficherMenuPrincipal()
                
    def choisirPseudo() :
        ERREUR_MAX = 5
        nombreErreur = 0

        print(Interface.SEPARATION)

        for i in range (ERREUR_MAX) : 
            pseudo = input("\nEntrez un pseudonyme : ")
            if (len(pseudo) > 1 and not all(caractere.isspace() for caractere in pseudo)):
                return pseudo.strip()
            elif nombreErreur <= ERREUR_MAX :
                nombreErreur += 1
            else :
                return "Joueur 1"
            
    def choisirJeton() :
        """
        Demande au joueur de choisir un jeton
        """

        ERREUR_MAX = 5
        nombreErreur  = 0

        print(Interface.SEPARATION)

        for i in range (ERREUR_MAX):
            jeton = input("\nPréférez-vous jouer avec des jetons ronds ou des croix ?\n  - Entrez 'o' pour rond,\n  - Entrez 'x' pour croix\n\nJeton : ")
            if (jeton.lower() == 'o' or jeton.lower() == "x" ) :
                return jeton.lower()
            elif nombreErreur <= ERREUR_MAX :
                nombreErreur += 1
                print("\nLe jeton entré est invalide.")
                print(Interface.SEPARATION)
            else :
                return "x"

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