#Euler 14 - longest colltaz sequence.

#Collatz sequence (Project Euler 14)
# Start with n. If n is even → n/2, if odd → 3n+1, repeat until 1.
# Example: 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1 (length 10)
longestnum = 0

startnum = 13

y = 0


for startnum in range (1,999999):
    
    n = startnum
    counter = 1
    


    while n != 1:
        if n % 2 != 0:
            n = 3 * n + 1
        else:
            n = n // 2
        counter += 1

    if counter > y:
        y =counter
        longestnum =startnum


print(f"Number with longest Collatz chain under 1,000,000:{longestnum}")
print("Chain length:",y)

        
    