def dijkstra(graph, startnode):
    startnode -= 1
    visited = [startnode]
    path = [[] for _ in range(len(graph))]
    for p in range(len(graph[startnode])):
        if graph[startnode][p] != float('inf'):
            path[p] = [startnode]
    currnode = startnode
    for i in range(len(graph)-1):
        mn = float('inf')
        for j in range(len(graph[currnode])):
            if not(j in visited) and graph[currnode][j] < mn:
                mn = graph[currnode][j]
                nextnode = j
        visited.append(nextnode)
        for z in range(len(graph[nextnode])):
            if not(z in visited):
                if graph[nextnode][z] + mn < graph[currnode][z]:
                    graph[currnode][z] = graph[nextnode][z] + mn
                    path[z].append(nextnode)
    for p in range(len(graph[startnode])):
        if graph[startnode][p] != float('inf'):
            path[p].append(p)
    return graph[startnode], path


if __name__ == '__main__':
    graph = [[0, 50, 45, 10, float('inf'), float('inf')],
             [float('inf'), 0, 10, 15, float('inf'), float('inf')],
             [float('inf'), float('inf'), 0, float('inf'), 30, float('inf')],
             [10, float('inf'), float('inf'), 0, 15, float('inf')],
             [float('inf'), 20, 35, float('inf'), 0, float('inf')],
             [float('inf'), float('inf'), float('inf'), float('inf'), 3, 0]]
    print(dijkstra(graph, 1))
