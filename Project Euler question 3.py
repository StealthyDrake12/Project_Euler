#Project Euler question 3

#starting numbers

number = 600851475143
divider = 2

# Check if the number returns an intiger

def Num_Check(number,divider):
    if number % divider == 0:
        
        print (f"{number} does divide by{divider}")
        return True
    else:
        
        print(f"{number} does NOT divide by {divider}")
        return False

#Do it

Num_Check(number, divider)

while divider * divider <= number:
    if Num_Check(number, divider):
        number = number // divider
        
    else:
        divider = divider + 1


#The Answer (Hopefully)
        
print("Done. Largest prime factor is:", number)