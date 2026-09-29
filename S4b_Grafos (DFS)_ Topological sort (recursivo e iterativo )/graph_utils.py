import minigraph as nx

def build_digraph_with_weights(edges_list, num_nodes, num_edges):
    # Añade aqui la rutina que hiciste en el primer ejercicio
    # de esta semana para crear el grafo dirigido con pesos.
    # ...
    graph = nx.DiGraph()

    for i in range(1, num_nodes + 1):
        graph.add_node(i)

    for i in range(num_edges):
        nodes = edges_list[i].split()
        graph.add_edge(int(nodes[0]), int(nodes[1]), weight=int(nodes[2]))
    return graph
