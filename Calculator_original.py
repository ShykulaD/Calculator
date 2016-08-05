# How to make sure the user enters a number (integer) - www.101computing.net

def inputVal(message):
    while True:
        try:
            retVal = int(input(message))
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            return retVal
            break

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
            inputVal("Enter number: ")
            first = inputVal("Enter first number: ")
            second = inputVal("Enter second number: ")
            result = first + second
            print(first, "+", second, "=", result)
            break
            #str = '%d + %d = %d' % (first, second, first+second)
            #print(str)
        elif cmd == 2:
            print("Subtraction")
            first = int(input("Enter first number :"))
            second = int(input("Enter second number :"))
            result = first - second
            print(first ,"-" , second , "=" , result)
        elif cmd == 3:
            print("Mmltiplication")
            first = int(input("Enter first number :"))
            second = int(input("Enter second number :"))
            result = first * second
            print(first ,"*" , second , "=" , result)
        elif cmd == 4:
            print("Division")
            first = int(input("Enter first number :"))
            second = int(input("Enter second number :"))
            result = first / second
            print(first ,"/" , second , "=" , result)
        elif cmd == 6:
            print("Quit!")
            running = False


calc()

