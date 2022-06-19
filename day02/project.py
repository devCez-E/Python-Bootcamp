print("Welcome to the tip calculator.")

total = float(input("What was the total bill? $"))
tip_percent = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people to split the bill? "))

each_tip = total * (1 + tip_percent / 100) / people

print(f"Each person should pay: ${round(each_tip, 2)}")