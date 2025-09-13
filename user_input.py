# Simple print back input message 
message = input("Write a message and I shall print it back to you: ")
print(message)

# Using input to create a greeting
name = input("Please state your name: ")
print(f'Hello, {name}!')

# When a prompt is perhaps too long for the input function it can be attached in from a variable
prompt = "If you share your name, we can personalize the messages you see."

# This eill add the new strong below onto the prompt above, in this case a new message will appear under the one above
prompt += "\nWhat is your first name? "

# Using the variable created
name = input(prompt)
print(f'Hello, {name}!')

# Using intergers with the input function
# This can be tricky as python inteperets all inputs as strings so we must convert it to an interger 
age = input('Enter your age: ')
age = int(age)
if age >= 20:
    print('True')
else:
    print("False")

# Rollacoaster height checker
height = input("Please enter your height in cm: ")
height = int(height)
if height >= 150:
    print(f'As your height is {height}cm you may go on the ride.')
elif height < 150:
    print(f'As your height is {height}cm you can not go on the ride.')



