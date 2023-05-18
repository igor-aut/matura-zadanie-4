file = open('punkty.txt', 'r')
points = file.read().split('\n')[:-1]
file.close()


def isPrime(number):
    number = int(number)
    
    if number == 0 or number == 1:
        return False
    prime = [True for i in range(number+1)]
    p = 2
    while (p * p <= number):
        if (prime[p] == True):
            for i in range(p * p, number+1, p):
                prime[i] = False
        p += 1
 
    return prime[-1]

primeCount = 0
for point in points:
    numbers = point.split(' ')
    if isPrime(numbers[0]) and isPrime(numbers[1]):
        primeCount += 1

print(primeCount)