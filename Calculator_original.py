def inputVal(message):
    while True:
        try:
            retVal = float(input(message))
        except ValueError:
            print("Not an integer! Try again.")
        else:
            return retVal

def cont():
    print("Wanna conntinue?")
    print("Type for conntinue 'Yes'")
    print("Type for conntinue 'No'")
    answer = input("Type your choice here: ")
    while True:
        if answer == "No" or "no":
            calc()
        elif answer == "Yes" or "yes":
            break
        else:
            print ("You didn't write Yes or No answer")
            cont()

def calc():
    while True:
        print("1 = Addition")
        print("2 = Subtraction")
        print("3 = Multiplication")
        print("4 = Division")
        print("5 = Exit program")
        cmd = inputVal("Enter number : ")
        if cmd == 1:
            print("Addition")
            first = inputVal("Enter first number: ")
            second = inputVal("Enter second number: ")
            result = first + second
            print(first, "+", second, "=", result)
            cont()
            #str = '%d + %d = %d' % (first, second, first+second)
            #print(str)
        elif cmd == 2:
            print("Subtraction")
            first = inputVal("Enter first number: ")
            second = inputVal("Enter second number: ")
            result = first - second
            print(first ,"-" , second , "=" , result)
            cont()
        elif cmd == 3:
            print("Mmltiplication")
            first = inputVal("Enter first number: ")
            second = inputVal("Enter second number: ")
            result = first * second
            print(first ,"*" , second , "=" , result)
            cont()
        elif cmd == 4:
            print("Division")
            first = inputVal("Enter first number: ")
            second = inputVal("Enter second number: ")
            result = first / second
            print(first ,"/" , second , "=" , result)
            cont()
        elif cmd == 5:
            print("Quit!")
            break

calc()