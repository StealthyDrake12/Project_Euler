import math

#variabels

total = 0

#function

def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

#code

for i in range (2, 2000000):
    if isPrime(i):
        total += i


print (total)