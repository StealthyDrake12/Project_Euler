#Project Euler question 7

#numbers

counter = 0      
number = 1    



#function

def prime_check(number):
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

#actual code

while counter < 10001:
    number += 1
    if is_prime(num):
        counter += 1

print(number)  # 10001st prime