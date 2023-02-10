if __name__ == "__main__":


    numberOne = int(input("Enter your first number: "))


    numberTwo = int(input("Enter your second number: "))

    print("Enter the option you want to calculate: ")


    print("""
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    """)


    optionToCalculate = int(input("Enter your option: "))


    if optionToCalculate == 1:


        adittion = numberOne + numberTwo


        print(f"The result between the operation of {numberOne} and {numberTwo} is {adittion}")


    if optionToCalculate == 2:


        subtraction = numberOne - numberTwo


        print(f"The result between the operation of {numberOne} and {numberTwo} is {subtraction}")


    if optionToCalculate == 3:


        multiplication = numberOne * numberTwo


        print(f"The result between the operation of {numberOne} and {numberTwo} is {multiplication}")


    if optionToCalculate == 4:


        division = numberOne / numberTwo


        print(f"The result between the operation of {numberOne} and {numberTwo} is {division}")




