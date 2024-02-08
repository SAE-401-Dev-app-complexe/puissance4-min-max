from Alignement import Alignement
from Colonne import Colonne
from typing import List
from GrilleIndexOutOfRange import GrilleIndexOutOfRange
from Jeton import Jeton
class Grille():
    
    nbColonne = 7
    nbLigne = 6
    
    def __init__(self):
        self.nbColonne = 7
        self.nbLigne = 6
        self.colonnes:List[Colonne]= []
        self.alignements:List[Alignement] = []
        
        for i in range(self.nbColonne):
            colonne = Colonne(i)
            self.colonnes.append(colonne)
        
    
    def affichageGrille(self) :
        affichage =""
        for ligne in range (self.nbLigne-1,-1,-1):
        
            affichage += "["
            
            for colonne in self.colonnes:
                if colonne.getIndex() == self.nbColonne-1 :
                    affichage += " " +str(colonne.getContenue(ligne)) +" "
                else :
                    
                    affichage += " "+ str(colonne.getContenue(ligne)) +" ,"
                
            affichage += "]\n"
        print(affichage)
    def placeJeton(self,jeton:Jeton):
        index = int(jeton.getColonne())

        valeurCorrecte = True
        if(index > self.nbColonne-1) :
            raise GrilleIndexOutOfRange("La valeur de la colonne est incorrecte")
        if index < 0 :
            raise GrilleIndexOutOfRange("La valeur de la colonne est incorrecte")
        if valeurCorrecte == True: 
            self.colonnes[jeton.getColonne()].ajoutJeton(jeton.getJeton())
            self.lastIndexPlay = jeton.getColonne()
            self.lastColonnePlay:Colonne = self.colonnes[jeton.getColonne()]
            
            return self.VerificationVictoire(self.colonnes[jeton.getColonne()],4)
    
        
    def getAlignement(self,tailleAlignement,alignement:Alignement,colonne):
        nombre = 0
        alignementListe :List[Alignement] = []
        alignementBase = Alignement(alignement.xdebut,alignement.ydebut,alignement.formatJetonAlignement)
        if(self.getAlignementVertical(tailleAlignement,alignement.xdebut,colonne,alignementBase)):
            #print("vertical")
            alignementListe.append(alignementBase)
        alignementBase = Alignement(alignement.xdebut,alignement.ydebut,alignement.formatJetonAlignement)
        if self.getAlignementHorizontal(tailleAlignement,alignement.ydebut,alignement.xdebut,alignementBase):
            alignementListe.append(alignementBase)
        alignementBase = Alignement(alignement.xdebut,alignement.ydebut,alignement.formatJetonAlignement)
        if(self.getAlignementDiagonal(tailleAlignement,alignement.ydebut,alignement.xdebut,alignementBase)):
            alignementListe.append(alignementBase)
        alignementBase = Alignement(alignement.xdebut,alignement.ydebut,alignement.formatJetonAlignement)
        if(self.getAlignementHautBas(tailleAlignement,alignement.ydebut,alignement.xdebut,alignementBase)):
            
            alignementListe.append(alignementBase)
        #self.alignements = alignementListe
        return alignementListe
        
    def getAlignementVertical(self,tailleAlignementVoulue,lignePosition:int,colonne : Colonne,alignement:Alignement):
        #print(lignePosition)
        trouvee = False
        if lignePosition < 0 :
            return False
        if lignePosition > self.nbLigne :
            return False
        #print(colonne.getContenue(lignePosition))
        #print(alignement.formatJetonAlignement)
        if alignement.formatJetonAlignement != colonne.getContenue(lignePosition):
            return False
        #print("ok")
        #print(alignement.xFin)
        #print(alignement.ajoutSegmentVertical(lignePosition,alignement.ydebut))
        alignement.ajoutSegmentVertical(lignePosition,alignement.ydebut)
        
        if(tailleAlignementVoulue == alignement.longueur) :
            return True
        if(alignement.xFin > lignePosition-1):
            trouvee= self.getAlignementVertical(tailleAlignementVoulue,lignePosition-1,colonne,alignement)
        #print(alignement.xFin< lignePosition+1)
        if(alignement.xdebut< lignePosition+1):
            trouvee |= self.getAlignementVertical(tailleAlignementVoulue,lignePosition+1,colonne,alignement)
        return trouvee
    
        
    def getAlignementHorizontal(self,tailleAlignementVoulue,colonnePosition:int,lignePosition,alignement : Alignement):
        trouvee = False
        if colonnePosition >= self.nbColonne or colonnePosition <0 :
            return False
        if alignement.formatJetonAlignement != self.colonnes[colonnePosition].getContenue(lignePosition):
            return False
        
        alignement.ajoutSegmentHorizontal(lignePosition,colonnePosition)
        ##print("debut " + str(alignement.xdebut))
        if(tailleAlignementVoulue == alignement.longueur) :
            return True
        if(alignement.yFin < colonnePosition+1):
            trouvee = self.getAlignementHorizontal(tailleAlignementVoulue,colonnePosition+1,lignePosition,alignement)
        if(alignement.ydebut > colonnePosition-1):
            
            trouvee |= self.getAlignementHorizontal(tailleAlignementVoulue,colonnePosition-1,lignePosition,alignement)
        return trouvee
        
    def getAlignementDiagonal(self,tailleAlignementVoulue,colonnePosition:int,lignePosition,alignement:Alignement):
        trouvee = False
        if lignePosition < 0 or lignePosition >= self.nbLigne:
            return False
        if colonnePosition >= self.nbColonne or colonnePosition <0 :
            return False
        if alignement.formatJetonAlignement != self.colonnes[colonnePosition].getContenue(lignePosition):
            return False
        alignement.ajoutSegmentDiagonalBasHaut(lignePosition,colonnePosition)
        if(tailleAlignementVoulue == alignement.longueur) :
            return True
        if(alignement.xFin < lignePosition+1 and alignement.yFin < colonnePosition+1):
            trouvee = self.getAlignementDiagonal(tailleAlignementVoulue,colonnePosition+1,lignePosition+1,alignement)
        if(alignement.xdebut > lignePosition-1 and alignement.ydebut > colonnePosition-1):
            trouvee = self.getAlignementDiagonal(tailleAlignementVoulue,colonnePosition-1,lignePosition-1,alignement)
        
        return trouvee
    
    def getAlignementHautBas(self,tailleAlignementVoulue,colonnePosition:int,lignePosition,alignement:Alignement):
        trouvee = False
        if lignePosition < 0 or lignePosition >= self.nbLigne:
            return False
        if colonnePosition >= self.nbColonne or colonnePosition <0 :
            return False
        if alignement.formatJetonAlignement != self.colonnes[colonnePosition].getContenue(lignePosition):
            return False
        
        alignement.ajoutSegmentDiagonalHautBas(lignePosition,colonnePosition)
        
        
        if(tailleAlignementVoulue == alignement.longueur) :
            
            return True
        
        if(alignement.xFin > lignePosition-1 and alignement.yFin < colonnePosition+1):
            trouvee = self.getAlignementHautBas(tailleAlignementVoulue,colonnePosition+1,lignePosition-1,alignement)
        if(alignement.xdebut < lignePosition+1 and alignement.ydebut > colonnePosition-1):
            trouvee |= self.getAlignementHautBas(tailleAlignementVoulue,colonnePosition-1,lignePosition+1,alignement)
        
        return trouvee
    
    def grilleRempli(self):
        grilleRempli = True
        for colonne in self.colonnes:
            if(not colonne.colonneRempli()):
                grilleRempli =False
        return grilleRempli
    
    
    def VerificationVictoire(self,colonne :Colonne,indexVictoire):
    
        alignement = Alignement(colonne.indexLastJetonPlace(),colonne.index,colonne.lastJetonPlace())
        alignementTrouvee = self.getAlignementVertical(indexVictoire,colonne.indexLastJetonPlace()-1,colonne,alignement)
        alignement = Alignement(colonne.indexLastJetonPlace(),colonne.index,colonne.lastJetonPlace())
        alignementTrouvee |=self.getAlignementHorizontal(indexVictoire,colonne.index,colonne.indexLastJetonPlace(),alignement)

        alignement = Alignement(colonne.indexLastJetonPlace(),colonne.index,colonne.lastJetonPlace())
        alignementTrouvee |=self.getAlignementDiagonal(indexVictoire,colonne.index,colonne.indexLastJetonPlace(),alignement)
        alignement = Alignement(colonne.indexLastJetonPlace(),colonne.index,colonne.lastJetonPlace())
        alignementTrouvee |=self.getAlignementHautBas(indexVictoire,colonne.index,colonne.indexLastJetonPlace(),alignement)
        return alignementTrouvee

    def blocagePossible(self, ali:Alignement):
        
        
        if(ali.ajoutSegmentHorizontal(ali.xdebut,ali.ydebut-1) and ali.ydebut-1 > 0 and self.colonnes[ali.ydebut].getContenue(ali.xdebut)== " "):
            return True
        
        
        elif(ali.ajoutSegmentHorizontal(ali.ydebut,ali.yFin+1)and ali.yFin+1< self.nbColonne and self.colonnes[ali.yFin].getContenue(ali.xdebut)== " "):
            #print("o31")
            
            return True

        elif(ali.ajoutSegmentVertical(ali.xdebut+1,ali.yFin)and ali.xdebut+1< self.nbLigne):
            
            return True
        elif(ali.ajoutSegmentVertical(ali.xdebut-1,ali.yFin)and ali.xdebut-1< 0):
            
            return True
        elif ali.ajoutSegmentDiagonalHautBas(ali.xdebut-1,ali.yFin+1)and ali.xdebut-1< 0 and ali.yFin+1< self.nbColonne and  self.colonnes[ali.yFin].getContenue(ali.xdebut)== " ":
            return True
            
        return False
    def colonneRempli(self,index) :
        return self.colonnes[index].colonneRempli()
    
    def VictoirePotentiel(self,alignement):
        alignement
grille = Grille()
grille.placeJeton(Jeton("X",2))
grille.placeJeton(Jeton("X",2))
grille.placeJeton(Jeton("X",2))

grille.affichageGrille()
#print(grille.getAlignementVertical(3,0,grille.lastColonnePlay,Alignement(0,2,"X")))

