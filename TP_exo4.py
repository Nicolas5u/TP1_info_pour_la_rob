import math

# Fonction qui calcule la distance entre deux points (x1, y1) et (x2, y2)
def distance(x1: float, y1: float, x2: float, y2: float) -> float:
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# Classe qui représente une position 2D avec des coordonnées x et y
class Position:
    def __init__(self, x: float = 0, y: float = 0) -> None:
        self.x: float = x
        self.y: float = y

    # Permet d’additionner deux positions (surcharge de l’opérateur +)
    def __add__(self, autrecoord: "Position") -> "Position":
        return Position(self.x + autrecoord.x, self.y + autrecoord.y)  # on ajoute aux coordonnées de 'self' les coordonnées d'un nouveau point

    # Affiche les coordonnées de la position
    def afficher(self) -> None:
        print(f'les coord sont (x={self.x} ,y={self.y})')

    # Calcule et retourne la distance entre cette position et une autre
    def distance_vers(self, autre: "Position") -> float:
        dx: float = autre.x - self.x
        dy: float = autre.y - self.y
        d: float = math.sqrt(dx**2 + dy**2)
        print(f'la distance est: {d}')
        return d


# Classe qui représente un robot capable de se déplacer
class Robot:
    def __init__(self, x: float = 0, y: float = 0, position: Position | None = None) -> None:
        # Si une position est donnée, on l’utilise, sinon on crée une nouvelle position avec x et y
        if position is not None:
            self.position: Position = position
        else:
            self.position: Position = Position(x, y)

    # Déplace le robot vers la droite (augmentation de x)
    def avancer_droite(self, n: float) -> None:
        self.position.x += n

    # Déplace le robot vers le haut (augmentation de y)
    def avancer_haut(self, n: float) -> None:
        self.position.y += n

    # Calcule la distance entre ce robot et un autre robot
    def distance_vers_robot(self, autre_robot: "Robot") -> float:
        return self.position.distance_vers(autre_robot.position)

    # Déplace le robot pas à pas vers une position cible
    def aller_vers(self, cible: Position) -> None:
        # Déplacement en x
        while self.position.x < cible.x:
            self.avancer_droite(1)
        while self.position.x > cible.x:
            self.position.x -= 1

        # Déplacement en y
        while self.position.y < cible.y:
            self.avancer_haut(1)
        while self.position.y > cible.y:
            self.position.y -= 1
        

# Classe qui représente une cible avec un nom et une position
class Cible:
    def __init__(self, position: Position, nom: str) -> None:
        self.position: Position = position
        self.nom: str = nom

    # Vérifie si un robot est exactement sur la même position que la cible
    def est_atteinte_par(self, robot: Robot) -> bool:
        return self.position.x == robot.position.x and self.position.y == robot.position.y

    # Calcule la distance entre la cible et un robot donné
    def distance_depuis(self, robot: Robot) -> float:
        return self.position.distance_vers(robot.position)

    # Affiche les informations de la cible
    def afficher(self) -> None:
        print(f'Cible: {self.nom} position x:{self.position.x} y={self.position.y}')


#test

cible: Cible = Cible(Position(5, 3), "Sortie")
robot: Robot = Robot(position=Position(2, 1))
assert cible.est_atteinte_par(robot) == False
assert cible.distance_depuis(robot) == distance(2, 1, 5, 3)
robot.aller_vers(Position(5, 3))
assert cible.est_atteinte_par(robot) == True

