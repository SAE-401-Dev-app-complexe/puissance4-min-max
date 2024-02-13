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
    def __init__(self, nom, formatJeton  , grille):
        super().__init__(nom, formatJeton, True)
        self.grille = grille


    def jouerJeton(self):
        return self.minMax(5,self.grille)
      
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
        
        listeScoreMax = []
        for i in range(Grille.COLONNE):
            
            grilleCopie : Grille = copy.deepcopy(grille)                
            if(grilleCopie.colonneRempli(i)):
                listeScoreMax.append(-10000)
            else :
                grilleCopie.setCellule(i,self.formatJeton)
                victoire = grilleCopie.alignementHorizontal( grilleCopie.derniereLigneJoue)
                victoire |= grilleCopie.alignementVertical( grilleCopie.derniereColonneJoue)
                victoire |= grilleCopie.alignementDiagonal()    
                
                if(victoire):
                    #listeScore2.append(self.evaluateur.evaluerGrilleSelonJoueur(self.formatJeton,grilleCopie)+20)
                    listeScoreMax.append(sys.maxsize)
                else :
                    
                    ##print("minmax")
                    
                    listeScoreMax.append(self.minF(profondeur-1,grilleCopie))
                    print(listeScoreMax)
                    
            
        return listeScoreMax.index(max(listeScoreMax))
    def max(self,profondeur,grille):
        
        
        listeScoreMax = []
        if (profondeur > 0):
             for i in range(Grille.COLONNE):
            
                grilleCopie : Grille = copy.deepcopy(grille)                
                if(grilleCopie.colonneRempli(i)):
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
            #return self.evaluateur.evaluerGrilleEnnemi(grille)
            return self.evaluerPositionEnnemi(grille,"o" if self.formatJeton == "x" else "x")
        
    
    def minF(self,profondeur,grille:Grille):
        listeScoreMin = []
        if (profondeur > 0):
             for i in range(Grille.COLONNE):
            
                grilleCopie : Grille = copy.deepcopy(grille)                
                if(grilleCopie.colonneRempli(i)):
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