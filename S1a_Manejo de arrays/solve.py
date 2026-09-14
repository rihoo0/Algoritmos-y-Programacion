def order_crossover(parent1, parent2, lower_bound, upper_bound):
    """
    Genera un hijo a partir de dos listas padre aplicando el operador
    de cruce de orden (Order Crossover).

    Parámetros:
        parent1: lista padre de la que se debe copiar directamente un segmento.
        parent2: lista madre de la que se deben tomar los elementos restantes.
        lower_bound: índice inicial del segmento que se copia desde parent1.
        upper_bound: índice final no incluido del segmento que se copia desde parent1.

    Restricciones:
        - No leer datos por teclado dentro de esta función.
        - No imprimir resultados dentro de esta función.
        - Devolver la lista hijo resultante.
        - Se asume que parent1 y parent2 tienen la misma longitud.
        - Se asume que ambas listas representan permutaciones compatibles.

    Ejemplo:
        parent1 = [8, 11, 3, 5, 6, 4, 2, 12, 1, 9, 7, 10]
        parent2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        lower_bound = 6
        upper_bound = 9

        Segmento copiado de parent1:
            parent1[6:9] == [2, 12, 1]

        Resultado esperado:
            [4, 5, 6, 7, 8, 9, 2, 12, 1, 10, 11, 3]
    """
    child1 = [None] * len(parent1)
    child1[lower_bound:upper_bound] = parent1[lower_bound:upper_bound]


    parent2_elements = []

    for i in range(upper_bound, len(parent2)):
        if parent2[i] not in child1:
            parent2_elements.append(parent2[i])
    for i in range(0, upper_bound):
        if parent2[i] not in child1:
            parent2_elements.append(parent2[i])
    
    for i in range(upper_bound, len(parent2)):
            child1[i] = parent2_elements.pop(0)
    
    for i in range(0, lower_bound):
         child1[i] = parent2_elements.pop(0)
        
    return child1
