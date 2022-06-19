height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

bmi = float(weight) / float(height) **2

print("Your BMI is " + str(bmi) +".")

#round
bmi_round = round(bmi)
print("Your BMI is " + str(bmi_round) +".")