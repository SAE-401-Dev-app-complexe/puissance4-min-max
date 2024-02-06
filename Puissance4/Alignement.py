
class Alignement():
    def __init__(self,xdebut,ydebut,formatJeton):
        self.xdebut = xdebut
        self.ydebut = ydebut
        self.formatJetonAlignement = formatJeton
        self.xFin = xdebut
        self.yFin = ydebut
        self.longueur = 1
        
    def ajoutSegmentDiagonalBasHaut(self,x,y):
        if(self.xdebut <= x <= self.xFin or self.ydebut<= y <= self.yFin):
            return False
            
        succes = False
        
        
        if x+1 == self.xdebut and self.ydebut == y+1 :
            self.xdebut = x
            self.ydebut = y
            succes = True
        if x-1 == self.xFin and self.yFin == y-1 :
            
            
            self.xFin = x
            
            self.yFin = y
            succes = True
        
        
        if(succes):
            self.longueur +=1
        return succes
    
    def ajoutSegmentDiagonalHautBas(self,x,y):
        if(self.xdebut <= x <= self.xFin or self.ydebut<= y <= self.yFin):
            return False
            
        succes = False
        
        if x - 1 == self.xdebut and y + 1 == self.ydebut:
            self.xdebut = x
            self.ydebut = y
            succes = True
        
        if x + 1 == self.xFin and y - 1 == self.yFin:
            self.xFin = x
            self.yFin = y
            succes = True
        
        if(succes):
            self.longueur +=1
        return succes
    
    def ajoutSegmentHorizontal(self,x,y):
        if(self.xdebut  != x):
            return False
        if(self.ydebut <= y <= self.yFin):
            return False
        succes = False
        
        if y+1 == self.ydebut and self.xFin == x :
            self.ydebut = y
            succes = True
        if self.xFin == x  and self.yFin == y-1  :
            self.xFin =x
            self.yFin =y 
            succes = True
        
        if(succes):
            self.longueur +=1
        return succes
    def verifFormat(self, format):
        return format == self.formatJetonAlignement
    
    
    
    def ajoutSegmentVertical(self,x,y):
        if(self.ydebut != y or self.xdebut<= x <= self.xFin):
            return False
        
        succes = False
        
        if x+1 == self.xFin and self.yFin == y :
            self.xFin = x
            succes = True
        if x-1 == self.xdebut and self.yFin == y :
            self.xdebut = x
            succes = True
        
        if(succes):
            self.longueur +=1
        return succes
    def verifFormat(self, format):
        return format == self.formatJetonAlignement
""""
alignement = Alignement(0,2,"X")
print(alignement.ydebut)
print(alignement.ajoutSegmentHorizontal(0,1))
print(alignement.ydebut)
print(alignement.yFin)
print(alignement.ajoutSegmentHorizontal(0,3))
print(alignement.ydebut)
print(alignement.yFin)
print(alignement.longueur)
print(alignement.ajoutSegmentHorizontal(0,2))
print(alignement.longueur)
print(alignement.ajoutSegmentHorizontal(0,3))
print(alignement.longueur)
print(alignement.ajoutSegmentHorizontal(0,4))
print(alignement.ajoutSegmentHorizontal(0,2))
print(alignement.longueur)
print(alignement.ajoutSegmentHorizontal(0,3))
print(alignement.longueur)
print(alignement.ajoutSegmentHorizontal(0,4))
print(alignement.ajoutSegmentHorizontal(0,6))

alignement = Alignement(0,0,"X")
print(alignement.ajoutSegmentDiagonalHautBas(-1,1))
print(alignement.xdebut)
print(alignement.xFin)
print(alignement.ydebut)
print(alignement.yFin)
print(alignement.ajoutSegmentDiagonalHautBas(1,-1))
print(alignement.xdebut)
print(alignement.xFin)
print(alignement.ydebut)
print(alignement.yFin)
"""
al =Alignement(0,0,"Z")
print(al.ajoutSegmentVertical(1,0))
al.ajoutSegmentVertical(1,0)
print(al.ajoutSegmentVertical(2,0))
print(al.ajoutSegmentVertical(3,0))
al.ajoutSegmentVertical(1,0)
