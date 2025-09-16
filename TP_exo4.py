"""
— Méthode est_atteinte_par(robot) qui vérifie si le robot a atteint la cible (même position)
— Méthode distance_depuis(robot) qui calcule la distance entre la cible et le robot
— Méthode afficher qui affiche les informations de la cible
cible = Cible(Position(5, 3), "Sortie")
robot = Robot(Position(2, 1))
assert cible.est_atteinte_par(robot) == False
assert cible.distance_depuis(robot) == distance_simple(2, 1, 5, 3)
robot.aller_vers(Position(5, 3))
assert cible.est_atteinte_par(robot) == True
"""

from TP_exo2 import Position

class Cible :                           # Classe Cible qui représente un objectif que le robot doit atteindre
    def __init__(self,position,nom) :   # Constructeur avec une position (Position) et un nom de cible
        self.position = Position(x,y)
        self.nom = nom
    
    def est_atteinte_par(robot) :       # Vérifie si le robot a atteint la cible (même position)
        if ()