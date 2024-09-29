import random

# Función que calcula la heurística: número de ataques entre reinas
def calcular_heuristica(tablero):
    ataques = 0
    n = len(tablero)
    for i in range(n):
        for j in range(i + 1, n):
            # Mismo fila
            if tablero[i] == tablero[j]:
                ataques += 1
            # Misma diagonal
            if abs(tablero[i] - tablero[j]) == abs(i - j):
                ataques += 1
    return ataques

# Función para generar un tablero inicial con una reina en cada columna
def generar_tablero_inicial(n=8):
    return [random.randint(0, n - 1) for _ in range(n)]

# Función de ascenso de colinas
def ascenso_de_colinas():
    # Inicializar el tablero
    tablero = generar_tablero_inicial()
    heuristica_actual = calcular_heuristica(tablero)
    historial_movimientos = [(tablero[:], heuristica_actual)]  # Guardar estado inicial

    print("Estado inicial:", tablero, "| Ataques:", heuristica_actual)
    
    while True:
        vecino_mejorado = False
        # Probar mover cada reina dentro de su columna y encontrar la mejor posición
        for col in range(len(tablero)):
            mejor_fila = tablero[col]
            mejor_heuristica = heuristica_actual
            
            print(f"\nEvaluando columna {col} con reina en fila {tablero[col]}:")

            # Mover la reina a todas las posibles filas dentro de su columna y calcular la heurística
            for fila in range(len(tablero)):
                if fila == tablero[col]:  # Si está en la misma fila, no moverse
                    continue
                
                # Mover a una nueva fila
                nuevo_tablero = list(tablero)
                nuevo_tablero[col] = fila
                nueva_heuristica = calcular_heuristica(nuevo_tablero)
                
                # Imprimir la evaluación de cada posición
                print(f"  - Mover a fila {fila} -> Tablero: {nuevo_tablero} | Heurística: {nueva_heuristica}")

                # Si encontramos una mejor posición, actualizar
                if nueva_heuristica < mejor_heuristica:
                    mejor_fila = fila
                    mejor_heuristica = nueva_heuristica
                    vecino_mejorado = True
            
            # Mover la reina a la mejor posición encontrada en esta columna
            tablero[col] = mejor_fila
            heuristica_actual = mejor_heuristica

        # Guardar el movimiento y el estado actual
        historial_movimientos.append((tablero[:], heuristica_actual))
        print(f"Estado actual del tablero después de evaluar todas las columnas: {tablero} | Ataques: {heuristica_actual}")

        # Verificar si hemos alcanzado un óptimo local
        if not vecino_mejorado:
            break
    
    return tablero, heuristica_actual, historial_movimientos

solucion, ataques_restantes, historial = ascenso_de_colinas()


print("\n--- Historial de Movimientos ---")
for paso, (tablero, ataques) in enumerate(historial):
    print(f"Paso {paso}: Tablero = {tablero} | Ataques = {ataques}")


print("\n--- Resultado Final ---")
print("Tablero final:", solucion)
print("Número de ataques restantes:", ataques_restantes)


print("\n-######################################################################################################")
