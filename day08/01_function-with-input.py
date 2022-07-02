# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet():
    print("Hello\nHow do you do?\nIsn't the weather nice today?")

greet()

# Function that allows for input

def greet_with_name(name):
    print(f"Hello {name}.\nHow do you do?\nIsn't the weather nice today?")

greet_with_name("Cezanne")

# Functions with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with("Cezanne", "Paris")

#Keyword Arguments
def my_function(a, b, c):
    print(a)
    print(b)
    print(c)

my_function(b=2, c=3, a=1)