print("Hello voici l'exo Robot, Parcours et Terrain du TP 1")

from math import sqrt

# ===============================
# Classe Position
# ===============================

# Rôle : Représente une position dans le plan (x, y)
class Position:
    # Entrées : x, y (float) coordonnées initiales, défaut 0
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # Rôle : additionner deux positions
    def __add__(self, autre: 'Position') -> 'Position':
        return Position(self.x + autre.x, self.y + autre.y)

    # Rôle : afficher les coordonnées de la position
    def afficher(self):
        print(f"Position(x={self.x}, y={self.y})")

    # Entrées : autre (Position)
    # Sortie : distance (float)
    # Rôle : calcule la distance euclidienne vers une autre position
    def distance_vers(self, autre: 'Position') -> float:
        dx = autre.x - self.x
        dy = autre.y - self.y
        return sqrt(dx**2 + dy**2)

# ===============================
# Classe Robot
# ===============================

# Rôle : Représente un robot pouvant se déplacer dans le plan
class Robot:
    # Entrées : position (Position), par défaut (0,0)
    def __init__(self, position: Position = None):
        if position is not None:
            self.position = position
        else:
            self.position = Position(0, 0)

    # Entrées : n (int)
    # Rôle : avancer de n cases vers la droite
    def avancer_droite(self, n: int):
        self.position.x += n

    # Entrées : n (int)
    # Rôle : avancer de n cases vers le haut
    def avancer_haut(self, n: int):
        self.position.y += n

    # Entrées : autre_robot (Robot)
    # Sortie : distance (float)
    # Rôle : calcule la distance entre deux robots
    def distance_vers_robot(self, autre_robot: 'Robot') -> float:
        return self.position.distance_vers(autre_robot.position)

    # Entrées : cible (Position)
    # Rôle : déplace le robot case par case vers la position cible
    def aller_vers(self, cible: Position):
        # Déplacement horizontal
        while self.position.x < cible.x:
            self.avancer_droite(1)
        while self.position.x > cible.x:
            self.position.x -= 1

        # Déplacement vertical
        while sel
