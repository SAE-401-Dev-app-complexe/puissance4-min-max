from src.grille import *
from src.humain import *
from src.ia import *
from src.saisie_exception import SaisieException

class Jeu:
    SEPARATION = '\n' + '—' * 60

    def __init__(self , nom, jeton):
        self.grille  = Grille()
        self.joueur1 = Humain(nom, jeton)
        self.joueur2 = IA("IA", "o" if jeton == "x" else "x", self.grille)
        self.joueurJouant = self.joueur1

    def configurerPartieIA(self):
        self.joueur1 = IA("IA" , "x" , self.grille)
        self.joueur2 = IA("IA2" , "o" if jeton == "x" else "x" , self.grille)

    def getJoueur1(self):
        return self.joueur1
      
    def getJoueur2(self):
        return self.joueur2

    def getTourJoueur1(self):
        return self.tourJoueur1

    def getGrille(self):
        return self.grille

    def lancerPartie(self, interface):
        """
        Lance la partie du puissance 4
        La partie n'est pas termine tant que la partie n'est pas nulle ou qu'un joueur à gagné
        """
        partieNonTermine = True
        
        print(self.grille)

        while (partieNonTermine):
            self.tourJoueur(self.joueurJouant)
            
            print()
            print(self.grille)
            
            # Verification Victoire
            # print("colonne " + str(self.grille.derniereColonneJoue) + "\nligne " + str(self.grille.derniereLigneJoue))
            victoire = self.grille.alignementHorizontal(self.grille.derniereLigneJoue)
            victoire |= self.grille.alignementVertical(self.grille.derniereColonneJoue)
            victoire |= self.grille.alignementDiagonal()

            # Affichage Victoire
            if (victoire):
                partieNonTermine = False
                print("Le joueur " + str(self.joueurJouant.getNom())+ " a gagné.\n" + self.SEPARATION + "\n")
                interface.afficherMenuPrincipal()
            elif self.grille.grillePleine():
                partieNonTermine = False
                print("Partie terminée.\nAucun joueur n'a gagné.\n")
                interface.afficherMenuPrincipal()
            else :
                self.joueurJouant = self.prochainJoueurJouant()
    
    def prochainJoueurJouant(self):
        return self.joueur2 if self.joueurJouant == self.joueur1 else self.joueur1

    def tourJoueur(self, joueur:Joueur):
        tourNonReussi = True
        erreurSaisies = False

        while (tourNonReussi):
            if (not erreurSaisies and not joueur.IA):
                print("C'est au tour de " + str(joueur.getNom())+ " de jouer un jeton.\n")
                print("Votre jeton est " + str(joueur.getFormatJeton()))
            elif (joueur.IA):
                print("C'est au tour de " + str(joueur.getNom())+ " de jouer un jeton.\n" + self.SEPARATION + "\n")

            try:
                coupGagnant = self.grille.setCellule(joueur.jouerJeton(), joueur.getFormatJeton()) 
                tourNonReussi = False
                erreurSaisies = False
            except SaisieException as e:
                erreurSaisies = True
                print(e.message)

        return coupGagnant