file = open('punkty.txt', 'r')
points = file.read().split('\n')[:-1]
file.close()


def turnToArray(number):
    digits = []
    for digit in str(number):
        if int(digit) not in digits:
            digits.append(int(digit))
    return sorted(digits)


def isDigitSim(number1, number2):
    number1 = int(number1)
    number2 = int(number2)

    return turnToArray(number1) == turnToArray(number2)


digSimCount = 0
for point in points:
    numbers = point.split(' ')
    if isDigitSim(numbers[0], numbers[1]):
        digSimCount += 1

print(digSimCount)
