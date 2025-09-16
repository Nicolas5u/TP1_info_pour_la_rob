print("hello voici l'exo 1 du TP 1")

def distance_robuste(mes1,mes2,mes3) :
    if (mes1 < mes2 < mes3 or mes3 < mes2 < mes1) :
        if (not(0.5 * mes1 < mes2 < 1.5 * mes1) and not(0.5 * mes3 < mes2 < 1.5 * mes3)) : #la médiane est la deuxieme mesure
            return -1 #les valeurs 1,3 sont absurde
        elif (not(0.5 * mes3 < mes2 < 1.5 * mes3)) :
            print("la valeur 3 est absurde")
            return (mes1 + mes2)/2
        elif (not(0.5 * mes1 < mes2 < 1.5 * mes1)) :
            print("la valeur 1 est absurde")
            return (mes2 + mes3)/2
        else :
            return (mes1 + mes2 + mes3)/3
    elif (mes2 < mes3 < mes1 or mes1 < mes3 < mes2) :
        print("la médiane est la troisieme mesure")
        if (not(0.5 * mes1 < mes3 < 1.5 * mes1) and not(0.5 * mes2 < mes3 < 1.5 * mes2)) :
            print("les valeurs 1,2 sont absurde")
            return -1
        elif (not(0.5 * mes2 < mes3 < 1.5 * mes2)) :
            print("la valeur 2 est absurde")
            return (mes1 + mes3)/2
        elif (not(0.5 * mes1 < mes3 < 1.5 * mes1)) :
            print("la valeur 1 est absurde")
            return (mes2 + mes3)/2
        else :
            return (mes1 + mes2 + mes3)/3
    else :
        print("la médiane est la premiere mesure")
        if (not(0.5 * mes3 < mes1 < 1.5 * mes3) and not(0.5 * mes2 < mes1 < 1.5 * mes2)) :
            print("la valeur 3,2 sont absurde")
            return -1
        elif (not(0.5 * mes2 < mes1 < 1.5 * mes2)) :
            print("la valeur 2 est absurde")
            return (mes1 + mes3)/2
        elif (not(0.5 * mes3 < mes1 < 1.5 * mes3)) :
            print("la valeur 3 est absurde")
            return (mes1 + mes2)/2
        else :
            return (mes1 + mes2 + mes3)/3

#assert abs(distance_robuste(2.0, 2.1, 1.9) - 2.0) < 0.1
#assert abs(distance_robuste(2.0, 2.1, 15.0) - 2.05) < 0.1
#assert distance_robuste(1.0, 15.0, 20.0) == 17.5
#assert distance_robuste(1.0, 15.0, 30.0) == -1