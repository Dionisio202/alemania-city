import random
import math
import matplotlib.pyplot as plt

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

# Función que genera un vecino aleatorio moviendo una reina a una fila diferente
def generar_vecino(tablero):
    vecino = tablero[:]
    col = random.randint(0, len(tablero) - 1)  # Selecciona una columna aleatoria
    fila_nueva = random.randint(0, len(tablero) - 1)  # Selecciona una fila aleatoria dentro de la columna
    while fila_nueva == vecino[col]:  # Asegurarse de que se mueve a una fila diferente
        fila_nueva = random.randint(0, len(tablero) - 1)
    vecino[col] = fila_nueva
    return vecino

# Algoritmo de temple simulado para las 8 reinas con criterios de parada adaptativos
def temple_simulado_8_reinas(temperatura_inicial, tasa_enfriamiento, temperatura_umbral=0.1):
    # Generar un estado inicial aleatorio (un tablero con 8 reinas)
    tablero_actual = generar_tablero_inicial()
    heuristica_actual = calcular_heuristica(tablero_actual)
    
    mejor_tablero = tablero_actual[:]
    mejor_heuristica = heuristica_actual
    
    temperatura = temperatura_inicial
    iteracion = 0  # Contador de iteraciones (solo para monitoreo, no para detener el bucle)

    # Bucle controlado por la temperatura y la heurística
    while temperatura > temperatura_umbral and mejor_heuristica > 0:
        iteracion += 1

        # Generar un vecino aleatorio del estado actual
        tablero_vecino = generar_vecino(tablero_actual)
        heuristica_vecino = calcular_heuristica(tablero_vecino)
        
        # Calcular la diferencia de heurística entre el vecino y el actual
        delta_heuristica = heuristica_vecino - heuristica_actual
        
        # Decidir si aceptar el vecino usando la fórmula de Boltzmann
        if delta_heuristica < 0 or random.random() < math.exp(-delta_heuristica / temperatura):
            tablero_actual = tablero_vecino[:]
            heuristica_actual = heuristica_vecino
            
            # Actualizar la mejor solución encontrada
            if heuristica_vecino < mejor_heuristica:
                mejor_tablero = tablero_vecino[:]
                mejor_heuristica = heuristica_vecino

        # Enfriar la temperatura
        temperatura *= tasa_enfriamiento

        # Mostrar progreso con el tablero en cada iteración en formato lista
        print(f"Iteración {iteracion}: Tablero = {tablero_actual}, Heurística actual = {heuristica_actual}, Temperatura = {temperatura:.4f}")

    print(f"Deteniendo el algoritmo. Temperatura alcanzada: {temperatura:.4f}, Heurística actual: {heuristica_actual}")
    return mejor_tablero, mejor_heuristica

# Función para graficar el tablero de las 8 reinas
def graficar_tablero(tablero):
    fig, ax = plt.subplots()
    n = len(tablero)

    # Dibujar el tablero de ajedrez
    for row in range(n):
        for col in range(n):
            # Colorear cuadros de ajedrez
            if (row + col) % 2 == 0:
                color = 'white'
            else:
                color = 'gray'
            ax.add_patch(plt.Rectangle((col, row), 1, 1, color=color))

    # Colocar las reinas en el tablero
    for col in range(n):
        row = tablero[col]
        ax.text(col + 0.5, row + 0.5, '♕', fontsize=30, ha='center', va='center', color='black' if (row + col) % 2 == 0 else 'white')

    # Ajustes finales del gráfico
    ax.set_xlim(0, n)
    ax.set_ylim(0, n)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title("Tablero de las 8 Reinas - Temple Simulado")
    plt.gca().invert_yaxis()  # Invertir el eje y para que 0,0 esté en la esquina inferior
    plt.show()

def ejecutar_temple():

# Parámetros del algoritmo
    temperatura_inicial = 1000 # Temperatura inicial alta para permitir exploración
    tasa_enfriamiento = 0.95   # Factor de enfriamiento (entre 0 y 1)
    temperatura_umbral = 0.000000001   # Temperatura mínima antes de detener el algoritmo

    # Ejecutar el algoritmo de temple simulado
    solucion, heuristica_final = temple_simulado_8_reinas(temperatura_inicial, tasa_enfriamiento, temperatura_umbral)

    # Mostrar resultado final
    print("\n--- Resultado Final ---")
    print(f"Tablero final = {solucion}")
    print("Número de ataques restantes (Heurística final):", heuristica_final)

    # Graficar el tablero final
    graficar_tablero(solucion)
