import math


file = open('punkty.txt', 'r')
points = file.read().split('\n')[:-1]
file.close()
points = [tuple(map(int, point.split())) for point in points]


def distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def find_furthest_points(points):
    max_distance = 0
    furthest_points = None

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            current_distance = distance(points[i], points[j])
            if current_distance > max_distance:
                max_distance = current_distance
                furthest_points = (points[i], points[j])

    return furthest_points, round(max_distance)

furthest_points, max_distance = find_furthest_points(points)
point1, point2 = furthest_points

print("Punkt 1:", point1)
print("Punkt 2:", point2)
print("Odległość:", max_distance)