import TP_exo1
import math

class Position:
    # Entrées : x, y (int ou float, par défaut 0)
    # Rôle : Représente une position dans un plan avec coordonnées (x, y)
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # Entrées : autrecoord (Position)
    # Sortie : (Position) nouvelle position
    # Rôle : Définit l’addition entre deux positions (somme des coordonnées)
    def __add__(self, autrecoord):
        return Position(self.x + autrecoord.x, self.y + autrecoord.y)  # on ajoute aux coordonnées de 'self' celles d'un autre point

    # Sortie : None
    # Rôle : Affiche les coordonnées de la position au format (x, y)
    def afficher(self):
        print(f'les coord sont (x={self.x} ,y={self.y})')

    # Entrées : autre (Position)
    # Sortie : (float) distance euclidienne
    # Rôle : Calcule et affiche la distance euclidienne entre deux positions
    def distance_vers(self, autre):
        dx = autre.x - self.x
        dy = autre.y - self.y
        d = math.sqrt(dx**2 + dy**2)
        print(f'la distance est: {d}')
        return d


# Tests
pos1 = Position(1, 1)
pos1.afficher()  # les coord sont (x=1 ,y=1)

pos2 = Position(4, 5)
pos2.afficher()  # les coord sont (x=4 ,y=5)

pos3 = pos1 + pos2
pos3.afficher()  # les coord sont (x=5 ,y=6)

assert pos1.distance_vers(pos2) == 5.0

