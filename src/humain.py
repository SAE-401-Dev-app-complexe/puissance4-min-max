from Joueur import Joueur
from Jeton import Jeton
from SaisieException import SaisieException

class Humain(Joueur):
    """
    """

    def __init__(self, nom, formatJeton):
        super().__init__(nom, formatJeton, False)

    def jouerJeton(self)->Jeton:
        """
        Demande un entier sur la console correspondant à la colonne dans laquel il veut jouer
        Si l'entrée est un entier, renvoie un Jeton
        Sinon renvoie une SaisieNonEntiereError
        """

        saisie = input("Choissisez une colonne ou placer votre jeton")
        if (not isinstance(saisie, int)):
            raise SaisieException("Vous devez entrez un numéro de colonne compris entre 1 et 7")

        return Jeton(self.formatJeton, saisie - 1)

""" Test
JoueurA = Humain("Jean","X")
JoueurA.jouerJeton()
JoueurA.getNom()
"""