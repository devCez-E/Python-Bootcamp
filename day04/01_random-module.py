#https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences

import random
import my_module

random_integer = random.randint(1, 10)
print(random_integer)
print(my_module.pi)

love_score = random.randint(1, 100)
print(f"Your Love-score is {love_score}")

random_float = random.random()
print(random_float)

#How to create a random decimal number between 0 and 5?
#0.0000000 - 0.999999...
#0.0000000 - 4.999999...
print(random_float * 5)