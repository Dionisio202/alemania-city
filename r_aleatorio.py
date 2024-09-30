import matplotlib.pyplot as plt
from a_stocástico import ascenso_estocastico, calcular_conflictos

def ascenso_estocastico_reinicio_aleatorio(num_reinicios=4):
    mejor_solucion = None
    mejor_reinicio = -1 
    menor_numero_conflictos = float('inf')

    for reinicio in range(num_reinicios):
        print(f"\nReinicio {reinicio + 1}:")

        solucion = ascenso_estocastico()
        conflictos_actuales = calcular_conflictos(solucion)

        print(f"Solución encontrada: {solucion} con {conflictos_actuales} conflictos")

        if conflictos_actuales < menor_numero_conflictos:
            mejor_solucion = solucion
            menor_numero_conflictos = conflictos_actuales
            mejor_reinicio = reinicio + 1  

    print("Mejor solución encontrada después de múltiples reinicios:")
    print(f"Solución: {mejor_solucion} con {menor_numero_conflictos} conflictos")
    print(f"Mejor solución encontrada en el reinicio número: {mejor_reinicio}")

    return mejor_solucion, mejor_reinicio

def graficar_tablero(tablero, title="Tablero de 8 Reinas"):
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
    plt.title(title)
    plt.show()

solucion, mejor_reinicio = ascenso_estocastico_reinicio_aleatorio(num_reinicios=100)

if solucion:
    print(f"Solución graficada corresponde al reinicio número: {mejor_reinicio}")
    graficar_tablero(solucion, title=f"Solución Final de las 8 Reinas (Reinicio {mejor_reinicio})")
else:
    print("No se encontró una solución óptima.")