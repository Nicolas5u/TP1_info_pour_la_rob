<<<<<<< HEAD
salut
=======
class Position:
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y

    def __add__(self, autrecoord):
        return Position(self.x + autrecoord.x, self.y + autrecoord.y) #on ajoute aux coordonnées de 'self' les coordonnées d'un nouveau point


    def afficher(self):
        print(f'les coord sont (x={self.x} ,y={self.y})')

    def distance_vers(self, autrecoord):
        d=((autrecoord.x-self.x)**2 + (autrecoord.y-self.y)**2)**0.5 #norme d=racine carré de ((x'-x)²+(y'-y)²)
        print(f'la distance est: {d}')
        return d

pos1 = Position(1, 1)
pos1.afficher() # Position(x=0, y=0)
pos2 = Position(4, 5)
pos2.afficher() # Position(x=3, y=4)
pos3 = pos1 + pos2
pos3.afficher() # Position(x=3, y=4)

assert pos1.distance_vers(pos2) == 5.0
>>>>>>> eb3049f (Exo2)
