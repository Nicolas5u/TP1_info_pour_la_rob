print("hello voici l'exo 1 du TP 1")

from math import sqrt

def distance_robuste(mes1,mes2,mes3) :

    if (mes1 < mes2 < mes3 or mes3 < mes2 < mes1) :                                        #la médiane est la deuxieme mesure
        return mediane_au_milieu (mes1,mes2,mes3)

    elif (mes2 < mes3 < mes1 or mes1 < mes3 < mes2) :
        return mediane_au_milieu (mes1,mes3,mes2)
    else :
        return mediane_au_milieu (mes2,mes1,mes3)
        
def mediane_au_milieu (mes1,mes2,mes3) :

    if (not(0.5 * mes1 < mes2 < 1.5 * mes1) and not(0.5 * mes3 < mes2 < 1.5 * mes3)) : #les valeurs 1,3 sont absurde
        return -1
    elif (not(0.5 * mes3 < mes2 < 1.5 * mes3)) :                                       # la valeur 3 est absurde
        return (mes1 + mes2)/2
    elif (not(0.5 * mes1 < mes2 < 1.5 * mes1)) :                                       # la valeur 1 est absurde
        return (mes2 + mes3)/2
    else :                                                                             # les valeurs 1 sont bonnes
        return (mes1 + mes2 + mes3)/3

#assert abs(distance_robuste(2.0, 2.1, 1.9) - 2.0) < 0.1
#assert abs(distance_robuste(2.0, 2.1, 15.0) - 2.05) < 0.1
#assert distance_robuste(1.0, 15.0, 20.0) == 17.5
#assert distance_robuste(1.0, 15.0, 30.0) == -1

def cout_deplacement(x,z,e,y,type_terrain) : #calcule le coût énergétique d’un déplacement en fonction du type de terrain.

    if(type_terrain == 'R') :
        return sqrt((y - x)**2 + (e - z)**2)
    if(type_terrain == 'H') :
        return (sqrt((y - x)**2 + (e - z)**2)) * 1.5
    if(type_terrain == 'S') :
        return (sqrt((y - x)**2 + (e - z)**2)) * 2.0
    if(type_terrain == 'O') :
        return (sqrt((y - x)**2 + (e - z)**2)) * 3.0

assert cout_deplacement(0, 0, 5, 0, 'R') == 5.0 # Route horizontale
assert cout_deplacement(0, 0, 3, 4, 'H') == 7.5 # Herbe, distance=5, cout=5*1.5
assert cout_deplacement(0, 0, 0, 2, 'S') == 4.0 # Sable vertical
assert cout_deplacement(1, 1, 1, 1, 'O') == 0.0 # Pas de mouvement

"""
Pour la planification de mission, implémenter temps_trajet qui estime le temps nécessaire pour un déplacement
en tenant compte de la vitesse variable du robot selon le terrain.
Vitesses par terrain : Route=2.0 m/s, Herbe=1.5 m/s, Sable=1.0 m/s, Roche=0.5 m/s
assert temps_trajet(0, 0, 6, 8, ’R’) == 5.0 # 10m à 2m/s = 5s
assert temps_trajet(0, 0, 3, 4, ’S’) == 5.0 # 5m à 1m/s = 5s
assert temps_trajet(0, 0, 0, 1, ’O’) == 2.0 # 1m à 0.5m/s = 2s"""

def distance(a,b,c,d) :
    return sqrt((d - a)**2 + (c - b)**2)

def temps_trajet(a,b,c,d,type_terrain) : # estime le temps nécessaire pour un déplacement en tenant compte de la vitesse variable du robot selon le terrain.
    dist = distance(a,b,c,d)
    if(type_terrain == 'R') :
        return dist / 2.0
    if(type_terrain == 'H') :
        return dist / 1.5
    if(type_terrain == 'S') :
        return dist
    if(type_terrain == 'O') :
        return dist / 0.5
    
assert temps_trajet(0, 0, 6, 8, 'R') == 5.0 # 10m à 2m/s = 5s
assert temps_trajet(0, 0, 3, 4, 'S') == 5.0 # 5m à 1m/s = 5s
assert temps_trajet(0, 0, 0, 1, 'O') == 2.0 # 1m à 0.5m/s = 2s