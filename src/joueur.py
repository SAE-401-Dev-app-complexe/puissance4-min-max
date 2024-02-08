from Jeton import Jeton
from abc import ABCMeta, abstractmethod
# Classe Abstraite représentant un joueur de puissance4
class Joueur(metaclass=ABCMeta):
    global formatJeton
    global nom
    

    @abstractmethod
    def __init__(self,nom,formatJeton,IA):
        """
        
        """
        self.formatJeton = formatJeton
        self.nom = nom
        self.IA = IA
        
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
