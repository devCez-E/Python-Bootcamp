#Write your code below this line ๐

def prime_checker(number):
    for check in range(2, number+1):
        if(number % check == 0):
            if(check == number):
                print("It's a prime number!")
            else:
                print("It's not a prime number.")
                break
        else:
            continue

#Write your code above this line ๐
    
#Do NOT change any of the code below๐
n = int(input("Check this number: "))
prime_checker(number=n)
