#  Calculamos la temperatura promedio de la ciudad de quito, guayaquil y cuenca, en un período de tiempo nuetra función va ser capaz de manejar datos de temperaturas de múltiples ciudades y semanas
temperaturas = [
    [
        [22, 23, 24, 25, 26, 27, 28],  # Quito, Semana 1
        [24, 25, 26, 27, 28, 29, 30],  # Quito, Semana 2
        [26, 27, 28, 29, 30, 31, 32]   # Quito, Semana 3
    ],
    [
        [28, 29, 30, 31, 32, 33, 34],  # Guayaquil, Semana 1
        [30, 31, 32, 33, 34, 35, 36],  # Guayaquil, Semana 2
        [32, 33, 34, 35, 36, 37, 38]   # Guayaquil, Semana 3
    ],
    [
        [20, 21, 22, 23, 24, 25, 26],  # Cuenca, Semana 1
        [22, 23, 24, 25, 26, 27, 28],  # Cuenca, Semana 2
        [24, 25, 26, 27, 28, 29, 30]   # Cuenca, Semana 3
    ]
]
# Definimos las ciudades y semanas para verificar la temparatura
ciudades = ['Quito', 'Guayaquil', 'Cuenca']
semanas = ['Semana 1', 'Semana 2', 'Semana 3']

# Calculamos el promedio de temperaturas para cada ciudad y semana
for i, ciudad in enumerate(ciudades):
    for j, semana in enumerate(semanas):
        promedio = sum(temperaturas[i][j]) / len(temperaturas[i][j])
        print(f'Promedio de temperaturas en {ciudad} durante la {semana}: {promedio:.2f}°C')