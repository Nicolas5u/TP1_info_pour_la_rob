from TP_exo4 import Cible
from TP_exo4 import Position
from TP_exo4 import Robot

class Parcours:
    def __init__(self):
        """Crée un parcours vide"""
        self.cibles = []

    def ajouter_cible(self, cible):
        """Ajoute une cible à la fin du parcours"""
        self.cibles.append(cible)

    def nombre_cibles(self):
        """Retourne le nombre total de cibles dans le parcours"""
        return len(self.cibles)

    def cible_suivante(self, robot=None):
        
        if robot is None:
            return self.cibles[0] if self.cibles else None
        for cible in self.cibles:
            if not cible.est_atteinte_par(robot):
                return cible
        return None  # Toutes les cibles ont été atteintes

    def afficher(self):

        if not self.cibles:
            print("Parcours vide")
        else:
            print("Parcours :")
            for i, cible in enumerate(self.cibles, start=1):
                print(f"{i}. {cible.nom} à (x={cible.position.x}, y={cible.position.y})")
     
    def executer_parcours(self, robot):
        for cible in self.cibles:
            robot.aller_vers(cible.position)



parcours = Parcours()
parcours.ajouter_cible(Cible(Position(2, 0), "Point A"))
parcours.ajouter_cible(Cible(Position(2, 3), "Point B"))
parcours.ajouter_cible(Cible(Position(5, 3), "Point C"))
assert parcours.nombre_cibles() == 3

robot = Robot()
parcours.executer_parcours(robot)
# Vérifier que le robot a atteint la dernière cible
derniere_cible = Cible(Position(5, 3), "Point C")
assert derniere_cible.est_atteinte_par(robot) == True