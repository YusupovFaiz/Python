import matplotlib.pyplot as plt
from matplotlib.path import Path

# 2 задание
cords2 = [(2, 1), (0, 2), (0, 3), (-1, -2), (4, -1)]
# создаем путь на основе вершин полигона
path = Path(cords2)

# проверяем точки
points = [(1, -2)]
for point in points:
    # проверяем, лежит ли точка внутри полигона
    if path.contains_point(point):
        print(f"Точка {point} лежит внутри полигона")
    else:
        print(f"Точка {point} лежит снаружи полигона")

Graph(cords2)