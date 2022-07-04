import art
import calculator

print(art.logo)
num1 = float(input("What's the first number?: "))
num2 = float(input("What's the second number?: "))

for symbol in calculator.operations:
    print(symbol)

def operation(n1, n2):
    operation_symbol = input("Pick an operation: ")
    function = calculator.operations[operation_symbol]
    answer = function(n1, n2)
    print(f"{n1} {operation_symbol} {n2} = {answer}")
    isContinue = input(f"Type 'y' to continue calculating with 8, or type 'n' to exit.: ")
    
    if isContinue == 'y':
        num3 = int(input("What's the next number?: "))
        operation(answer, num3)
        
operation(num1, num2)