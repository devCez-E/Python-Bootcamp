import os
import art

isContinue = True
auction = []
num = 0

print(art.logo)
print("Welcome to the secret auction program.")

while(isContinue):
    temp = {}

    name = input("What is your name?: ")
    bids = int(input("What's your bid?: $"))
    temp["name"] = name
    temp["bid"] = bids
    auction.append(temp)

    isContinue = input("Are ther any other bidders? Type 'yes' or 'no'.\n") == "yes"
    os.system('cls')

for bid in range(len(auction)):
    compare_value = 0
    if auction[bid]["bid"] > compare_value:
        compare_value = auction[bid]["bid"]
        num = bid
    else:
        continue

print(f"The winner is {auction[num]['name']} with a bid of ${auction[num]['bid']}.")