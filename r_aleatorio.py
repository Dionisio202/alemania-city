import random

# Función para calcular el número de conflictos en el tablero
def calcular_conflictos(tablero):
    conflictos = 0
    n = len(tablero)
    for i in range(n):
        for j in range(i + 1, n):
            if tablero[i] == tablero[j]:  # Misma fila
                conflictos += 1
            elif abs(tablero[i] - tablero[j]) == abs(i - j):  # Misma diagonal
                conflictos += 1
    return conflictos

# Generar un estado vecino al mover una reina a una nueva fila aleatoria en su columna
def generar_vecino(tablero):
    n = len(tablero)
    nuevo_tablero = list(tablero)
    col = random.randint(0, n - 1)  # Seleccionar una columna aleatoria
    fila = random.randint(0, n - 1)  # Seleccionar una fila aleatoria
    nuevo_tablero[col] = fila  # Mover la reina a la nueva fila en la misma columna
    return nuevo_tablero

# Función para calcular las probabilidades basadas en los conflictos de los vecinos
def calcular_probabilidades(vecinos, total_conflictos):
    probabilidades = [(total_conflictos - conflictos) / total_conflictos for _, conflictos in vecinos]
    total_probabilidades = sum(probabilidades)
    probabilidades_normalizadas = [p / total_probabilidades for p in probabilidades]
    return probabilidades_normalizadas

# Selección de un vecino basado en las probabilidades calculadas
def seleccionar_vecino_aleatorio(vecinos, probabilidades):
    return random.choices(vecinos, weights=probabilidades, k=1)[0]

# Algoritmo de ascenso estocástico con reinicio aleatorio para las 8 reinas
def ascenso_estocastico_reinicio_aleatorio(n=8, max_iteraciones=1000, num_reinicios=10):
    mejor_solucion = None
    menor_numero_conflictos = float('inf')  # Un valor alto para comparar

    for reinicio in range(num_reinicios):
        # Generar una solución inicial aleatoria para cada reinicio
        estado_actual = [random.randint(0, n - 1) for _ in range(n)]
        conflictos_actuales = calcular_conflictos(estado_actual)

        # Calcular el número total de conflictos posibles (C(n, 2) = n*(n-1)/2)
        total_conflictos = n * (n - 1) // 2

        for iteracion in range(max_iteraciones):
            # Si no hay conflictos, se ha encontrado una solución
            if conflictos_actuales == 0:
                print(f"Solución encontrada en la iteración {iteracion} del reinicio {reinicio}")
                return estado_actual

            # Generar una lista de vecinos y sus conflictos
            vecinos = [generar_vecino(estado_actual) for _ in range(10)]  # Generar 10 vecinos aleatorios
            conflictos_vecinos = [(vecino, calcular_conflictos(vecino)) for vecino in vecinos]

            # Calcular las probabilidades basadas en los conflictos de los vecinos
            probabilidades = calcular_probabilidades(conflictos_vecinos, total_conflictos)

            # Seleccionar un vecino aleatorio basado en las probabilidades calculadas
            vecino_seleccionado, conflictos_vecino_seleccionado = seleccionar_vecino_aleatorio(conflictos_vecinos, probabilidades)

            # Moverse al vecino seleccionado
            estado_actual = vecino_seleccionado
            conflictos_actuales = conflictos_vecino_seleccionado

        # Actualizar la mejor solución global
        if conflictos_actuales < menor_numero_conflictos:
            mejor_solucion = estado_actual
            menor_numero_conflictos = conflictos_actuales

        print(f"Reinicio {reinicio}: Mejor solución actual con {menor_numero_conflictos} conflictos")

    print("No se encontró una solución óptima, pero se encontró la mejor solución posible con reinicio aleatorio.")
    return mejor_solucion

# Ejecutar el algoritmo para el problema de las 8 reinas con reinicio aleatorio
solucion = ascenso_estocastico_reinicio_aleatorio(n=8, max_iteraciones=100000, num_reinicios=10000)
print("\nSolución Final:", solucion)