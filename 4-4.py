import math

file = open('punkty.txt', 'r')
points = file.read().split('\n')[:-1]
file.close()

def count_points(points):
    inside_count = 0
    boundary_count = 0
    outside_count = 0

    for point in points:
        x, y = map(int, point.split())
        if abs(x) < 5000 and abs(y) < 5000:
            inside_count += 1
        elif abs(x) == 5000 or abs(y) == 5000:
            boundary_count += 1
        else:
            outside_count += 1

    return inside_count, boundary_count, outside_count

inside_points, boundary_points, outside_points = count_points(points)

print("a. Wewnątrz kwadratu K (bez jego boków):", inside_points)
print("b. Na bokach kwadratu K:", boundary_points)
print("c. Na zewnątrz kwadratu K (bez jego boków):", outside_points)