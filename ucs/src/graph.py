from collections import defaultdict
from src.node import Node

class Graph:

    # Constructor
    def __init__(self):
        self.__graph = {}

    @property
    def graph(self):
        return self.__graph

    # Adição de novo nó ao grafo caso ele ainda não exista
    def addNode(self, node):
        if node not in self.__graph:
            self.__graph[node] = Node(node)

    # Recuperando determinado nó do grafo
    def node(self, node):
        return self.__graph[str(node)]

    # Recuperando lista de nós do grafo
    def nodes(self):
        return list(self.__graph.keys())

    # Adicionando conexões entre os nós
    def addEdge(self, n, c, weight):
        if n not in self.__graph:
            self.__graph[n] = Node(n)

        if c not in self.__graph:
            self.__graph[c] = Node(c)

        node = self.node(n)
        node.addConnection(self.node(c), weight)

    # Recuperando todas as conexões
    def edges(self):
        edges = []
        for node in self.__graph:
            for neighbour in self.__graph[node].connections:
                if (node, neighbour['connection'].value) not in edges:
                     edges.append((node, neighbour['connection'].value))
        return edges