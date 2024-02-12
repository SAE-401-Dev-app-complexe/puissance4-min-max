from src.jeu import *

class Interface:

    SEPARATION = '\n' + '—' * 60

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

        pseudo = Interface.choisirPseudo()
        jeton = Interface.choisirJeton()
        jeuEnCours = Jeu(pseudo, jeton)
        jeuEnCours.lancerPartie()

    def boucleDeJeu(jeuEnCours):
        print(jeuEnCours.getGrille())
        gagne = False
        while(not gagne) : 
            if(jeuEnCours.getTourJoueur1()) :
                choix = Interface.choixColonne(jeuEnCours)
    

    def choixColonne(jeuEnCours):
        positionValide = False
        CHOIX_MIN = 1
        CHOIX_MAX = 7
        while (not positionValide) :
            choix = input("Dans quelle colonne souhaitez vous jouer ? ")
            if (choix.isdigit() and int(choix) >= CHOIX_MIN and int(choix) <= CHOIX_MAX) :
                try :
                    jeuEnCours.jouer(int(choix) - 1)
                    print(jeuEnCours.getGrille())
                    positionValide = True
                except IndexError as e :
                    print(e.args[0])
                
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
        ERREUR_MAX = 5
        nombreErreur  = 0

        print(Interface.SEPARATION)

        for i in range (ERREUR_MAX):
            jeton = input("\nPréférez-vous jouer avec des jetons ronds ou des croix ?\n  - Entrez 'o' pour rond,\n  - Entrez 'x' pour croix\n\nJeton : ")
            if (jeton.lower() == 'o' or jeton.lower() == "x" ) :
                print('')
                return jeton
            elif nombreErreur <= ERREUR_MAX :
                nombreErreur += 1
                print("\nLe jeton entré est invalide.")
                print(Interface.SEPARATION)
            else :
                print('')
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