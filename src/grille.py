class Grille:
    COLONNE: int = 7
    LIGNE: int = 6
    AFFICHAGE : str = "+---+---+---+---+---+---+---+\n"


    def __init__(self):
        self.grille = [[0] * self.COLONNE for _ in range(self.LIGNE)]

    def __str__(self):
        # Convertir la grille en une chaîne de caractères
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
        # Récupérer la valeur de la cellule aux coordonnées (x, y)
        return self.grille[y][x]


# Exemple d'utilisation
ma_grille = Grille()
print(ma_grille)
print(ma_grille.getCellule(0,0))
