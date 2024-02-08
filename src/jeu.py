from grille import*
from humain import*
from ia import*

class Jeu:
    # TODO
    def __init__(self , nom):
        self.grille = Grille()
        self.joueur1 = Humain(nom , "x")
        self.joueur2 = IA("Ia" , "o" , self.grille)

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

    