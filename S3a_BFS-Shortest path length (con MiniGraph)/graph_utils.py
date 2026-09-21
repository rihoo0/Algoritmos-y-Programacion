import minigraph as nx


def build_graph(edges_list, num_nodes, num_edges):
    """
    Construye un grafo no dirigido y sin pesos utilizando MiniGraph.

    Parámetros:
        edges_list: lista de num_edges cadenas con los extremos de cada
            arista separados por espacios, por ejemplo, "1 4".
        num_nodes: número de vértices, numerados desde 1 hasta num_nodes.
        num_edges: número de aristas de la entrada.

    Devuelve:
        Un grafo nx.Graph con todos los vértices y las aristas indicadas.
        Debe incluir también los vértices que no tengan aristas.
        Los extremos de las aristas deben convertirse a enteros.

    No lee entrada ni imprime resultados; main.py gestiona la E/S
    """

   # ...
    graph = nx.Graph()
    
        # Añade aquí todos los vértices desde 1 hasta num_nodes.
    for i in range(1, num_nodes + 1):
        graph.add_node(i)
        
        # Recorre edges_list, separa cada línea en dos extremos u y v, 
    for edge in edges_list:
        arista = edge.split()
        graph.add_edge(int(arista[0]), int(arista[1]))
    return graph