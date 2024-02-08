
from abc import ABCMeta, abstractmethod
class Joueur(metaclass=ABCMeta):
    global formatJeton
    global nom
    
    @abstractmethod
    def __init__(self,nom,formatJeton,IA):
        self.formatJeton = formatJeton
        self.nom = nom
        self.IA = IA
        
    @abstractmethod
    def playJeton(self):
        pass

    
    def getNom(self):
        return self.nom

    def getFormatJeton(self):
        return self.formatJeton