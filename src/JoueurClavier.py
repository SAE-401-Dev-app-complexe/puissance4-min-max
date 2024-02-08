from Joueur import Joueur
from Jeton import Jeton
from SaisieException import SaisieException
class JoueurClavier(Joueur):
    
    def __init__(self,nom,formatJeton):
        super().__init__(nom,formatJeton,False)
        
    def playJeton(self) ->Jeton:
        """
        Demande un entier sur la console correspondant à la colonne dans laquel il veut jouer
        Si l'entrée est un entier, renvoie un Jeton
        Sinon renvoie une SaisieNonEntiereError
        """
        saisie = input("Choissisez une colonne ou placer votre jeton")
        if(not isinstance(saisie,int)):
            raise SaisieException("Vous devez entrez un numéro de colonne")
        return Jeton(self.formatJeton,saisie-1)

""" Test
JoueurA = JoueurClavier("Jean","X")
JoueurA.playJeton()
JoueurA.getNom()
"""