from GrilleIndexOutOfRange import GrilleIndexOutOfRange


class Colonne():
    
    taille = 6
    
    def __init__(self,index):
        self.contenue = []
        self.nombreJeton = 0
        self.index = index
        
    def getIndex(self):
        return self.index
    def estVide(self):
        if self.nombreJeton ==0 :
            return True
        else :
            return False
    def colonneRempli(self):
        return self.nombreJeton == Colonne.taille
    
    def ajoutJeton(self,formatJeton):
        if(not self.colonneRempli()) :
            self.contenue.append(formatJeton)
            self.nombreJeton += 1
        else :
            raise GrilleIndexOutOfRange("Cette colonne est déjà rempli")
    def indexRempli(self,index):
        return self.nombreJeton > index
    
    def getContenue(self,index):
        if self.indexRempli(index):
            return self.contenue[index]
        else:
            return " "
        
    def lastJetonPlace(self):
        return self.contenue[self.nombreJeton - 1] if self.nombreJeton > 0 else None
    
    def indexLastJetonPlace(self):
        return self.nombreJeton - 1 if self.nombreJeton > 0 else None