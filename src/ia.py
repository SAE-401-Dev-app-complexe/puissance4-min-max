from src.joueur import *
class IA(Joueur):

    
    grille = [  [3 , 4 , 5 , 7 , 5 , 4 , 3 ] , 
                [4 , 6 , 8 , 10 , 8 , 6 , 4] ,
                [5 , 8 , 11 , 13 , 11 , 8 , 5] ,
                [5 , 8 , 11 , 13 , 11 , 8 , 5], 
                [4 , 6 , 8 , 10 , 8 , 6 , 4] ,
                [3 , 4 , 5 , 7 , 5 , 4 , 3]
             ]
    def __init__(self, nom, formatJeton  , grille):
        super().__init__(nom, formatJeton, True)
        self.grille = grille


    def jouerJeton(self, colonne):
        pass
      
    def trouverCoupPerdant(self):
        """
        Trouve un coup perdant
        """
        
        # TODO
        pass

    def trouverCoupGagnant(self):
        """
        Trouve un coup gagnant
        """
        
        # TODO
        pass