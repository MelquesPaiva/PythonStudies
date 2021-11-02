class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]\
                         for row in range(vertices)]
        self.__domain = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G']

    # Realiza verificação se verticies vizinhos tem a mesma cor do atual
    def isSafe(self, v, colour, c):
        for i in range(self.V):
            if self.graph[v][i] == 1 and colour[i] == c:
                return False
        return True

    # Função recursiva que faz a resolução do problema de cores
    def graphColourUtil(self, m, colour, v):
        if v == self.V:
            return True

        for c in range(1, m + 1):
            if self.isSafe(v, colour, c) == True:
                colour[v] = c
                if self.graphColourUtil(m, colour, v + 1) == True:
                    return True
                colour[v] = 0

    # Coloreção de grafo
    def graphColouring(self, m):
        colour = [0] * self.V
        if self.graphColourUtil(m, colour, 0) == None:
            return False

        # Imprimindo solução
        print ("Solução existente com a seguinte sequência de cores:")
        for index, c in enumerate(colour):
            print (str(index + 1) + " - " + self.__domain[c], end='; ')
        return True
