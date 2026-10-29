
import funciones as fc
import variables as v
import time

t_riv_bar = fc.crear_tablero()
t_riv_dis = fc.crear_tablero()
t_jug_bar= fc.crear_tablero()
t_jug_dis = fc.crear_tablero()


flota_jugador = fc.crear_flota()
flota_rival = fc.crear_flota()


t_jug_bar = fc.colocar_flota(flota_jugador, t_jug_bar)
t_riv_bar = fc.colocar_flota(flota_rival, t_riv_bar)

print(v.texto_bienvienida)
time.sleep(2)
fc.pintar(t_jug_bar, t_jug_dis)
fc.turnos(t_riv_bar, t_jug_dis, t_jug_bar, t_riv_dis)

