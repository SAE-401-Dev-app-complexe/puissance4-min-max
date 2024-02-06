from Evaluateur import Evaluateur
from GrilleIndexOutOfRange import GrilleIndexOutOfRange
from JoueurClavier import JoueurClavier
from IA import IA
from Joueur import Joueur
from Grille import Grille
from SaisieException import SaisieException
class Jeu:
    global partieConfigure 
    partieConfigure = False
    
    @staticmethod
    def configurerPartie():
        global JoueurA
        global JoueurB
        global grillePartie


        grillePartie = Grille()
        
        evaluateur = Evaluateur(grillePartie,"X","O")
        JoueurB = JoueurClavier("E","X")
        JoueurA = IA("a","O",evaluateur)
        print(evaluateur)
    
        global joueurJouant
        joueurJouant  = JoueurB
    
    
    
    @staticmethod
    def lancerPartie():
        global partieConfigure
        global joueurJouant 
        partieNonTermine = True
        if partieConfigure == False :
            Jeu.configurerPartie()
        grillePartie.affichageGrille()
        while(partieNonTermine) :
            tourGagnant = Jeu.tourJoueur(joueurJouant)
            
            grillePartie.affichageGrille()
            if(tourGagnant):
                partieNonTermine= False
                print("Le joueur " +str(joueurJouant.getNom())+ " a gagné")
            else :
                partieNonTermine = not grillePartie.grilleRempli()
                joueurJouant = Jeu.nextPlayer()
            
            
            
    
    
    def nextPlayer():
        global joueurJouant
        if (joueurJouant == JoueurA):
            return JoueurB
        else :
            return JoueurA

    
    @staticmethod
    def tourJoueur(Joueur:Joueur):
        tourNonReussi = True
        erreurSaisies = False
        while (tourNonReussi):
            if(not erreurSaisies or not Joueur.IA):
                print("C'est au tour de " +str(Joueur.getNom())+ " de jouer un jeton")
                print("Votre jeton est "+str(Joueur.getFormatJeton()))
            try:
                coupGagnant = grillePartie.placeJeton(Joueur.playJeton()) 
                tourNonReussi = False
            except GrilleIndexOutOfRange as e:
                erreurSaisies = True
                Jeu.affichageException(e.message,Joueur.IA)
            except SaisieException as e:
                erreurSaisies = True
                Jeu.affichageException(e.message,Joueur.IA)
        return coupGagnant
                
    @staticmethod
    def affichageException(message,IA) :
        if(not IA):
            grillePartie.affichageGrille()
            print(message)
        
        
Jeu.lancerPartie()