import minigraph  as nx
from sys          import maxsize as infinite
from simple_queue import *


def bfs_path_length(graph, first_node):
    """
    Calcula las distancias mínimas desde first_node mediante BFS.

    Parámetros:
        graph: grafo no dirigido y sin pesos de MiniGraph.
        first_node: vértice de origen, perteneciente al grafo.

    Devuelve:
        Un diccionario {vertice: distancia_en_aristas} para todos los
        vértices del grafo. La distancia del origen es 0 y la de los
        vértices no alcanzables es infinite (sys.maxsize).

    Utiliza la clase Queue de simple_queue.py.
    No lee entrada ni imprime resultados; main.py gestiona la E/S.
    """


    distance = {}                 # Diccionario con la distancia desde 
                                  # firstNode al resto de los nodos.
    for node in graph.nodes():
        distance[node] = infinite

    # solve it here!
    # ...
    obj = Queue()
    distance[first_node] = 0
    obj.enqueue(first_node)

    while not obj.isEmpty():    #Mientras la cola no este vacia
        u = obj.dequeue()   #Se saca el primer elemento de la cola
        for v in graph.neighbors(u):    #Miramos los vecinos del nodo u
            if distance[v] == infinite: #Si la distancia es igual a infinito, es decir, no ha sido visitado
                distance[v] = distance[u] + 1   #Se dice que la distancia del nodo v es la distancia del nodo u + 1
                obj.enqueue(v)  #Se añade el nodo v a la cola para seguir explorando sus vecinos

    return distance
