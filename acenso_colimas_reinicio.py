import matplotlib.pyplot as plt
from ascenso_colimas import ascenso_de_colinas  # Importar la función de ascenso de colinas

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
    ax.set_title("Tablero de las 8 Reinas - Mejor Solución")
    plt.gca().invert_yaxis()  # Invertir el eje y para que 0,0 esté en la esquina inferior
    plt.show()

def reinicio_aleatorio_ascenso_colinas(n_reinicios=4):
    mejor_tablero = None  # Variable para almacenar el mejor tablero encontrado
    mejor_heuristica = 28 # Heurística inicial (infinitamente grande para facilitar comparación)
    mejor_reinicio = -1  # Variable para almacenar el número de reinicio de la mejor solución

    # Almacenar el historial de todos los reinicios
    historial_reinicios = []

    # Ejecutar el ascenso de colinas múltiples veces desde diferentes puntos iniciales
    for reinicio in range(n_reinicios):
        print(f"\nReinicio {reinicio + 1}")

        # Ejecutar el ascenso de colinas para obtener una solución y la heurística actual
        solucion, heuristica_actual, historial = ascenso_de_colinas()

        # Almacenar el historial del reinicio
        historial_reinicios.append({
            "reinicio": reinicio + 1,
            "tablero_final": solucion,
            "heuristica": heuristica_actual,
            "historial": historial
        })

        print(f"Solución final del reinicio {reinicio + 1}: {solucion} con {heuristica_actual} ataques")

        # Si encontramos una mejor solución (menor número de ataques), la actualizamos
        if heuristica_actual < mejor_heuristica:
            mejor_tablero = solucion
            mejor_heuristica = heuristica_actual
            mejor_reinicio = reinicio + 1  # Guardar el número de reinicio de la mejor solución

    # Mostrar la mejor solución encontrada en todos los reinicios
    print("\n--- Mejor Solución Global ---")
    print(f"Tablero final: {mejor_tablero}")
    print(f"Menor número de ataques restantes: {mejor_heuristica}")
    print(f"Mejor solución encontrada en el reinicio: {mejor_reinicio}")

    # Mostrar el historial de cada reinicio con sus soluciones finales y número de ataques
    print("\n--- Historial de todos los reinicios ---")
    for reinicio in historial_reinicios:
        print(f"\nReinicio {reinicio['reinicio']}:")
        for paso, (tablero, ataques) in enumerate(reinicio['historial']):
            print(f"  Paso {paso}: Tablero = {tablero} | Ataques = {ataques}")
        print(f"  Solución final del reinicio {reinicio['reinicio']}: {reinicio['tablero_final']} con {reinicio['heuristica']} ataques")

    # Graficar la mejor solución encontrada
    if mejor_tablero is not None:
        graficar_tablero(mejor_tablero)

    return mejor_tablero, mejor_heuristica, mejor_reinicio


# Ejecutar la función con los valores predeterminados
def ejecutar_reinicio_aleatorio_colinas():
    reinicio_aleatorio_ascenso_colinas()
