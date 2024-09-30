import random
import matplotlib.pyplot as plt

def calcular_heuristica(tablero):
    ataques = 0
    n = len(tablero)
    for i in range(n):
        for j in range(i + 1, n):
            if tablero[i] == tablero[j]:
                ataques += 1
            if abs(tablero[i] - tablero[j]) == abs(i - j):
                ataques += 1
    return ataques

def generar_tablero_inicial(n=8):
    return [random.randint(0, n - 1) for _ in range(n)]

def ascenso_de_colinas():
    tablero = generar_tablero_inicial()
    heuristica_actual = calcular_heuristica(tablero)
    historial_movimientos = [(tablero[:], heuristica_actual)]  

    print("Estado inicial:", tablero, "| Ataques:", heuristica_actual)
    
    while True:
        vecino_mejorado = False
        for col in range(len(tablero)):
            mejor_fila = tablero[col]
            mejor_heuristica = heuristica_actual
            
            print(f"\nEvaluando columna {col} con reina en fila {tablero[col]}:")

            for fila in range(len(tablero)):
                if fila == tablero[col]:  
                    continue
                
                nuevo_tablero = list(tablero)
                nuevo_tablero[col] = fila
                nueva_heuristica = calcular_heuristica(nuevo_tablero)
                
                print(f"  - Mover a fila {fila} -> Tablero: {nuevo_tablero} | Heurística: {nueva_heuristica}")

                if nueva_heuristica < mejor_heuristica:
                    mejor_fila = fila
                    mejor_heuristica = nueva_heuristica
                    vecino_mejorado = True
            
            tablero[col] = mejor_fila
            heuristica_actual = mejor_heuristica

        historial_movimientos.append((tablero[:], heuristica_actual))
        print(f"Estado actual del tablero después de evaluar todas las columnas: {tablero} | Ataques: {heuristica_actual}")

        if not vecino_mejorado:
            break
    
    return tablero, heuristica_actual, historial_movimientos

def graficar_tablero(tablero):
    fig, ax = plt.subplots()
    n = len(tablero)

    for row in range(n):
        for col in range(n):
            if (row + col) % 2 == 0:
                color = 'white'
            else:
                color = 'gray'
            ax.add_patch(plt.Rectangle((col, row), 1, 1, color=color))

    for col in range(n):
        row = tablero[col]
        ax.text(col + 0.5, row + 0.5, '♕', fontsize=30, ha='center', va='center', color='black' if (row + col) % 2 == 0 else 'white')

    ax.set_xlim(0, n)
    ax.set_ylim(0, n)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title("Tablero de las 8 Reinas")
    plt.gca().invert_yaxis()  
    plt.show()

def ejecutar_asencso():
    solucion, ataques_restantes, historial = ascenso_de_colinas()

    print("\n--- Historial de Movimientos ---")
    for paso, (tablero, ataques) in enumerate(historial):
        print(f"Paso {paso}: Tablero = {tablero} | Ataques = {ataques}")

    print("\n--- Resultado Final ---")
    print("Tablero final:", solucion)
    print("Número de ataques restantes:", ataques_restantes)

    graficar_tablero(solucion)
