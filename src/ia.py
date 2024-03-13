import sys
from src.joueur import *
from src.grille import Grille
import copy
import time

class IA(Joueur):
    grille = [  [3 , 4 , 5 , 7 , 5 , 4 , 3 ] , 
                [4 , 6 , 8 , 10 , 8 , 6 , 4] ,
                [5 , 8 , 11 , 13 , 11 , 8 , 5] ,
                [5 , 8 , 11 , 13 , 11 , 8 , 5], 
                [4 , 6 , 8 , 10 , 8 , 6 , 4] ,
                [3 , 4 , 5 , 7 , 5 , 4 , 3]
             ]

    def __init__(self, nom, formatJeton, grille, profondeur):
        super().__init__(nom, formatJeton, True)
        self.grille = grille
        self.profondeur = profondeur
        self.tempsJeu = 999

    def jouerJeton(self, grille):
        """
        Applique l'algo MinMax pour décider d'une colonne dans lequelle jouer
        """
        if(self.tempsJeu < 1) :
            self.profondeur += 1
        tempsDebut = time.time()
        grille.setCellule(self.minMax(self.profondeur, grille), self.formatJeton)
        self.tempsJeu = time.time() - tempsDebut
    
    def minMax(self, profondeur,grille:Grille):
        """
        Première partie de l'algo : côté Max (IA)
        A la fin de l'algo l'index du max sur les 7 colonnes est pris ce qui désignera le coup joué par l'IA
        """
        # Cette liste correspond aux différents colonnes jouer sur la grille
        listeScoreMax = []
        for i in range(Grille.COLONNE):
            # On crée une grille qui est une copie de la grille du jeu pour simuler le reste de la partie
            grilleCopie : Grille = copy.deepcopy(grille)     

            # Si la colonne est remplie on veut que l'IA ou l'adversaire ne joue pas dans cette colonne 
            # donc on donne un score bas pour que le max évite de jouer le coup           
            if (grilleCopie.colonneRemplie(i)):
                listeScoreMax.append(-10000)
            else:
                grilleCopie.setCellule(i, self.formatJeton)

                # On vérifie que ce coup ne fait pas terminer la partie
                victoire = grilleCopie.alignementHorizontal(grilleCopie.derniereLigneJoue)
                victoire |= grilleCopie.alignementVertical(grilleCopie.derniereColonneJoue)
                victoire |= grilleCopie.alignementDiagonal()

                # Si la partie est gagnée par l'IA on donne le score max possible pour forcer le min max à prendre le coup
                if (victoire):
                    listeScoreMax.append(sys.maxsize)
                else:
                    # Sinon on ajoute le score a la colonne
                    listeScoreMax.append(self.minF(profondeur - 1, grilleCopie))

        # On envoie l'index de la colonne qui est le max parmi toutes les colonnes
        return listeScoreMax.index(max(listeScoreMax))
        
    def max(self,profondeur,grille):
        """
        Côté Max (IA)
        Il récupère le coup qui lui donne le plus de point (Max) ou qui minimise les points de l'adversaire tout en essayant de se bénéficier
        Pour minimiser il va prendre le Max de la liste reçu
        """
        
        listeScoreMax = []
        
        # Si la profondeur à atteint 0 donc on a atteint le seuil de l'algo on envoie le score du Min sinon on continue a regarder en profondeur
        if (profondeur > 0):
            for i in range(Grille.COLONNE):  
                grilleCopie : Grille = copy.deepcopy(grille)  

                if (grilleCopie.colonneRemplie(i)):
                    listeScoreMax.append(-10000)
                else :
                    grilleCopie.setCellule(i,self.formatJeton)

                    victoire = grilleCopie.alignementHorizontal(grilleCopie.derniereLigneJoue)
                    victoire |= grilleCopie.alignementVertical(grilleCopie.derniereColonneJoue)
                    victoire |= grilleCopie.alignementDiagonal()

                    if (victoire):
                        listeScoreMax.append(self.evaluerPositionJoueur(grilleCopie, self.formatJeton) + 200)
                    else:
                        listeScoreMax.append(self.minF(profondeur - 1,grilleCopie))
             
            return max(listeScoreMax)
        else:
            # Le coup étant le dernier à prévoir on envoie le score de la partie simulé
            return -self.evaluerPositionEnnemi(grille, "o" if self.formatJeton == "x" else "x")
        
    
    def minF(self,profondeur,grille:Grille):
        """
        Côté Min (Adversaire)
        Il récupère le coup qui lui donne le plus de point (Min) ou qui minimise les points de l'IA tout en essayant de se bénéficier
        Pour minimiser il va prendre le Min de la liste reçu
        """
        listeScoreMin = []

        if (profondeur > 0):
            for i in range(Grille.COLONNE):    
                grilleCopie : Grille = copy.deepcopy(grille)

                # Si la colonne est remplie on veut que l'Ia ou l'adversaire ne joue pas dans cette colonne 
                # donc on donne un score élevé pour que le min évite de jouer le coup        
                if (grilleCopie.colonneRemplie(i)):
                    listeScoreMin.append(10000)
                else:
                    grilleCopie.setCellule(i, "o" if self.formatJeton == "x" else "x")
                    
                    victoire = grilleCopie.alignementHorizontal( grilleCopie.derniereLigneJoue)
                    victoire |= grilleCopie.alignementVertical( grilleCopie.derniereColonneJoue)
                    victoire |= grilleCopie.alignementDiagonal()
                    
                    if (victoire):
                        listeScoreMin.append(-self.evaluerPositionEnnemi(grilleCopie,"o" if self.formatJeton == "x" else "x") - 200)
                    else:
                        listeScoreMin.append(self.max(profondeur-1,grilleCopie))
             
            return min(listeScoreMin)
        else:
            return self.evaluerPositionJoueur(grille, self.formatJeton)

    def evaluerPositionJoueur(self,grilleteste : Grille,jeton:str) :
        score = 0

        for colonne in range(Grille.COLONNE):
            for ligne in range(Grille.LIGNE):
                if (grilleteste.getCellule(colonne, ligne) == jeton):
                    score += IA.grille[ligne][colonne]
        
        return score
    
    def evaluerPositionEnnemi(self, grilleteste:Grille, jeton) :
        score = 0

        for colonne in range(Grille.COLONNE):
            for ligne in range(Grille.LIGNE):
                if (grilleteste.getCellule(colonne, ligne) == jeton ): 
                    score += IA.grille[ligne][colonne]

        return score