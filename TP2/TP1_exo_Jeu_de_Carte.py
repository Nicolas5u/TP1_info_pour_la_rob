from abc import ABC, abstractmethod
import random


class Cartes(ABC):
    @abstractmethod
   
    def initialise_et_melange_liste(liste_carte):

        for i in range(30):
            liste_carte.append(CarteNormale())

        for i in range(6):
            liste_carte.append(CarteBonus())

        for i in range(5):
            liste_carte.append(CarteMalus())

        for i in range(15):
            liste_carte.append(CarteChance())
        
        random.shuffle(liste_carte) # Mélanger l'ordre des cartes

        return liste_carte
    
def piocher(liste_carte, joueur):
    carte_sortie = liste_carte.pop(0)
    print(f' {carte_sortie}')
    effet=carte_sortie.valeur(joueur)
    return carte_sortie


class CarteNormale(Cartes):
    
    def valeur(self, joueur):
        points = random.randint(1, 10)
        joueur.ajouter_score(points)
        return f'Carte normale + {points} points'


class CarteBonus(Cartes): #regle
    
    def valeur(self, joueur):
        joueur.ajouter_score(joueur.score)
        return f'Carte Bonus+ {points} points'


class CarteMalus(Cartes):
    
    def valeur(self, joueur):
        points =-5
        joueur.ajouter_score(points)
        return f'Carte malus {points} points'


class CarteChance(Cartes):
    
    def valeur(self, joueur):
        points=random.randint(-5, 15)
        joueur.ajouter_score(points)
        return f'Carte Chance + {points} points'


class Joueur:
    def __init__(self, nom, score=0):
        self.nom=nom
        self.score=score

    def ajouter_score(self, points):
        self.score += points

    def affichage(self):
        print(f'score actuel du {joueur.nom} : {joueur.score}')



if __name__=="__main__":

    Cartes.liste_carte=[]
    joueurs=[Joueur("léo"), Joueur("Nico")]
    joueur_actif = 0
    
    Cartes.initialise_et_melange_liste(Cartes.liste_carte)
    
    #nb_tours=input('Combien de tours ?')
    nb_tours=5

    for i in range (1, nb_tours+1):
        print(f'tour numéro {i}')
        for joueur in joueurs:
            piocher(Cartes.liste_carte, joueur)
            print(f'joueur {joueur.nom} : {joueur.score}')
        
