import sys
from src.joueur import *
from src.grille import Grille
import copy
class IA(Joueur):

    grille = [  [3 , 4 , 5 , 7 , 5 , 4 , 3 ] , 
                [4 , 6 , 8 , 10 , 8 , 6 , 4] ,
                [5 , 8 , 11 , 13 , 11 , 8 , 5] ,
                [5 , 8 , 11 , 13 , 11 , 8 , 5], 
                [4 , 6 , 8 , 10 , 8 , 6 , 4] ,
                [3 , 4 , 5 , 7 , 5 , 4 , 3]
             ]

    def __init__(self, nom, formatJeton, grille):
        super().__init__(nom, formatJeton, True)
        self.grille = grille

    def jouerJeton(self, grille):
        """
        Applique l'algo MinMax pour décider d'une colonne dans lequelle jouer
        """

        grille.setCellule(self.minMax(5, grille), self.formatJeton)
      
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

    
    def minMax(self, profondeur,grille:Grille):
        """
        Première partie de l'algo : côté Max (IA)
        A la fin de l'algo l'index du max sur les 7 colonnes est pris ce qui désignera le coup joué par l'IA

        """
        #Cette liste correspond aux différents colonnes jouer sur la grille
        listeScoreMax = []
        for i in range(Grille.COLONNE):
            #On crée une grille qui est une copie de la grille du jeu pour simuler le reste de la partie
            grilleCopie : Grille = copy.deepcopy(grille)      
            #Si la colonne est rempli on veut que l'Ia ou l'adversaire ne joue pas dans cette colonne 
            #donc on donne un score bas pour que le max évite de jouer le coup           
            if (grilleCopie.colonneRemplie(i)):
                listeScoreMax.append(-10000)
            else :
                grilleCopie.setCellule(i,self.formatJeton)
                # On vérifie que ce coup ne fait pas terminer la partie
                victoire = grilleCopie.alignementHorizontal( grilleCopie.derniereLigneJoue)
                victoire |= grilleCopie.alignementVertical( grilleCopie.derniereColonneJoue)
                victoire |= grilleCopie.alignementDiagonal()    
                #Si la partie est gagné par l'IA on donne le score max possible pour forcer Le min max à prendre le coup
                if (victoire):
                    #listeScore2.append(self.evaluateur.evaluerGrilleSelonJoueur(self.formatJeton,grilleCopie)+20)
                    listeScoreMax.append(sys.maxsize)
                else :
                    
                    ##print("minmax")
                    #Sinon on ajoute le score a la colonne
                    listeScoreMax.append(self.minF(profondeur-1,grilleCopie))
                    # print(listeScoreMax)
                    
        #On envoie l'index de la colonne qui est le max parmi toutes les colonnes
        return listeScoreMax.index(max(listeScoreMax))
        
    def max(self,profondeur,grille):
        """
        côté Max (IA)
        Il récupére le coup qui lui donne le plus de point (Max) ou qui minimise les points de l'adversaire tout en essayant de se bénéficier
        Pour minimiser il va prendre le Max de la liste reçu
        """
        
        listeScoreMax = []
        
        #Si la profondeur à atteint 0 donc on a atteint le seuil de l'algo on envoie le score du Min sinon on continue a regarder en profondeur
        if (profondeur > 0):
             for i in range(Grille.COLONNE):
            
                grilleCopie : Grille = copy.deepcopy(grille)                
                if(grilleCopie.colonneRemplie(i)):
                    listeScoreMax.append(-10000)
                else :
                    grilleCopie.setCellule(i,self.formatJeton)
                    victoire = grilleCopie.alignementHorizontal(grilleCopie.derniereLigneJoue)
                    victoire |= grilleCopie.alignementVertical(grilleCopie.derniereColonneJoue)
                    victoire |= grilleCopie.alignementDiagonal()
                    if(victoire):
                    #listeScore2.append(self.evaluateur.evaluerGrilleSelonJoueur(self.formatJeton,grilleCopie)+20)
                        listeScoreMax.append(self.evaluerPositionJoueur(grilleCopie,self.formatJeton) + 200)
                    else :
                        
                        
                        listeScoreMax.append(self.minF(profondeur-1,grilleCopie))
             
             return max(listeScoreMax)
        else : 
            #Le coup étant le dernier à prévoir on envoie le score de la partie simulé
            #return self.evaluateur.evaluerGrilleEnnemi(grille)
            return self.evaluerPositionEnnemi(grille,"o" if self.formatJeton == "x" else "x")
        
    
    def minF(self,profondeur,grille:Grille):
        """
        côté Min (Adversaire)
        Il récupére le coup qui lui donne le plus de point (Min) ou qui minimise les points de l'IA tout en essayant de se bénéficier
        Pour minimiser il va prendre le Min de la liste reçu


        """
        listeScoreMin = []
        if (profondeur > 0):
             for i in range(Grille.COLONNE):
            
                grilleCopie : Grille = copy.deepcopy(grille)          
                #Si la colonne est rempli on veut que l'Ia ou l'adversaire ne joue pas dans cette colonne 
                #donc on donne un score élevé pour que le min évite de jouer le coup        
                if(grilleCopie.colonneRemplie(i)):
                    listeScoreMin.append(10000)
                else :
                    grilleCopie.setCellule(i, "o" if self.formatJeton == "x" else "x")
                    victoire = grilleCopie.alignementHorizontal( grilleCopie.derniereLigneJoue)
                    victoire |= grilleCopie.alignementVertical( grilleCopie.derniereColonneJoue)
                    victoire |= grilleCopie.alignementDiagonal()
                    
                    if(victoire):
                    #listeScore2.append(self.evaluateur.evaluerGrilleSelonJoueur(self.formatJeton,grilleCopie)+20)
                        listeScoreMin.append(self.evaluerPositionEnnemi(grilleCopie,"o" if self.formatJeton == "x" else "x") - 200)
                    else :
                        listeScoreMin.append(self.max(profondeur-1,grilleCopie))
                        #print(listeScore2)
             
             return min(listeScoreMin)
        else : 
            #return self.evaluateur.evaluerGrilleSelonJoueur(self.formatJeton,grilleCopie) 
            return self.evaluerPositionJoueur(grille,self.formatJeton)
    def evaluerPositionJoueur(self,grilleteste : Grille,jeton:str) :
        score = 0
        #grille.affichageGrille()
        for colonne in range(Grille.COLONNE):
            for ligne in range(Grille.LIGNE):
                if(grilleteste.getCellule(colonne,ligne)== jeton):
                    
                    score += IA.grille[ligne][colonne]
                    #print(score)
        return score
    
    def evaluerPositionEnnemi(self,grilleteste:Grille,jeton) :
        score = 0
        #grille.affichageGrille()
        for colonne in range(Grille.COLONNE):
            for ligne in range(Grille.LIGNE):
                if(grilleteste.getCellule(colonne,ligne) == jeton ):
                    
                    score -= IA.grille[ligne][colonne]
                    #print(score)
        return score