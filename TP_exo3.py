import math



class Position:
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y

    def __add__(self, autrecoord):
        return Position(self.x + autrecoord.x, self.y + autrecoord.y) #on ajoute aux coordonnées de 'self' les coordonnées d'un nouveau point


    def afficher(self):
        print(f'les coord sont (x={self.x} ,y={self.y})')

    def distance_vers(self, autree):
        dx = autree.x - self.x
        dy = autree.y - self.y
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

    def aller_vers(self, autre_robot):
        while self.position.x<autre_robot.x :
            self.avancer_droite(1)
        while self.position.x>autre_robot.x :
            self.position.x-=1


        while self.position.y<autre_robot.y :
            self.avancer_haut(1)
        while self.position.y>autre_robot.y :
            self.position.y-=1
        


   
    




    def afficher(self):
        print(f"position du robot (x={self.position.x}, t={self.position.y})")


robot1 = Robot(position=Position(0, 0))
robot2 = Robot(position=Position(3, 4))
assert robot1.distance_vers_robot(robot2) == 5.0

robot1.aller_vers(Position(2, 3))
assert robot1.position.x == 2
assert robot1.position.y == 3