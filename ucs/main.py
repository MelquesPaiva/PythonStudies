import sys
from src.graph import Graph
from src.search import Search

def main():
    currentFile, graphFile, start, goal = sys.argv

    # Recuperando nome do arquivo passado no parâmetro
    file = open(graphFile)
    graph = Graph()

    # Primeira linha de configuração do nó
    graphConfig = file.readline().split(' ')
    amountNods = graphConfig[0]

    nodeList = []

    for line in file:
        line = line.replace('\n', '')
        nodeData = line.split(' ')

        # Adicionando nó ao grafo
        graph.addNode(nodeData[0])

        # Adicionando conexão do respectivo nó
        graph.addEdge(nodeData[0], nodeData[1], nodeData[2])

    path, cost = Search.ucs(graph, start, goal)
    if path == None or cost == None:
        print('Caminho inexistente')
        return

    result = ''

    for node in path:
        result += node + ' -> '

    result += 'Custo: ' + str(cost)

    print(result)

    file.close()

main()
