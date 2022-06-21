import rsp
import random

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
com_choice = random.randint(0,2)

print(rsp.choices[choice])
print(f"Computer chose:\n{rsp.choices[com_choice]}")

if choice == com_choice:
    print("Draw")
else:
    if choice == 0:
        if com_choice == 1:
            print("You lose")
        else:
            print("You win")
    elif choice == 1:
        if com_choice == 0:
            print("You win")
        else:
            print("You lose")
    else:
        if com_choice == 0:
            print("You lose")
        else:
            print("You win")