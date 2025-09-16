import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


class Position:
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y

    def __add__(self, autrecoord):
        return Position(self.x + autrecoord.x, self.y + autrecoord.y) #on ajoute aux coordonnées de 'self' les coordonnées d'un nouveau point


    def afficher(self):
        print(f'les coord sont (x={self.x} ,y={self.y})')

    def distance_vers(self, autre):
        dx=autre.x - self.x
        dy=autre.y - self.y
        d=math.sqrt(dx**2 + dy**2)
        print(f'la distance est: {d}')
        return d

class Robot:
    def __init__(self, x=0, y=0, position=None):
        if position is not None:
            self.position=position
        else:
            self.position=Position(x, y)

    def avancer_droite(self, n):
        self.position.x+=n

    def avancer_haut(self, n):
        self.position.y+=n

    def distance_vers_robot(self, autre_robot):
        return self.position.distance_vers(autre_robot.position)

    def aller_vers(self, cible):
        while self.position.x<cible.x :
            self.avancer_droite(1)
        while self.position.x>cible.x :
            self.position.x-=1


        while self.position.y<cible.y :
            self.avancer_haut(1)
        while self.position.y>cible.y :
            self.position.y-=1
        

class Cible:
    def __init__(self, position, nom):
        self.position=position
        self.nom=nom

    def est_atteinte_par(self, robot):
        return self.position.x==robot.position.x and self.position.y==robot.position.y

    def distance_depuis(self, robot):
        return self.position.distance_vers(robot.position)

    def afficher(self):
        print(f'Cible: {self.nom} position x:{self.position.x} y={self.position.y}')

cible = Cible(Position(5, 3), "Sortie")
robot = Robot(position=Position(2, 1))
assert cible.est_atteinte_par(robot) == False
assert cible.distance_depuis(robot) == distance(2, 1, 5, 3)
robot.aller_vers(Position(5, 3))
assert cible.est_atteinte_par(robot) == True