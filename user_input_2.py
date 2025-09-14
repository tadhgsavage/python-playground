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


# Lets create a while loop to make a number counter up to 5
current_number = 5
# Creation of the while loop
while current_number <= 5:
    print(current_number)
    # Add the value of 1 to current number inside of the while loop
    current_number += 1


# We can also get a program to keep running with a while loop 
prompt = ('\nGive me a sentence and I shall repeat it back to you: ')
prompt += ("\nEnter 'quit' and the program will stop running.")

message = ('')
while message != ('quit'):
    message = input(prompt)
    print(message)


# This while loop works but when the user inputs quit the quit message is still displayed, which might not be ideal
# This can, however, be fixed by a simple if statement

prompt = "\nInput a message of your choice and this program will print it back to you"
prompt += "\nWrite 'quit' to quit the program: "

message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)





