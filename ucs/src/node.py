class Node:

    # Constructor
    def __init__(self, value=None):
        self.__value = value
        self.__connections = []

    @property
    def value(self):
        return self.__value

    @property
    def connections(self):
        return self.__connections

    # Adicionando conexão
    def addConnection(self, node, weightValue):
        self.__connections.append({'connection': node, 'weight': weightValue})

    # Alterando método para apresentação na tela dos dados do nó
    def __str__(self):
        res = f'Nó: {self.__value}\n'
        res += 'Conexões:\n'
        for connection in self.__connections:
            res += f"{connection['connection'].value}, peso: {connection['weight']}\n"

        return res