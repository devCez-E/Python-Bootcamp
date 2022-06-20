#if condition:
#   do this
#else:
#   do this

from turtle import heading


water_level = int(input("ENTER WATER LEVEL : "))

if water_level > 80:
    print("Drain water")
else:
    print("Continue")

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
    print("You can ride the rollercoaster!")
else:
    print("You can't ride the rollercoaster!")