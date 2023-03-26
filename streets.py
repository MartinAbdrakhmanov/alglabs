from dijkstraalg import dijkstra

graph = [[0, 400, float('inf'), 250, 280],
         [400, 0, 190, float('inf'), float('inf')],
         [float('inf'), 190, 0, 290, float('inf')],
         [250, float('inf'), 290, 0, 160],
         [280, float('inf'), float('inf'), 160, 0]]

print(dijkstra(graph, 1))
