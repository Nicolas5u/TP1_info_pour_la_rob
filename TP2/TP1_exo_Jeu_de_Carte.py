form abc import ABC, abstractmethod
import random


class Cartes(ABC):
    def appliquer(self, joueur):
        pass



class CarteNormale(Cartes):

    def __init__(self):
    
    def valeur(self, joueur):
        points = random.randint(1, 10)
        joueur.ajouter_score(points)
        return f'Carte normale + {points} points'


class Cartebonus(Cartes):

    def valeur(self, joueur):
        joueur.ajouter_score(joueur.score)
        return f'Carte Bonus+ {points} points'


class CarteMalus(Cartes):
cd
    def valeur(self, joueur):
        points=-5
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



if __name__='main':

    j1=Joueur("j1")
    j2=Joueur("j2")
    int nb_tours
    #nb_tours=input('Combien de tours ?')
    nb_tours=5

    for i in range (0, nb_tours):
        print(f'tour numéro {i}')
        for joueur in Joueur:
            piocher(deck, joueur)
            print(f'joueur {Joueur.nom} : {Joueur.score}')
