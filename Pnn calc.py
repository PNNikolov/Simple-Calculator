running = True 

while running:
    print("1 = Sum")
    print("2 = Sub")
    print("3 = Multiplication")
    print("4 = Divide")
    print("5 = Exit program")
    command = int(input("Enter number:"))
    if command == 1:
        print("Sum:")
        firstNumber = int(input("Enter first number:"))
        secondNumber = int(input("Enter second number:"))
        result = 'result: ' + str(firstNumber) + '+' + str(secondNumber) + '=' + str(firstNumber + secondNumber)
    elif command == 2:
        print("Sub:")
        firstNumber = int(input("Enter first number:"))
        secondNumber = int(input("Enter second number:"))
        result = 'result: ' + str(firstNumber) + '-' + str(secondNumber) + '=' + str(firstNumber - secondNumber)
    elif command == 3:
        print("Multiplication:")
        firstNumber = int(input("Enter first number:"))
        secondNumber = int(input("Enter second number:"))
        result = 'result: ' + str(firstNumber) + '*' + str(secondNumber) + '=' + str(firstNumber * secondNumber)
    elif command == 4:
        print("Divide:")
        firstNumber = int(input("Enter first number:"))
        secondNumber = int(input("Enter second number:"))
        result = 'result: ' + str(firstNumber) + '/' + str(secondNumber) + '=' + str(firstNumber / secondNumber)
    elif command == 5:
        result = "Goodbye!"
        running = False
    print('\n' + result + '\n')
