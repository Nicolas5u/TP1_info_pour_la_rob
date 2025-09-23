from abc import ABC, abstractmethod
import random

# ---------- Classe abstraite des cartes ----------
class Cartes(ABC):
    """Classe abstraite représentant une carte du jeu"""

    @abstractmethod
    def valeur(self, joueur):
        """Applique l'effet de la carte sur le joueur"""
        pass

    @staticmethod
    def initialise_et_melange_liste(liste_carte) -> 'liste_carte':
        """
        Remplit la liste avec des cartes normales, bonus, malus et chance,
        puis mélange les cartes
        """
        for _ in range(30):
            liste_carte.append(CarteNormale())
        for _ in range(6):
            liste_carte.append(CarteBonus())
        for _ in range(5):
            liste_carte.append(CarteMalus())
        for _ in range(15):
            liste_carte.append(CarteChance())

        random.shuffle(liste_carte)
        return liste_carte

# ---------- Types de cartes ----------
class CarteNormale(Cartes):
    """Carte normale : ajoute un nombre aléatoire de points au joueur"""

    def valeur(self, joueur):
        points = random.randint(1, 10)
        joueur.ajouter_score(points)
        return f'Carte normale + {points} points'

class CarteBonus(Cartes):
    """Carte bonus : double le score actuel du joueur"""

    def valeur(self, joueur):
        points = joueur.score
        joueur.ajouter_score(points)
        return f'Carte Bonus + {points} points'

class CarteMalus(Cartes):
    """Carte malus : retire 5 points au joueur"""

    def valeur(self, joueur):
        points = -5
        joueur.ajouter_score(points)
        return f'Carte Malus {points} points'

class CarteChance(Cartes):
    """Carte chance : ajoute ou retire un nombre aléatoire de points"""

    def valeur(self, joueur):
        points = random.randint(-5, 15)
        joueur.ajouter_score(points)
        return f'Carte Chance + {points} points'

# ---------- Classe Joueur ----------
class Joueur:
    """Représente un joueur avec un nom et un score"""

    def __init__(self, nom, score=0):
        """
        Initialise un joueur
        :param nom: nom du joueur
        :param score: score initial (par défaut 0)
        """
        self.nom = nom
        self.score = score

    def ajouter_score(self, points):
        """
        Ajoute des points au score du joueur
        param points: nombre de points à ajouter
        """
        self.score += points

    def jouer_carte(self, carte):
        """
        Applique l'effet d'une carte tirée
        :param carte: instance de Carte
        """
        effet = carte.valeur(self)
        print(f'{self.nom} pioche {carte.__class__.__name__} -> {effet}')

    def affichage(self):
        """Affiche le score actuel du joueur"""
        print(f'Score actuel de {self.nom} : {self.score}')


class Tricheur(Joueur):
    """Joueur spécial qui ne subit pas les cartes Malus"""

    def jouer_carte(self, carte):
        """
        Applique l'effet d'une carte
        Si c'est un Malus, le joueur ne perd pas de points
        """
        if isinstance(carte, CarteMalus):
            effet = "Carte Malus ignorée (tricheur)"
            print(f'{self.nom} pioche {carte.__class__.__name__} -> {effet}')
        else:
            super().jouer_carte(carte)  # Joueur normal pour toutes les autres cartes

# ---------- Fonction pour piocher ----------
def piocher(liste_carte, joueur):
    """
    Le joueur pioche la première carte de la liste et applique son effet
    :param liste_carte: liste de cartes
    :param joueur: instance de Joueur
    """
    if not liste_carte:
        print("Plus de cartes à piocher !")
        return

    carte_tiree = liste_carte.pop(0)
    joueur.jouer_carte(carte_tiree)

# ---------- Partie principale ----------
if __name__ == "__main__":
    # Liste de toutes les cartes
    liste_cartes = []

    # Création des joueurs
    joueurs = [Joueur("Léo"), Tricheur("Nico")]

    # Initialisation et mélange des cartes
    Cartes.initialise_et_melange_liste(liste_cartes)

    # Nombre de tours
    NOMBRE_TOURS = 5

    # Boucle des tours
    for tour in range(1, NOMBRE_TOURS + 1):
        print(f'\n=== Tour numéro {tour} ===')
        for joueur_actuel in joueurs:
            piocher(liste_cartes, joueur_actuel)
            joueur_actuel.affichage()
