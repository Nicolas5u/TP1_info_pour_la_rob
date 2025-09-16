print("hello voici l'exo 1 du TP 1")

from math import sqrt

# Entrées : mes1, mes2, mes3 (float)
# Sortie : (float) distance robuste ou -1 si incohérente
# Rôle : Détermine une distance fiable à partir de trois mesures, en éliminant les valeurs aberrantes
def distance_robuste(mes1, mes2, mes3) -> float:

    if (mes1 < mes2 < mes3 or mes3 < mes2 < mes1):                                     # la médiane est la deuxième mesure
        return mediane_au_milieu(mes1, mes2, mes3)

    elif (mes2 < mes3 < mes1 or mes1 < mes3 < mes2):                                   # la médiane est la troisième mesure
        return mediane_au_milieu(mes1, mes3, mes2)

    else:                                                                              # la médiane est la première mesure
        return mediane_au_milieu(mes2, mes1, mes3)


# Entrées : mes1, mes2, mes3 (float)
# Sortie : (float) distance moyenne ou -1 si incohérente
# Rôle : Vérifie la cohérence des mesures et calcule une estimation fiable
def mediane_au_milieu(mes1, mes2, mes3) -> float:

    if (not(0.5 * mes1 < mes2 < 1.5 * mes1) and not(0.5 * mes3 < mes2 < 1.5 * mes3)):  # les valeurs 1,3 sont absurdes
        return -1
    elif (not(0.5 * mes3 < mes2 < 1.5 * mes3)):                                        # la valeur 3 est absurde
        return (mes1 + mes2) / 2
    elif (not(0.5 * mes1 < mes2 < 1.5 * mes1)):                                        # la valeur 1 est absurde
        return (mes2 + mes3) / 2
    else:                                                                              # les trois valeurs sont bonnes
        return (mes1 + mes2 + mes3) / 3


# Entrées : x, z, e, y (float), type_terrain (str)
# Sortie : (float) coût énergétique
# Rôle : Calcule le coût énergétique d’un déplacement en fonction du type de terrain
def cout_deplacement(x, z, e, y, type_terrain) -> float:

    if type_terrain == 'R':
        return sqrt((y - x)**2 + (e - z)**2)
    if type_terrain == 'H':
        return sqrt((y - x)**2 + (e - z)**2) * 1.5
    if type_terrain == 'S':
        return sqrt((y - x)**2 + (e - z)**2) * 2.0
    if type_terrain == 'O':
        return sqrt((y - x)**2 + (e - z)**2) * 3.0


assert cout_deplacement(0, 0, 5, 0, 'R') == 5.0   # Route horizontale
assert cout_deplacement(0, 0, 3, 4, 'H') == 7.5   # Herbe, distance=5, coût=5*1.5
assert cout_deplacement(0, 0, 0, 2, 'S') == 4.0   # Sable vertical
assert cout_deplacement(1, 1, 1, 1, 'O') == 0.0   # Pas de mouvement


# Entrées : a, b, c, d (float)
# Sortie : (float) distance entre les deux points
# Rôle : Calcule la distance euclidienne entre deux points du plan
def distance(a, b, c, d) -> float:
    return sqrt((d - a)**2 + (c - b)**2)


# Entrées : a, b, c, d (float), type_terrain (str)
# Sortie : (float) temps en secondes
# Rôle : Estime le temps nécessaire pour un trajet selon la vitesse du robot et le terrain
def temps_trajet(a, b, c, d, type_terrain) -> float:
    dist = distance(a, b, c, d)
    if type_terrain == 'R':
        return dist / 2.0
    if type_terrain == 'H':
        return dist / 1.5
    if type_terrain == 'S':
        return dist
    if type_terrain == 'O':
        return dist / 0.5


assert temps_trajet(0, 0, 6, 8, 'R') == 5.0  # 10m à 2m/s = 5s
assert temps_trajet(0, 0, 3, 4, 'S') == 5.0  # 5m à 1m/s = 5s
assert temps_trajet(0, 0, 0, 1, 'O') == 2.0  # 1m à 0.5m/s = 2s

