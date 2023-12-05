from geopy.distance import geodesic

# Координаты городов
cities = {
    'Москва': (55.755825, 37.617634),
    'Мадрид': (40.416775, -3.703790),
    'Пекин': (39.904200, 116.407396),
    'Вашингтон': (38.895110, -77.036369),
    'Сингапур': (1.352083, 103.819836)
}

# Рассчитываем расстояния
distances = {}
for city1, coord1 in cities.items():
    distances[city1] = {}
    for city2, coord2 in cities.items():
        if city1 == city2:
            distances[city1][city2] = 0
        else:
            distances[city1][city2] = round(geodesic(coord1, coord2).kilometers)

# Выводим таблицу расстояний
# print("\t", end="")
# for city in cities:
#     print(f"{city}\t", end="")
# print()

# for city1 in cities:
#     print(f"{city1}\t", end="")
#     for city2 in cities:
#         print(f"{distances[city1][city2]:,}\t", end="")
#     print()

for city1 in cities:
    print('[',end='')
    for city2 in cities:
        print(f"{distances[city1][city2]},", end="")
    print(']',end='')
    print()
