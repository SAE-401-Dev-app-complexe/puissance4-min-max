class Grille:

    COLONNE: int = 7
    LIGNE: int = 6
    AFFICHAGE : str = "+---" * 7 + "+\n"

    def __init__(self):
        """
        Genere un tableau COLONNE x LIGNE remplie de chaine vide
        """
        self.grille = [[" "] * self.COLONNE for _ in range(self.LIGNE)]
        self.derniereColonneJoue = None
        self.derniereLigneJoue = None

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
        grille_str += self.AFFICHAGE  + affichage_colone + '\n'

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
        self.derniereColonneJoue = x
        self.derniereLigneJoue = y-1
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
            
    def alignementVertical(self , y ):
        """
        Verifie un alignement vertical de 4
        """
        tableau = self.grille
        # Ligne - 3 sinon Execption puisque ligne[5] + 1 n'exite pas par ex.
        for i in range(self.LIGNE-3):
            if all(tableau[i+k][y] != " " and tableau[i+k][y] == tableau[i][y] for k in range(1, 4)):
                return True
        return False
        
    def alignementHorizontal(self , x ):
        """
        Verifie un alignement dans la grille pour une ligne donnée
        """
        tableau = self.grille[x]
        # len(tableau) - 3 -> meme principe que pour les ligne
        for i in range(len(tableau)-3) :
            if tableau[i] != " " and tableau[i] == tableau [i+1] == tableau[i+2] == tableau[i+3] :
                return True
        return False
    

    def alignementDiagonal(self):
    # Vérification des diagonales de gauche à droite
        for i in range(self.LIGNE - 3):
            for j in range(self.COLONNE - 3):
                if (self.grille[i][j] != " " and
                    self.grille[i][j] == self.grille[i + 1][j + 1] == self.grille[i + 2][j + 2] == self.grille[i + 3][j + 3]):
                    return True

        # Vérification des diagonales de droite à gauche
        for i in range(self.LIGNE - 3):
            for j in range(3, self.COLONNE):
                if (self.grille[i][j] != " " and
                    self.grille[i][j] == self.grille[i + 1][j - 1] == self.grille[i + 2][j - 2] == self.grille[i + 3][j - 3]):
                    return True
        return False

    def grillePleine(self):
        """
        Vérifie si la grille est pleine.
        """
        for i in self.grille[0]:
            if i == ' ':
                return False
        return True

    def colonneRemplie(self, colonne: int):
        if (self.getCellule(colonne, 0) != ' '):
            return True
        return False

# ma_grille = Grille()
# try :

#     ma_grille.setCellule( 0 , "o")
#     print(ma_grille)
    
#     ma_grille.setCellule( 0 , "o")
#     print(ma_grille)
#     ma_grille.setCellule( 0 , "o")
#     print(ma_grille)
#     ma_grille.setCellule( 0 , "o")
#     print(ma_grille)
#     ma_grille.setCellule( 0 , "x")
#     print(ma_grille)
#     ma_grille.setCellule( 1 , "x")
#     ma_grille.setCellule( 0 , "x")
#     print(ma_grille)
#     ma_grille.setCellule( 6, "o")
#     ma_grille.setCellule( 5, "o")
#     ma_grille.setCellule( 4, "o")
#     ma_grille.setCellule( 3, "o")
#     ma_grille.setCellule( 3, "o")
#     ma_grille.setCellule( 3, "o")
#     ma_grille.setCellule( 3, "o")
#     ma_grille.setCellule( 5, "o")
#     ma_grille.setCellule( 4, "o")
#     ma_grille.setCellule( 4, "o")
#     print(ma_grille)
    
#     print(ma_grille.alignementVertical(0))
#     print(ma_grille.alignementHorizontal(5))
#     print(ma_grille.getCellule(0,2))
#     print(ma_grille.colonneRemplie(1))
# except IndexError as e :
#     print(e.args[0])