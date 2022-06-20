height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi = round(float(weight) / float(height) **2, 1)

print("Your BMI is " + str(bmi) +".")

if bmi > 35:
    print("Clinically Obese.")
elif bmi > 30:
    print("Obese.")
elif bmi > 25:
    print("Overweight.")
elif bmi > 18.5:
    print("Normal weight.")
else:
    print("Underweight.")