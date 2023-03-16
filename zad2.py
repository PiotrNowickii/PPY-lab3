while True:
    check = False
    tmp = 0
    while not check:
        tmp = input("What operation would you like to do: +, -, /, *. If you want to end input: end\n")
        if tmp != '+' and tmp != '-' and tmp != '*' and tmp != '/' and tmp != "end":
            print("Please input correct value")
        else:
            check = True
    if tmp == "end":
        break
    numOne = int(input("Input first number"))
    numTwo = int(input("Input second number"))
    if tmp == '+':
        result = numOne + numTwo
        print(result)
    elif tmp == '-':
        result = numOne - numTwo
        print(result)
    elif tmp == '*':
        result = numOne * numTwo
        print(result)
    elif tmp == '/':
        result = numOne / numTwo
        print(result)
    else:
        print("Error")
