from Joueur import Joueur
from Jeton import Jeton
from SaisieException import SaisieException
class JoueurClavier(Joueur):
    
    def __init__(self,nom,formatJeton):
        super().__init__(nom,formatJeton,False)
        
    def playJeton(self) ->Jeton:
        try :
            saisie = int(input("Choissisez une colonne ou placer votre jeton"))
        except ValueError:
            raise SaisieException("Vous devez entrez un numéro de colonne")
        jeton = Jeton(self.formatJeton,saisie-1)

        return jeton

    def getNom(self):
        return self.nom
""" Test
JoueurA = JoueurClavier("Jean","X")
JoueurA.playJeton()
JoueurA.getNom()
"""