import random
import matplotlib.pyplot as plt

def calcular_conflictos(tablero):
    conflictos = 0
    n = len(tablero)
    for i in range(n):
        for j in range(i + 1, n):
            if tablero[i] == tablero[j]:
                conflictos += 1
            elif abs(tablero[i] - tablero[j]) == abs(i - j):
                conflictos += 1
    return conflictos

def generar_vecino(tablero):
    n = len(tablero)
    nuevo_tablero = list(tablero)
    col = random.randint(0, n - 1)
    fila = random.randint(0, n - 1)
    nuevo_tablero[col] = fila
    return nuevo_tablero

def ascenso_estocastico(n=8, max_iteraciones=1000):
    
    estado_actual = [random.randint(0, n - 1) for _ in range(n)]
    conflictos_actuales = calcular_conflictos(estado_actual)

    for iteracion in range(max_iteraciones):

        if conflictos_actuales == 0:
            print(f"Solución encontrada en la iteración {iteracion}")
            return estado_actual

        vecino = generar_vecino(estado_actual)
        conflictos_vecino = calcular_conflictos(vecino)

        if conflictos_vecino < conflictos_actuales or random.random() < 0.1:
            estado_actual = vecino
            conflictos_actuales = conflictos_vecino

        print(f"Iteración {iteracion}: {estado_actual} con {conflictos_actuales} conflictos")

    print("No se encontró una solución óptima en las iteraciones dadas.")
    return estado_actual 

def graficar_tablero(tablero):
    n = len(tablero)

    fig, ax = plt.subplots()
    ax.set_xticks(range(n))
    ax.set_yticks(range(n))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.grid(True)
    
    for i in range(n):
        for j in range(n):
            
            color = 'white' if (i + j) % 2 == 0 else 'gray'
            ax.add_patch(plt.Rectangle((j, i), 1, 1, color=color))
    
    for col, row in enumerate(tablero):
        plt.text(col + 0.5, row + 0.5, '♕', fontsize=36, ha='center', va='center', color='black')
    
    ax.set_xlim(0, n)
    ax.set_ylim(0, n)
    plt.gca().invert_yaxis() 
    plt.title('Tablero de las 8 Reinas')
    plt.show()

def ejecutar_ascenso_est():

    solucion = ascenso_estocastico(n=8, max_iteraciones=1000)

    if solucion:
        graficar_tablero(solucion)
    else:
        print("No se encontró una solución óptima.")
