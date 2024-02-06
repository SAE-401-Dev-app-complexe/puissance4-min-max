from Alignement import Alignement
from Evaluateur import Evaluateur
from Joueur import Joueur
import copy
from Jeton import Jeton
import random
from Grille import Grille
class IA(Joueur):
    
    def __init__(self,nom,formatJeton,evaluateur:Evaluateur):
        super().__init__(nom,formatJeton,True)
        self.evaluateur:Evaluateur = evaluateur
        
    def playJeton(self) ->Jeton:
        ##print(self.evaluateur.grille.lastColonnePlay.indexLastJetonPlace())
        ##print(self.evaluateur.grille.lastIndexPlay)
        """""
        ali = Alignement(self.evaluateur.grille.lastColonnePlay.indexLastJetonPlace(),self.evaluateur.grille.lastIndexPlay,self.evaluateur.jetonJoueur)
        liste = self.evaluateur.grille.getAlignement(3,ali,self.evaluateur.grille.lastColonnePlay)
        for ele in liste :
            ##print(ele.xdebut)
            ##print(ele.xFin)
            ##print(ele.ydebut)
            ##print(ele.yFin)
            saisie = self.evaluateur.grille.blocagePossible(ele)
            ##print(saisie)
            if(saisie!= None):
                return Jeton(self.formatJeton,saisie)
        """
        saisie = self.playJetonTest()
        
        #saisie = random.randint(1, Grille.nbColonne)
        #jeton = Jeton(self.formatJeton,saisie)
        return Jeton(self.formatJeton,saisie)


    def playJetonTest(self):
        
        """ listeScore = []
        listeScoreE = []
        listeScore2Ia = []
        listeScoreEInd = []
        indexCoup = 0
        
        for i in range(self.evaluateur.grille.nbColonne):
            #print(i)
            grilleCopie = copy.deepcopy(self.evaluateur.grille)
            
            if(grilleCopie.colonneRempli(i)):
                listeScoreEInd.append(-10000)
            else :
                victoire = grilleCopie.placeJeton(Jeton(self.formatJeton,i))
                
                if(victoire):
                    listeScoreEInd.append(self.evaluateur.evaluerGrilleSelonJoueur(self.formatJeton,grilleCopie))
                else :
                    listeScore2 = []
                    for l in range(self.evaluateur.grille.nbColonne):
                        grilleCopie2 = copy.deepcopy(grilleCopie)
                        listeScore2.append(self.simulerJetonEnnemi(l,grilleCopie2))
                        
                        
                    listeScore2Ia.append(max(listeScore2))
                    #print(listeScore2)
                    listeScoreEInd.append(min(listeScore2))
                    
                    indexCoup = listeScoreEInd.index(max(listeScoreEInd))
        #print(listeScoreEInd)
        #print(indexCoup)"""
        """ for l in range(self.evaluateur.grille.nbColonne):
            grilleCopie = copy.deepcopy(self.evaluateur.grille)
            listeScoreE.append(self.simulerJetonEnnemi(l,grilleCopie))
            listeScoreEn2 = []
            for i in range(self.evaluateur.grille.nbColonne):
                grilleCopie2 = copy.deepcopy(grilleCopie)
                listeScoreEn2.append(self.simulerJetonEnnemi(l,grilleCopie))
            listeScoreEn2.append(max(listeScoreEn2))"""
        
            
        """"
        #print("Score iA " + str(max(listeScore)*1.25))
        #print("Score Joeuur " + str(max(listeScoreE)*0.85))
        #print("Score Max Joeuur apres tour ia" + str(max(listeScore2Ia)*0.85))
        #print("index ia " + str(listeScore.index(max(listeScore))))
        #print("index Joeur " + str(listeScoreE.index(max(listeScoreE))))
        #print("index Joeur apres ia " + str(listeScore2Ia.index(max(listeScore2Ia))))
        #print("score ia apres indexJoueur " + str(min(listeScoreEInd)))
        #print("score ia apres indexJoueur " + str(listeScore2Ia[listeScore.index(max(listeScore))]*0.85))
        if(max(listeScoreEn2)-1 > max(listeScore2Ia)):
            indexCoup = listeScoreEn2.index(max(listeScoreEn2))
            #print(indexCoup)
        else :
            indexCoup =listeScore2Ia.index(max(listeScore2Ia))"""
        """if(listeScore2Ia[listeScore.index(max(listeScore))]>max(listeScore)*1.25 and listeScore2Ia[listeScore.index(max(listeScore))]>max(listeScoreE)*1.50):
            pasbon = True
            i = 0
            while (pasbon):
                if(i>10):
                    indexCoup = random.randint(0,6)
                    #print("ind")
                    pasbon = False
                i+= 1
                
                #print("reset")
                indexCoup = listeScore.index(min(listeScore))
                if(self.evaluateur.grille.colonneRempli(indexCoup)):
                    listeScore.remove(min(listeScore))
                else : 
                    pasbon = False
            
            
            
        
            
        elif (max(listeScoreE)*0.85 > max(listeScore)*1.25):
            indexCoup = listeScoreE.index(max(listeScoreE))
            #print(indexCoup)
        else :
            indexCoup =listeScore.index(max(listeScore))"""
        return self.minMax(3,self.evaluateur.grille)
    
    def minMax(self, profondeur,grille):
        listeScore = []
        listeScore2 = []
        for i in range(self.evaluateur.grille.nbColonne):
            
            grilleCopie = copy.deepcopy(grille)                
            if(grilleCopie.colonneRempli(i)):
                listeScore2.append(-10000)
            else :
                victoire = grilleCopie.placeJeton(Jeton(self.formatJeton,i))
                    
                if(victoire):
                    listeScore2.append(self.evaluateur.evaluerGrilleSelonJoueur(self.formatJeton,grilleCopie)+20)
                else :
                    
                    #print("minmax")
                    
                    listeScore2.append(self.minF(profondeur-1,grilleCopie,i))
                    print("min")
                    print(listeScore2)
        return listeScore2.index(max(listeScore2))
    def max(self,profondeur,grille,position):
        
        listeScore = []
        listeScore2 = []
        if (profondeur > 0):
            for i in range(self.evaluateur.grille.nbColonne):
                
                grilleCopie = copy.deepcopy(grille)
                
                if(grilleCopie.colonneRempli(i)):
                    listeScore2.append(-10000)
                else :
                    victoire = grilleCopie.placeJeton(Jeton(self.formatJeton,i))
                    
                    if(victoire):
                        listeScore2.append(self.evaluateur.evaluerGrilleSelonJoueur(self.formatJeton,grilleCopie))
                    else :
                        
                        #print("max")
                        listeScore2.append(self.minF(profondeur-1,grilleCopie,i))
                        print("min")
                        print(listeScore2)
            #print(listeScore2)
            return (max(listeScore2))
        else : 
            return self.evaluateur.evaluerGrilleEnnemi(self.evaluateur.jetonJoueur,grille)
        
    
    def minF(self,profondeur,grilleCopie:Grille,position):
        valeur = 0
        listeScore = []
        #print("ok")
        listeScore2 = []
        if (profondeur > 0):
            for i in range(self.evaluateur.grille.nbColonne):
                grilleCopie2 = copy.deepcopy(grilleCopie)
                #print("ok2")
                if(grilleCopie2.colonneRempli(i)):
                    listeScore2.append(10000)
                else :
                    victoire = grilleCopie2.placeJeton(Jeton(self.evaluateur.jetonJoueur,i))
                    
                    if(victoire):
                        listeScore2.append(self.evaluateur.evaluerGrilleEnnemi(self.evaluateur.jetonJoueur,grilleCopie2))
                    else :
                        
                        
                        #print("min")
                        #grilleCopie2.affichageGrille()
                        listeScore2.append(self.max(profondeur-1,grilleCopie2,i))
                        print(listeScore2)
            
            return min(listeScore2)
        else : 
            return self.evaluateur.evaluerGrilleSelonJoueur(self.formatJeton,grilleCopie) 
    
    def simulerJeton(self,position,grilleCopie:Grille):
        if(grilleCopie.colonneRempli(position)):
            return -10000
        grilleCopie.placeJeton(Jeton(self.formatJeton,position))
        
        
        
        return self.evaluateur.evaluerGrilleSelonJoueur(self.formatJeton,grilleCopie)
    
    def simulerJetonEnnemi(self,position,grilleCopie:Grille):
        if(grilleCopie.colonneRempli(position)):
            return 10000
        
        grilleCopie.placeJeton(Jeton(self.evaluateur.jetonJoueur,position))
        #grilleCopie.affichageGrille()
        
        
        return self.evaluateur.evaluerGrilleEnnemi("X",grilleCopie)
    def getNom(self):
        return self.nom
""" Test
JoueurA = JoueurClavier("Jean","X")
JoueurA.playJeton()
JoueurA.getNom()

grille = Grille()
grille.placeJeton(Jeton("X",5))
grille.placeJeton(Jeton("O",4))
grille.placeJeton(Jeton("X",4))
grille.placeJeton(Jeton("O",3))
grille.placeJeton(Jeton("O",3))
grille.placeJeton(Jeton("X",3))
grille.placeJeton(Jeton("O",2))
grille.placeJeton(Jeton("O",2))
grille.affichageGrille()
ia = IA("A","X",Evaluateur(grille,"O","X"))
grille.placeJeton(ia.playJeton())
grille.affichageGrille()

"""
