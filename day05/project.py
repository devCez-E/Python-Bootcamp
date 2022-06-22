import random
import pwdata
easy_pw = ""
hard_pw = []
passward = ""

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level (e.g. fghf^&23)
for letter in range(0, nr_letters):
    easy_pw += random.choice(pwdata.letters)
    #index = random.randint(0, len(pwdata.letters) - 1)
    #easy_pw += pwdata.letters[index]

for n in range(0, nr_symbols):
    easy_pw += random.choice(pwdata.symbols)
    #index = random.randint(0, len(pwdata.symbols) - 1)
    #easy_pw += pwdata.symbols[index]

for n in range(0, nr_numbers):
    easy_pw += random.choice(pwdata.numbers)
    #index = random.randint(0, len(pwdata.numbers) - 1)
    #easy_pw += pwdata.numbers[index]
print(easy_pw)

#Hard Level (e.g. g^2jk8&)
for letter in range(0, nr_letters):
    hard_pw.append(random.choice(pwdata.letters))

for letter in range(0, nr_symbols):
    hard_pw.append(random.choice(pwdata.symbols))

for letter in range(0, nr_numbers):
    hard_pw.append(random.choice(pwdata.numbers))

for letter in range(0, len(hard_pw)):
    passward += random.choice(hard_pw)
print(passward)