
import funciones as fc
import variables as v
t_riv_bar = fc.crear_tablero()
t_riv_dis = fc.crear_tablero()
t_jug_bar= fc.crear_tablero()
t_jug_dis = fc.crear_tablero()


flota_jugador = fc.crear_flota()
flota_rival = fc.crear_flota()

t_jug_bar = fc.colocar_flota(flota_jugador, t_jug_bar)
t_riv_bar = fc.colocar_flota(flota_rival, t_riv_bar)


print("🗺️ 🗺️ 🗺️ 🗺️ 🗺️ 🗺️ 🗺️ 🗺️ Tableros 🗺️ 🗺️ 🗺️ 🗺️ 🗺️ 🗺️ 🗺️ 🗺️")
print("\n")
print("\n")
print("⚓ ⚓ ⚓ ⚓ ⚓ ⚓ ⚓ ⚓ Esto son tus Barcos ⚓ ⚓ ⚓ ⚓ ⚓ ⚓ ⚓ ⚓ ")
print("\n")
print(t_jug_bar)
print("\n")
print(flota_jugador)
print("\n")
print(" 🏹 🏹 🏹 🏹 🏹 🏹 🏹 🏹  Este es tu panel de disparos 🏹 🏹 🏹 🏹 🏹 🏹 🏹 🏹 ")
print("\n")
print(t_jug_dis)
print("\n")
print("barcos____rival")
print(t_riv_bar)
print("juegooo")
fc.disparo_maq1(t_jug_bar,t_riv_dis)
print(t_jug_bar)
