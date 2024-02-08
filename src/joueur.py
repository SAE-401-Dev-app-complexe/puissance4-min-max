from Jeton import Jeton
from abc import ABCMeta, abstractmethod

class Joueur(metaclass=ABCMeta):
    """
    Classe abstraite représentant un joueur de puissance4
    """

    formatJeton
    nom
    estIA
    
    @abstractmethod
    def __init__(self, nom, formatJeton, IA):
        """
        Initialise un joueur avec un nom, un format de jeton et un booléen indiquant si le joueur est une IA
        """

        self.nom = nom
        self.formatJeton = formatJeton
        self.estIA = IA
    
        
    @abstractmethod
    def jouerJeton(self)->Jeton:
        """
        Permet au joueur de jouer son jeton dans la colonne de son choix
        """
        pass

    
    def getNom(self):
        return self.nom

    def getFormatJeton(self):
        return self.formatJeton

    def estIA(self):
        return self.estIA