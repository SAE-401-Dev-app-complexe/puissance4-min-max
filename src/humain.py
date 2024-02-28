from src.joueur import *
from src.saisie_exception import SaisieException

class Humain(Joueur):
    """
    """

    SEPARATION = '\n' + '—' * 60

    def __init__(self, nom, formatJeton):
        super().__init__(nom, formatJeton, False)

    def jouerJeton(self, grille):
        """
        Demande un entier sur la console correspondant à la colonne dans laquelle le joueur veut jouer.
        """

        positionValide = False
        CHOIX_MIN = 1
        CHOIX_MAX = 7

        while (not positionValide) :
            choix = input("Dans quelle colonne souhaitez vous jouer ? ")
            if (choix.isdigit() and int(choix) >= CHOIX_MIN and int(choix) <= CHOIX_MAX) :
                try:
                    grille.setCellule(int(choix) - 1, self.formatJeton)
                    positionValide = True
                except IndexError as e:
                    print(e)
                    print(self.SEPARATION + "\n")
            else :
                print("\nVeuillez entrer un numéro de colonne compris entre 1 et 7 !\n" + self.SEPARATION + "\n")

""" Test
JoueurA = Humain("Jean","X")
JoueurA.jouerJeton()
JoueurA.getNom()
"""