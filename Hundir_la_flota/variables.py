import  numpy as np

texto_bienvienida = "Despierta, grumete. ¡Es la guerra! \n Nuestro cápitan está indispuesto, y nos estan atacando. \n Necesitamos que vengas urgentemetne al puente de mando.\n ¡ Rápido! "
fallo_1 = "¡Agua!"
fallo_2 = "¡Fallaste!"
fallo_3 = "Si disparar al agua fuese deporte olímpico, serías medalla de oro"
fallo_4 = "Menudo manta estás hecho"
textos_Fallo = np.random.choice((fallo_1,fallo_2,fallo_3,fallo_4))

acierto_1 = "Diana"
acierto_2 = "Bingo"
acierto_3 = "Tocado"
acierto_4 ="Le diste!"
textos_acierto = np.random.choice((acierto_1,acierto_2,acierto_3,acierto_4))


hundido= "Hudido"


tamanio = 10
esloras_f = [4, 3, 3, 2, 2, 2]
jugadores =["Jugador","Rival"]
turno_actual = 0
