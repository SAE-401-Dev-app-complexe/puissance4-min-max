from src.joueur import *
from src.saisie_exception import SaisieException

class Humain(Joueur):
    """
    """

    def __init__(self, nom, formatJeton):
        super().__init__(nom, formatJeton, False)

    def jouerJeton(self):
        """
        Demande un entier sur la console correspondant à la colonne dans laquel il veut jouer
        Si l'entrée est un entier, il est renvoyé
        Sinon renvoie une SaisieNonEntiereError
        """
        try :
            saisie = int(input("Choissisez une colonne où placer votre jeton : "))
        except ValueError :
            raise SaisieException("Vous devez entrez un numéro de colonne compris entre 1 et 7")

        return (saisie - 1, self.formatJeton)

""" Test
JoueurA = Humain("Jean","X")
JoueurA.jouerJeton()
JoueurA.getNom()
"""