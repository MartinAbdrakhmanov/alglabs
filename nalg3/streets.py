from dijkstraalg import dijkstra

graph = [[0, 400, float('inf'), 250, 280],
         [400, 0, 190, float('inf'), float('inf')],
         [float('inf'), 190, 0, 290, float('inf')],
         [250, float('inf'), 290, 0, 160],
         [280, float('inf'), float('inf'), 160, 0]]
streets = {1: 'Пять углов',
           2: 'Мост ломоносова',
           3: 'Набережная Фонтанки',
           4: 'Улица Рубинштейна',
           5: 'Станция метро Достоевская'}
s = input('Введите где вы находитесь: ')
for i in streets:
    if streets[i] == s:
        n = i - 1
r, p = dijkstra(graph, n)
for i in range(len(p)):
    if i != n:
        p[i].insert(0, n)
        for j in range(len(p[i])):
            p[i][j] = streets[p[i][j]+1]
print('Расстояния до близжайших улиц:')
for i in range(len(graph[n])):
    if i != n:
        print(f'{streets[i+1]}: {r[i]} метров')
        print(f'Лучший маршрут: {p[i]}')
