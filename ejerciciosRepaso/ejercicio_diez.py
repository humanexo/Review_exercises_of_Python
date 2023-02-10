
if __name__ == "__main__":


    number = int(input("Enter your number: "))

    def factorial(number):


        if number == 0:


            return 1


        else:


            return number * factorial(number - 1)


    print(f"The number factorial of {number} is {factorial(number)}")