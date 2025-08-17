#Project Euler question 7

counter = 0
number = 1

#function

def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    # check only odd numbers from 5
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True



# main code

while counter < 10001:
    number += 1
    if is_prime(number):
        counter += 1
        print (number)


 #answer
print(f"the answer is{number}")  
