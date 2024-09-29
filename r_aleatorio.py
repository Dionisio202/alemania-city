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

# Algoritmo de ascenso estocástico para las 8 reinas
def ascenso_estocastico(n=8, max_iteraciones=1000):
    # Generar una solución inicial aleatoria
    estado_actual = [random.randint(0, n - 1) for _ in range(n)]
    conflictos_actuales = calcular_conflictos(estado_actual)

    for iteracion in range(max_iteraciones):
        # Si no hay conflictos, se ha encontrado una solución
        if conflictos_actuales == 0:
            print(f"Solución encontrada en la iteración {iteracion}")
            return estado_actual

        # Generar un vecino aleatorio
        vecino = generar_vecino(estado_actual)
        conflictos_vecino = calcular_conflictos(vecino)

        # Si el vecino tiene menos conflictos, moverse a ese vecino
        if conflictos_vecino < conflictos_actuales or random.random() < 0.1:
            estado_actual = vecino
            conflictos_actuales = conflictos_vecino

        # Imprimir estado intermedio y número de conflictos
        print(f"Iteración {iteracion}: {estado_actual} con {conflictos_actuales} conflictos")

    print("No se encontró una solución óptima en las iteraciones dadas.")
    return None

# Ejecutar el algoritmo para el problema de las 8 reinas
solucion = ascenso_estocastico(n=8, max_iteraciones=1000)
print("\nSolución Final:", solucion)