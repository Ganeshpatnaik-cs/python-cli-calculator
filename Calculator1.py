def calculator():
    print("simple calculator")
    print("1. addition")
    print("2. subtraction")
    print("3. multiplication")
    print("4. division")
    choice=input("enter your choice (1-4): ")
    num1=float(input("enter first number: "))
    num2=float(input("enter second number: "))
    if choice=='1':
        print("result:",num1+num2)
    elif choice=='2':
        print("result:",num1-num2)
    elif choice=='3':
            print("result:",num1*num2)
    elif choice=='4':
            if num2 !=0:
                  print("result:",num1/num2)
            else:
                  print("Error! Cannot divide zero")
    else:
          print("invalid choice!")
calculator()