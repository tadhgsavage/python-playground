# A useful operator when working with numbers is the Mondulo operator \
# The Mondulo operator divides one number by another and returns the remainder.
# When a number is divisible by another number it always returns 0, therefore useful for finding even and odd numbers
# 2 goes into 5 twice with remainder 1. Therefore 1 is printed back at us. 
print(5 % 2)

# Even number detector 
number = input("Enter in a number and i'll tell you if its even or not: ")
number = int(number)

if number % 2 == 0:
    print(f'Your nuber: {number}, is even!')
else:
    print(f'Sorry chuck your number of {number} is no good.')
