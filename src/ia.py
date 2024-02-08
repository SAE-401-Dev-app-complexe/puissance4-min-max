class IA(Joueur):

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