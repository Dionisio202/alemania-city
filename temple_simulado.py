import random
import math
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

def generar_vecino(tablero):
    vecino = tablero[:]
    col = random.randint(0, len(tablero) - 1) 
    fila_nueva = random.randint(0, len(tablero) - 1)  
    while fila_nueva == vecino[col]:  
        fila_nueva = random.randint(0, len(tablero) - 1)
    vecino[col] = fila_nueva
    return vecino

def temple_simulado_8_reinas(temperatura_inicial, tasa_enfriamiento, temperatura_umbral=0.1):
    tablero_actual = generar_tablero_inicial()
    heuristica_actual = calcular_heuristica(tablero_actual)
    
    mejor_tablero = tablero_actual[:]
    mejor_heuristica = heuristica_actual
    
    temperatura = temperatura_inicial
    iteracion = 0  

    while temperatura > temperatura_umbral and mejor_heuristica > 0:
        iteracion += 1

        tablero_vecino = generar_vecino(tablero_actual)
        heuristica_vecino = calcular_heuristica(tablero_vecino)
        
        delta_heuristica = heuristica_vecino - heuristica_actual
        
        if delta_heuristica < 0 or random.random() < math.exp(-delta_heuristica / temperatura):
            tablero_actual = tablero_vecino[:]
            heuristica_actual = heuristica_vecino
            
            if heuristica_vecino < mejor_heuristica:
                mejor_tablero = tablero_vecino[:]
                mejor_heuristica = heuristica_vecino

        temperatura *= tasa_enfriamiento

        print(f"Iteración {iteracion}: Tablero = {tablero_actual}, Heurística actual = {heuristica_actual}, Temperatura = {temperatura:.4f}")

    print(f"Deteniendo el algoritmo. Temperatura alcanzada: {temperatura:.4f}, Heurística actual: {heuristica_actual}")
    return mejor_tablero, mejor_heuristica

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
    ax.set_title("Tablero de las 8 Reinas - Temple Simulado")
    plt.gca().invert_yaxis()  
    plt.show()

def ejecutar_temple():

    temperatura_inicial = 1000 
    tasa_enfriamiento = 0.95   
    temperatura_umbral = 0.000000001   

    solucion, heuristica_final = temple_simulado_8_reinas(temperatura_inicial, tasa_enfriamiento, temperatura_umbral)

    print("\n--- Resultado Final ---")
    print(f"Tablero final = {solucion}")
    print("Número de ataques restantes (Heurística final):", heuristica_final)

    graficar_tablero(solucion)
