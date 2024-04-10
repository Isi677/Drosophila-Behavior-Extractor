#Formato Diccionario
#Llave: string con genotipo, sexo, edad
#Contenido del diccionario: lista con los nombres de los excels con coordenadas + numero de moscas por video
excels_coordenadas = {
    "w1118 Macho 3a5": [
        ["Videos/Control-w1118/dp 3-5 Macho w1118/N1", 5],
        ["Videos/Control-w1118/dp 3-5 Macho w1118/N2", 5],
        ["Videos/Control-w1118/dp 3-5 Macho w1118/N3", 5],
        ["Videos/Control-w1118/dp 3-5 Macho w1118/N4", 5],
        ["Videos/Control-w1118/dp 3-5 Macho w1118/N5", 5],
        ["Videos/Control-w1118/dp 3-5 Macho w1118/N6", 5],
        ["Videos/Control-w1118/dp 3-5 Macho w1118/N7", 5], 
        ["Videos/Control-w1118/dp 3-5 Macho w1118/N8", 5]
        ]
}

#Tiempo real de grabacion en segundos
record_time = 300
#Frames totales 
frames_totales = 1050

#Tiempo
tiempo = record_time / frames_totales

#Se debe elegir si aplicar filtro o no de distancia, velocidad y actividad
#Lista de dos valores: Primer valor es booleano: True si hay filtro, False si no hay. Segundo valor es valor para filtrar. 
# Ej: si se elige 0.5, solo se considerara movimiento si mosca se mueve menos de 0.5
filtro_distancia = [True, 0.5]

# Ej: si se elige 0.25, valores de velocidad de 0.25 mm/s se considerará como movimiento de la mosca
#     Solo estos valores se consideraran como actividad, por lo que usarán para calcular la velocidad y aceleracion media
#     Bajo 0.25, se determina que la mosca está detenida o en pausa
filtro_actividad_pausas = 0.25

#Lista: Primer valor es un booleano. Si es True, se calcula preferencia. 
#Segundo valor indica si se quiere calcula la preferencia por derecha-izquierda (1) o arriba-abajo (2) de la arena 
analizar_preferencia = [False, 1]

#Numero de anillo: permite que el usuario determine el número de anillos concentricos de igual área para calcular el centrofobismo
n_rings = 6