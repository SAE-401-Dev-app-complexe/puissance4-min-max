class Jeton():
    def __init__(self,formatJeton):
        self.formatJeton = formatJeton
        self.numeroColonne = None
    
    def __init__(self,formatJeton,numeroColonne):
        self.formatJeton = formatJeton
        self.numeroColonne = numeroColonne
        
    def getJeton(self):
        return self.formatJeton
    
    def getColonne(self):
        return self.numeroColonne
    def setChoixColonne(self,index) :
        self.numeroColonne = index-1
