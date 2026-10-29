import numpy as np
import variables as v 
import time


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
    time.sleep(1.6)


    print("🏹 🏹 🏹 🏹 🏹 🏹Este es tu panel de disparos 🏹 🏹 🏹 🏹 🏹 🏹 ")
    print(t_jug_dis)
    print()
    time.sleep(0.5)
    print()
    print("⚓ ⚓ ⚓ ⚓ ⚓ ⚓ Esto son tus barcos ⚓ ⚓ ⚓ ⚓ ⚓ ⚓")
    print(t_jug_bar)
    print()

    
       

def disparo(t_riv_bar, t_jug_dis, t_jug_bar):
    
    
    fila = int(input("Escoge la fila: "))
    if fila == 333:
        print("👁️ 👁️ 👁️ 👁️Superperiscopio activado 👁️ 👁️ 👁️ 👁️")
        print(t_riv_bar)
        return disparo(t_riv_bar, t_jug_dis, t_jug_bar)
    elif fila >10 or fila < -1:
        print("Pero con un valor del 0 al 9, leñe ")
        return disparo(t_riv_bar, t_jug_dis, t_jug_bar)

    columna = int(input("Escoge la columna "))
    if columna >10 or columna < -1:
            print("Pero con un valor del 0 al 9, leñe ")
            return disparo(t_riv_bar, t_jug_dis, t_jug_bar)
    
    if t_riv_bar[fila][columna] == "🚢":
        t_jug_dis[fila][columna] = "💥"
        time.sleep(1.4)
        print(v.textos_acierto)
        time.sleep(0.8)
        print()
        time.sleep(0.7)
        print("🏹 🏹 🏹 🏹 🏹 🏹Este es tu panel de disparos 🏹 🏹 🏹 🏹 🏹 🏹 ")
        time.sleep(0.5)
        print(t_jug_dis)
        print()
        time.sleep(0.5)
        print(f"Has conseguido {np.count_nonzero(t_jug_dis == "💥")} impactos. Te quedan {16 -np.count_nonzero(t_jug_dis == "💥")} ")
        time.sleep(0.4)
        if np.count_nonzero(t_riv_bar == "💥") <= 16:
            disparo(t_riv_bar, t_jug_dis, t_jug_bar)
        else:
            print("¡¡¡¡¡ LO CONSEGUISTE GRUEMETE!!!!!\n has derrotado a la flota rival")
   
        
 

    else:
        t_jug_dis[fila][columna] = "💨"
        time.sleep(1.4)
        print(v.textos_Fallo)
        print()
        time.sleep(0.5)
        print("🏹 🏹 🏹 🏹 🏹 🏹Este es tu panel de disparos 🏹 🏹 🏹 🏹 🏹 🏹 ")
        time.sleep(0.5)
        print(t_jug_dis)
        time.sleep(0.5)
        print(f"Has conseguido {np.count_nonzero(t_jug_dis == "💥")} impactos. Te quedan {16 -np.count_nonzero(t_jug_dis == "💥")} ")
        print()
      
      


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
        print()
        time.sleep(0.5)
        print("⚓ ⚓ ⚓ ⚓ ⚓ ⚓ Esto son tus barcos ⚓ ⚓ ⚓ ⚓ ⚓ ⚓")
        print(t_jug_bar)
        print()
        time.sleep(3)
        if np.count_nonzero(t_jug_bar == "💥") <= 16:
            return disparo_maq1(t_jug_bar, t_riv_dis, t_jug_dis)
        else:
            print("PERDISTE GRUMETE. TODA LA FLOTA ESTA PERDIDA ")

    else:
        t_riv_dis[fila, columna] = "💨"
        t_jug_bar[fila, columna] = "💨"
        time.sleep(1.4)
        print("Han fallado")
        print()
        time.sleep(0.5)
        print("⚓ ⚓ ⚓ ⚓ ⚓ ⚓ Esto son tus barcos ⚓ ⚓ ⚓ ⚓ ⚓ ⚓")
        print(t_jug_bar)
        print()
   
        return False






def turnos(t_riv_bar, t_jug_dis, t_jug_bar, t_riv_dis):
    turno_jugador = True

    while True:
        if np.count_nonzero(t_jug_bar == "💥") >= 16:
            print("PERDISTE GRUMETE. TODA LA FLOTA ESTA PERDIDA ")
            break

        if np.count_nonzero(t_riv_bar == "💥") >= 16:
            break

        if turno_jugador:
            print("Turno Jugador")
            disparo(t_riv_bar, t_jug_dis, t_jug_bar)
            turno_jugador = False

        else:
            print("Turno Rival")
            time.sleep(2)
            disparo_maq1(t_jug_bar, t_riv_dis, t_jug_dis)
            turno_jugador = True
