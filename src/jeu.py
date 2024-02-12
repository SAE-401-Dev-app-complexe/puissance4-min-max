from src.grille import*
from src.humain import*
from src.ia import*

class Jeu:
    # TODO
    def __init__(self , nom , jetons):
        self.grille = Grille()
        self.joueur1 = Humain(nom , jetons)
        self.joueur2 = IA("Ia" , "x" if jetons == "o" else "o" , self.grille)
        self.tourJoueur1 = True

    def getJoueur1(self):
        return self.joueur1
      
    def getJoueur2(self):
        return self.joueur2

    def getTourJoueur1(self):
        return self.tourJoueur1

    def getGrille(self):
        return self.grille

    def inverserTourJoueur(self):
        """
        Inverse le tour du joueur
        """
        
        self.tourJoueur1 = not self.tourJoueur1

    def jouer(self, indiceColonne):
        """
        Joue un coup
        """
        print(indiceColonne)
        self.getGrille().setCellule(indiceColonne , self.getJoueur1().getFormatJeton())


    