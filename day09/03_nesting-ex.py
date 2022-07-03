programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
}

print(programming_dictionary["Bug"])
print(programming_dictionary["Function"])

# Adding new item to dictionary.
programming_dictionary["Loop"] = "The action of doing something over and over again."

print(programming_dictionary)

# Create an empty dictionary.
empty_dictionary = {}
print(empty_dictionary)

# Wipe an existing dictionary
#programming_dictionary = {}
#print(programming_dictionary)

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in a computer"
print(programming_dictionary)

# Loop through a dictionary
for thing in programming_dictionary:
    print(f"{thing} is {programming_dictionary[thing].lower()}")


##########################################################################

#Nesting
capitals = {
    "France" : "Paris",
    "Germany" : "Berlin",
}

#Nesting Dictionary in a Dictionary

travel_log_dict = {
    "France" : {
        "cities_visited": ["Paris", "Lille", "Dijon"], 
        "total_visits": 12},
    "Germany" : {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5},
}

#Nesting Dictionary in a List
travel_log_list = [
    {
        "country":"France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country":"Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    },
]