form abc import ABC, abstractmethod
import random


class Cartes(ABC):



class CarteNormale(Cartes):

    def __init__(self):
    
    def valeur(self, joueur):
        points = random.randint(1, 10)
        joueur.ajouter_score(points)
        return f'Carte normale + {points} points'

class CarteBonus(Cartes): #regle

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


class Joueur
