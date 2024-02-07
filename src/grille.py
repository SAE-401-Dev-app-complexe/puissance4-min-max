class Grille:

    COLONNE: int = 7
    LIGNE: int = 6
    AFFICHAGE : str = "+---+---+---+---+---+---+---+\n"

    def __init__(self):
        """
        Genere un tableau COLONNE x LIGNE remplie de chaine vide
        """
        self.grille = [[" "] * self.COLONNE for _ in range(self.LIGNE)]

    def __str__(self):
        """
        Convertie la grille en une chaîne de caractères
        """
        grille_str = ""
        affichage_colone = ""
        for i in range(1 , self.COLONNE+1) :
            affichage_colone += "  " + str(i) + " "
        grille_str += affichage_colone +"\n" 
        for ligne in self.grille:
            grille_str += self.AFFICHAGE + "| "
            grille_str += " | ".join(map(str, ligne)) + " |\n"
        grille_str += self.AFFICHAGE  + affichage_colone
        return grille_str
    
    def getCellule(self, x, y):
        """
        Récupére la valeur de la cellule aux coordonnées (x, y)
        """
        return self.grille[y][x]

    def setCellule(self , x , valeur):
        """ 
        Modifie la valeur de la grille en x , y 
        Y etant la dernière case de la colonne differente de
        la valeur par defaut etant " "
        """
        y = self.getDernierIndiceLibre(x)
        self.grille[y-1][x] = valeur

    def getDernierIndiceLibre(self , y):
        """
        Renvoie l'indice de la dernière case vide dans la colonne
        @throws IndexError si colonne remplie
        """
        for i in range (self.LIGNE , 0  , -1 ):
            if self.grille[i-1][y] == " " : 
                return i
        raise IndexError("Colonne remplie ! Veuillez jouer ailleurs.")
            
        

# Exemple d'utilisation
ma_grille = Grille()
try :
    ma_grille.setCellule( 1 , "x")
    print(ma_grille)
    ma_grille.setCellule( 1 , "o")
    print(ma_grille)
    ma_grille.setCellule( 1 , "x")
    print(ma_grille)
    ma_grille.setCellule( 1 , "x")
    print(ma_grille)
    ma_grille.setCellule( 1 , "o")
    print(ma_grille)
    ma_grille.setCellule( 1 , "x")
    print(ma_grille)
    ma_grille.setCellule( 6, "0")
    print(ma_grille)
except IndexError as e :
    print(e.args[0])

