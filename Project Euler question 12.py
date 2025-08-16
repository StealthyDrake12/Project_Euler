import math

n = 1
trinagular = 0
max = 500
#my super slow funciton that took hours
# def count_divisors(n):
#     count = 0
#     for i in range(1, n + 1):
#         if n % i == 0:  # if i divides n evenly
#             count += 1
#     return count


##Internet super fast function##
##took seconds##


def count_divisors(n):
    count = 0
    root = int(math.sqrt(n))
    for i in range(1, root + 1):
        if n % i == 0:
            count += 2  # i and n//i
    if root * root == n:  # if n is a perfect square
        count -= 1
    return count



while True:

    trinagular += n
    n += 1
    print (trinagular)
    divisors = count_divisors(trinagular)
    print(divisors)
    if divisors >500:
     print(f"{trinagular} has over 500 divisors")
     break
    if n > 1000000:
        break