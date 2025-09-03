#Printing basic message
print("Hello World!")

#Printing with varibale
message = ("Hello Tadhg")
print(message)

#redefining variable
message = ("Hello, reader")
print(message)

# Some basic name and methods attached
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

# Using an f string to tie a name together
first_name = 'ada'
last_name = 'lovelace'
full_name = (f"{first_name} {last_name}")
print(full_name.title())

# Using an f string to make a sentence from a created variable
message = (f"Hello, {full_name.title()}!")
print(message)

print("\t" + message)
print (f'\t{message}')
print ("\t",message)

# Stripping white spaces with the strip method
message = (" python ")
print (message.lstrip())
print (message.rstrip())
print (message.strip())

# Removing prefixes with the removepreffix method and suffixes 
website = ("https://apple.com")
print(website.removeprefix("https://"))


website = ("https://apple.com")
print(website.removesuffix(".com"))

webiste = ("https://apple.com")
print(website.removeprefix("https://").removesuffix(".com"))
