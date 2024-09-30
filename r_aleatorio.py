import matplotlib.pyplot as plt
from a_stocástico import ascenso_estocastico, calcular_conflictos  # Importar las funciones necesarias

# Algoritmo de ascenso estocástico con reinicio aleatorio para las 8 reinas
def ascenso_estocastico_reinicio_aleatorio(num_reinicios=4):
    mejor_solucion = None
    mejor_reinicio = -1  # Almacena el número de reinicio en que se encontró la mejor solución
    menor_numero_conflictos = float('inf')  # Valor alto inicial para comparar

    for reinicio in range(num_reinicios):
        print(f"\nReinicio {reinicio + 1}:")

        # Ejecutar el ascenso estocástico básico para cada reinicio
        solucion = ascenso_estocastico()  # Utilizar la función importada
        conflictos_actuales = calcular_conflictos(solucion)

        print(f"Solución encontrada: {solucion} con {conflictos_actuales} conflictos")

        # Actualizar la mejor solución si se encuentra un estado con menos conflictos
        if conflictos_actuales < menor_numero_conflictos:
            mejor_solucion = solucion
            menor_numero_conflictos = conflictos_actuales
            mejor_reinicio = reinicio + 1  # Almacenar el número de reinicio de la mejor solución

    print("Mejor solución encontrada después de múltiples reinicios:")
    print(f"Solución: {mejor_solucion} con {menor_numero_conflictos} conflictos")
    print(f"Mejor solución encontrada en el reinicio número: {mejor_reinicio}")

    return mejor_solucion, mejor_reinicio

# Función para graficar el tablero de las 8 reinas
def graficar_tablero(tablero, title="Tablero de 8 Reinas"):
    n = len(tablero)
    # Crear una figura y un eje
    fig, ax = plt.subplots()
    ax.set_xticks(range(n))
    ax.set_yticks(range(n))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.grid(True)
    
    # Dibujar el tablero de ajedrez
    for i in range(n):
        for j in range(n):
            # Determinar el color de la celda
            color = 'white' if (i + j) % 2 == 0 else 'gray'
            ax.add_patch(plt.Rectangle((j, i), 1, 1, color=color))
    
    # Colocar las reinas en el tablero
    for col, row in enumerate(tablero):
        plt.text(col + 0.5, row + 0.5, '♕', fontsize=36, ha='center', va='center', color='black')
    
    # Ajustar los límites del tablero
    ax.set_xlim(0, n)
    ax.set_ylim(0, n)
    plt.gca().invert_yaxis()  # Invertir el eje y para que (0,0) esté en la esquina inferior
    plt.title(title)
    plt.show()

# Ejecutar el algoritmo para el problema de las 8 reinas con reinicio aleatorio y graficar el tablero final
solucion, mejor_reinicio = ascenso_estocastico_reinicio_aleatorio(num_reinicios=4)

if solucion:
    print(f"Solución graficada corresponde al reinicio número: {mejor_reinicio}")
    graficar_tablero(solucion, title=f"Solución Final de las 8 Reinas (Reinicio {mejor_reinicio})")
else:
    print("No se encontró una solución óptima.")