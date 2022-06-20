true = 0
love = 0
love_score = 0

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
combine_name = name1 + name2
combine_name.lower()

true += combine_name.count("t")
true += combine_name.count("r")
true += combine_name.count("u")
true += combine_name.count("e")

love += combine_name.count("l")
love += combine_name.count("o")
love += combine_name.count("v")
love += combine_name.count("e")

love_score = int(str(true) + str(love))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}")