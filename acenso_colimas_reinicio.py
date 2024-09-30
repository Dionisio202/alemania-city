import matplotlib.pyplot as plt
from ascenso_colimas import ascenso_de_colinas  

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
    ax.set_title("Tablero de las 8 Reinas - Mejor Solución")
    plt.gca().invert_yaxis() 
    plt.show()

def reinicio_aleatorio_ascenso_colinas(n_reinicios=4):
    mejor_tablero = None 
    mejor_heuristica = 28 
    mejor_reinicio = -1 

    historial_reinicios = []

    for reinicio in range(n_reinicios):
        print(f"\nReinicio {reinicio + 1}")

        solucion, heuristica_actual, historial = ascenso_de_colinas()

        historial_reinicios.append({
            "reinicio": reinicio + 1,
            "tablero_final": solucion,
            "heuristica": heuristica_actual,
            "historial": historial
        })

        print(f"Solución final del reinicio {reinicio + 1}: {solucion} con {heuristica_actual} ataques")

        if heuristica_actual < mejor_heuristica:
            mejor_tablero = solucion
            mejor_heuristica = heuristica_actual
            mejor_reinicio = reinicio + 1  
    print("\n--- Mejor Solución Global ---")
    print(f"Tablero final: {mejor_tablero}")
    print(f"Menor número de ataques restantes: {mejor_heuristica}")
    print(f"Mejor solución encontrada en el reinicio: {mejor_reinicio}")

    print("\n--- Historial de todos los reinicios ---")
    for reinicio in historial_reinicios:
        print(f"\nReinicio {reinicio['reinicio']}:")
        for paso, (tablero, ataques) in enumerate(reinicio['historial']):
            print(f"  Paso {paso}: Tablero = {tablero} | Ataques = {ataques}")
        print(f"  Solución final del reinicio {reinicio['reinicio']}: {reinicio['tablero_final']} con {reinicio['heuristica']} ataques")

    if mejor_tablero is not None:
        graficar_tablero(mejor_tablero)

    return mejor_tablero, mejor_heuristica, mejor_reinicio


def ejecutar_reinicio_aleatorio_colinas():
    reinicio_aleatorio_ascenso_colinas()
