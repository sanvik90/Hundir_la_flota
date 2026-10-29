import numpy as np
import variables as v 
import time

"""
_____________Cosas de tableros
"""

def crear_tablero():
    tablero =np.full((10,10),"🌊")
    return tablero




def crear_barco(eslora):
    voh = np.random.choice(("a", "b"))

    if voh == "a":  # Vertical
        proa_fila = np.random.randint(10 - eslora + 1)
        proa_col = np.random.randint(10)
    else:  # Horizontal
        proa_fila = np.random.randint(10)
        proa_col = np.random.randint(10 - eslora + 1)

    barco = []

    for i in range(eslora):
        if voh == "a":
            barco.append((proa_fila + i, proa_col))
        else:
            barco.append((proa_fila, proa_col + i))

    return barco


def crear_flota():
    flota = []
    for eslora in v.esloras_f:
        flota.append(crear_barco(eslora))
    for barco in flota:
        for coor in barco:
            if 0 < coor[0]>9 or 0 < coor[1]> 9:
                return crear_flota()

    coordenadas_vistas = set()
    repetidas = set()

    for barco in flota:
        for coor in barco:
            if coor in coordenadas_vistas:
                repetidas.add(coor)
            coordenadas_vistas.add(coor)

    if repetidas:
        return crear_flota()
        
    return flota

def colocar_flota(flota,tablero):
    for barco in flota:
        for pos in barco:
            fila, col = pos
            tablero[fila, col] = "🚢" 
    return tablero




def pintar(t_jug_bar, t_jug_dis):
    time.sleep(1)


    print("🏹 🏹 🏹 🏹 🏹 🏹Este es tu panel de disparos 🏹 🏹 🏹 🏹 🏹 🏹 ")
    print(t_jug_dis)
    print()
    time.sleep(0.5)

    print("⚓ ⚓ ⚓ ⚓ ⚓ ⚓ Esto son tus barcos ⚓ ⚓ ⚓ ⚓ ⚓ ⚓")
    print(t_jug_bar)
    print()

    
       

def disparo(t_riv_bar, t_jug_dis, t_jug_bar):

    fila = int(input("Escoge la fila: "))
    columna = int(input("Escoge la columna: "))

    if t_riv_bar[fila][columna] == "🚢":
        t_jug_dis[fila][columna] = "💥"
        time.sleep(1.4)
        print(v.textos_acierto)
        pintar(t_jug_bar, t_jug_dis)
        return disparo(t_riv_bar, t_jug_dis, t_jug_bar)

    else:
        t_jug_dis[fila][columna] = "💨"
        time.sleep(1.4)
        print(v.textos_Fallo)
        pintar(t_jug_bar, t_jug_dis)
        return False


def disparo_maq1(t_jug_bar, t_riv_dis, t_jug_dis):

    fila = np.random.randint(10)
    columna = np.random.randint(10)

    while t_riv_dis[fila, columna] != "🌊":
        fila = np.random.randint(10)
        columna = np.random.randint(10)

    if t_jug_bar[fila, columna] == "🚢":
        t_riv_dis[fila, columna] = "💥"
        t_jug_bar[fila, columna] = "💥"
        time.sleep(1.4)
        print("Nos han dado")
        pintar(t_jug_bar, t_jug_dis)
        return disparo_maq1(t_jug_bar, t_riv_dis, t_jug_dis)

    else:
        t_riv_dis[fila, columna] = "💨"
        t_jug_bar[fila, columna] = "💨"
        time.sleep(1.4)
        print("Han fallado")
        pintar(t_jug_bar, t_jug_dis)
        return False


def crear_lista_impactos(flota):
    impactos = []

    for barco in flota:
        impactos.append([])

    return impactos


def turnos(t_riv_bar, t_jug_dis, t_jug_bar, t_riv_dis):

    turno_jugador = True


    while True:
        if turno_jugador:
            print("Turno Jugador número")
            disparo(t_riv_bar, t_jug_dis, t_jug_bar)
        
            turno_jugador = False
          

        else:
            print("Turno Rival")
            time.sleep(2)
            disparo_maq1(t_jug_bar, t_riv_dis, t_jug_dis)
            turno_jugador = True
        if "🚢" not in t_riv_bar:
            ganador = jugador
            break
            

        if "🚢" not in t_jug_bar:
            ganador = rival
            break





