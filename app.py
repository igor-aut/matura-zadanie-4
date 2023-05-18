import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def are_digit_similar(n1, n2):
    digits1 = set(str(n1))
    digits2 = set(str(n2))
    return digits1 == digits2

def distance(x1, y1, x2, y2):
    return round(math.sqrt((x2 - x1)**2 + (y2 - y1)**2))

points = []
with open('punkty.txt', 'r') as file:
    for line in file:
        x, y = map(int, line.split())
        points.append((x, y))

prime_points_count = 0
digit_similar_points_count = 0
max_distance = 0
max_distance_points = ()

for i in range(len(points)):
    for j in range(i+1, len(points)):
        x1, y1 = points[i]
        x2, y2 = points[j]

        if is_prime(x1) and is_prime(y1):
            prime_points_count += 1

        if are_digit_similar(x1, y1):
            digit_similar_points_count += 1

        curr_distance = distance(x1, y1, x2, y2)
        if curr_distance > max_distance:
            max_distance = curr_distance
            max_distance_points = ((x1, y1), (x2, y2))

# Zapis wyników do pliku
with open('wyniki4.txt', 'w') as file:
    file.write("1. {}\n".format(prime_points_count))
    file.write("2. {}\n".format(digit_similar_points_count))
    file.write("3. {}, {}\n".format(max_distance_points[0], max_distance_points[1]))
    file.write("   {}\n".format(max_distance))