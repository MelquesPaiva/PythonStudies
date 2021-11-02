import sys
from src.graph import Graph

def main():
    currentFile, graphFile, domain = sys.argv
    file = open(graphFile)

    graphConfig = file.readline().split(' ')
    nodesQtd = int(graphConfig[0])

    # Driver Code
    g = Graph(nodesQtd)

    graph = []
    for var in range(nodesQtd):
        graph.append([])

    for var in range(nodesQtd):
        for var2 in range(nodesQtd):
            graph[var].append(0)

    for line in file:
        line = line.replace('\n', '')
        nodeData = line.split(' ')
        node = int(nodeData[0]) - 1
        conn = int(nodeData[1]) - 1
        graph[node][conn] = 1

    g.graph = graph
    m = int(domain)
    g.graphColouring(m)

    # This code is contributed by Divyanshu Mehta

main()
