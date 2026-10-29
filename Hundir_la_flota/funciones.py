import numpy as np
import variables as v 

"""
_____________Cosas de tableros
"""

def crear_tablero():
    tablero =np.full((10,10),"🌊")
    return tablero

"""
_________________creacion de barcos
"""


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

def marcador():
    for i, barco in enumerate(flota):(f"Barco {i + 1}: {len(barco)} esloras")


def cordenadas(flota_rival):
    for i, barco in enumerate(flota_rival):
        print(f"Barco {i + 1}: {len(barco)} esloras")
        print(f"Tipo: {type(barco)}")
        print(f"Contenido: {barco}")


def pintar(t_jug_bar, t_jug_dis):

    print("🗺️ 🗺️ 🗺️ 🗺️ 🗺️ 🗺️ 🗺️ 🗺️ Tableros")
    print()

    print("⚓ ⚓ ⚓ ⚓ ⚓ ⚓ Esto son tus barcos ⚓ ⚓ ⚓ ⚓ ⚓ ⚓")
    print(t_jug_bar)
    print()

  

    print("🏹 🏹 🏹 🏹 🏹 🏹Este es tu panel de disparos 🏹 🏹 🏹 🏹 🏹 🏹 ")
    print(t_jug_dis)
    print()
       

def disparo(t_riv_bar,t_jug_dis):

    try:
        fila = int(input("Fila"))
        columna = int(input("Columna"))
        if t_riv_bar[fila][columna] =="🚢":
            t_jug_dis[fila][columna] ="💥"
            print(v.textos_acierto)
        else:
            t_jug_dis[fila][columna] ="💨"
            print(v.textos_Fallo)
        
    except:
       
        print("Valor no valido")
    return 


def disparo_maq1(t_jug_bar, t_riv_dis):

    fila = np.random.randint(10)
    columna = np.random.randint(10)

    while t_riv_dis[fila, columna] != "🌊":
        fila = np.random.randint(10)
        columna = np.random.randint(10)

    if  t_jug_bar[fila, columna] == "🚢":
        t_riv_dis[fila, columna] = "💥"
        t_jug_bar[fila, columna] = "💥"
        print("Nos han dado!!!!!!!!!")
    else:
        t_riv_dis[fila, columna] = "💨"
        t_jug_bar[fila, columna] = "💨"
        print("Han fallado")
        
    return 


def crear_lista_impactos(flota):
    impactos = []

    for barco in flota:
        impactos.append([])

    return impactos


def turnos(t_riv_bar, t_jug_dis, t_jug_bar, t_riv_dis):

    turno_jugador = True

    while True:
        if turno_jugador:
            print("Turno Jugador")
            disparo(t_riv_bar, t_jug_dis)
            turno_jugador = False
            print(pintar(t_jug_bar, t_jug_dis))

        else:
            print("Turno Rival")
            disparo_maq1(t_jug_bar, t_riv_dis)
            turno_jugador = True
            print(pintar(t_jug_bar, t_jug_dis))






