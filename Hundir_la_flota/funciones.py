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
    proa_fila = np.random.randint(0, 11 - eslora)
    proa_col = np.random.randint(0, 11 - eslora)
    voh = np.random.choice(("a","b")) # un random con dos salidas para elegir si el barco sera horizontal o vertical.
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
                print("gnerando de nuevo")
                crear_flota()
    coordenadas_vistas = set()
    repetidas = set()

    for barco in flota:
        for coor in barco:
            if coor in coordenadas_vistas:
                repetidas.add(coor)
            coordenadas_vistas.add(coor)

    if repetidas:
        crear_flota()
        
    
    
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

















