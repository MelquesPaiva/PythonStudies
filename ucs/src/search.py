from queue import PriorityQueue

class Search:

    def ucs(graph, start, goal):
        visited = set()
        q = PriorityQueue()

        q.put((0, str(start), [str(start)]))
        while not q.empty():
            cost, node, path = q.get()
            visited.add(node)
            if node == str(goal):
                return path, cost
            else:
                for conn in graph.node(node).connections:
                    nodeConn = conn['connection'].value
                    if nodeConn not in visited:
                        q.put((cost + int(conn['weight']), nodeConn, path + [str(nodeConn)]))

        return None, None