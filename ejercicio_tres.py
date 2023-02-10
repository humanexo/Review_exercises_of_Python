import random

if __name__ == "__main__":


    list = []
    numbersOnTheList = int(input("Enter the numbers: "))
    for i in range (numbersOnTheList):
        list.append(random.randint(0,100))
    print(list)