from src.grille import *
from src.humain import *
from src.ia import *
from src.saisie_exception import SaisieException

class Jeu:
    SEPARATION = '\n' + '—' * 60

    def __init__(self , nom, jeton):
        self.grille  = Grille()
        self.joueur1 = Humain(nom, jeton)
        self.joueur2 = IA("IA", "o" if jeton == "x" else "x", self.grille,5)
        self.joueurJouant = self.joueur1

    def configurerPartieIA(self):
        self.joueur1 = IA("IA" , "x" , self.grille)
        self.joueur2 = IA("IA2" , "o" if jeton == "x" else "x" , self.grille)

    def getJoueur1(self):
        return self.joueur1
      
    def getJoueur2(self):
        return self.joueur2

    def getJoueurJouant(self):
        return self.joueurJouant

    def getGrille(self):
        return self.grille

    def inverserJoueurJouant(self):
        """
        Inverse le joueur jouant
        """
        self.joueurJouant = self.joueur2 if self.joueurJouant == self.joueur1 else self.joueur1

    def gererTourJoueur(self):
        """
        Gère le tour d'un joueur : demande un coup, vérifie si le coup est valide, joue le coup.
        """

        joueur = self.getJoueurJouant()

        if (not joueur.IA):
            print("C'est au tour de " + joueur.getNom() + " de jouer un jeton.\n")
            print("Votre jeton est " + str(joueur.getFormatJeton()))
        elif (joueur.IA):
            print("C'est au tour de " + joueur.getNom() + " de jouer un jeton.\n" + self.SEPARATION)

        joueur.jouerJeton(self.grille)
        print()

    def verifierFinPartie(self):
        """
        Verifie si la partie est terminée
        """
        victoire = self.grille.alignementHorizontal(self.grille.derniereLigneJoue)
        victoire |= self.grille.alignementVertical(self.grille.derniereColonneJoue)
        victoire |= self.grille.alignementDiagonal()

        if (victoire):
            print("Le joueur " + str(self.joueurJouant.getNom())+ " a gagné.\n" + self.SEPARATION + "\n")
            return True
        elif self.grille.grillePleine():
            print("Partie terminée.\nAucun joueur n'a gagné.\n")
            return True
        return False