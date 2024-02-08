from Alignement import Alignement
from Grille import Grille
from typing import List
from Colonne import Colonne
from Jeton import Jeton
class Evaluateur():
    
    def __init__(self,grille:Grille,jetonJ,jetonA):
        self.grille:Grille = grille
        self.jetonJoueur = jetonJ
        self.jetonIA = jetonA
        
    def resetGrille(self,grille):
        self.grille = grille
    
    def evaluerGrilleSelonJoueur(self,formatJeton,grille:Grille):
        
        score = 0
        alignement4:List[Alignement] = []
        alignement3 :List[Alignement] = []
        alignement2 :List[Alignement] = []
        for colonne in grille.colonnes:
            for ligne in range(grille.nbLigne):
                ali = Alignement(ligne,colonne.index,formatJeton)
                alignement4 += grille.getAlignement(4,ali,colonne)
                alignement3 += grille.getAlignement(3,ali,colonne)
                alignement2 += grille.getAlignement(2,ali,colonne)
        
        alignement4 = self.retirerDoublons(alignement4)
        alignement3 = self.retirerDoublons(alignement3)
        alignement2 = self.retirerDoublons(alignement2)
        
        for ali3 in alignement3:
            if(not self.grille.blocagePossible(ali3)):
                alignement3.remove(ali3)
        for ali2 in alignement2:
            if(not self.grille.blocagePossible(ali2)):
                alignement2.remove(ali2)
        if(formatJeton == self.jetonJoueur):
            score -= len(alignement4)*100 - len(alignement3)*9-len(alignement2)*3 
        
        else : 
            score += len(alignement4)*100 + len(alignement3)*9+len(alignement2)*3
        return score
    
    def evaluerGrilleEnnemi(self,formatJeton,grille:Grille):
        
        score = 0
        
        alignement4:List[Alignement] = []
        alignement3 :List[Alignement] = []
        alignement2 :List[Alignement] = []
        for colonne in grille.colonnes:
            for ligne in range(grille.nbLigne):
                ali = Alignement(ligne,colonne.index,formatJeton)
                alignement4 += grille.getAlignement(4,ali,colonne)
                alignement3 += grille.getAlignement(3,ali,colonne)
                alignement2 += grille.getAlignement(2,ali,colonne)
        
        alignement4 = self.retirerDoublons(alignement4)
        alignement3 = self.retirerDoublons(alignement3)
        alignement2 = self.retirerDoublons(alignement2)
        for ali3 in alignement3:
            if(not self.grille.blocagePossible(ali3)):
                alignement3.remove(ali3)
        for ali2 in alignement2:
            if(not self.grille.blocagePossible(ali2)):
                alignement2.remove(ali2)
        print(table[grille.lastColonnePlay.index][grille.lastIndexPlay])
        score = -len(alignement4)*100 - len(alignement3)*9-len(alignement2)*3
        
        
        return score
    def retirerDoublons(self,liste:List[Alignement]):
        listeSansDoublons:List[Alignement] = []
        for i in range(0,len(liste),1):
            
            if(not isinstance(liste[i], list)):
                
                bon = True
                for listeS in listeSansDoublons:
                    
                        
                    ali2 = liste[i]
                        
                    if  self.compareTo(ali2, listeS):
                        bon = False
                if(bon):
                    listeSansDoublons.append(liste[i])
                
        return listeSansDoublons
    
    def compareTo(self,first:Alignement,other:Alignement):
        return (first.xdebut, first.ydebut) == \
                (other.xdebut, other.ydebut)
"""
grille = Grille()
grille.placeJeton(Jeton("X",5))
grille.placeJeton(Jeton("O",4))
grille.placeJeton(Jeton("X",4))
grille.placeJeton(Jeton("O",3))
grille.placeJeton(Jeton("O",3))
grille.placeJeton(Jeton("X",3))
grille.placeJeton(Jeton("O",2))
grille.placeJeton(Jeton("O",2))
grille.placeJeton(Jeton("O",2))
##print(grille.lastIndexPlay)
grille.affichageGrille()
eval =Evaluateur(grille)
##print(eval.evaluerGrilleSelonJoueur("X",grille))
"""
table = [[0,2,7,7,2,0],[2,5,7,7,5,2],[5,7,10,10,7,5],[5,7,10,10,7,5],[5,7,10,10,7,5],[2,5,7,7,5,2],[0,2,7,7,2,0]]
