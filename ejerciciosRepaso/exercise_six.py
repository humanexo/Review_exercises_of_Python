import random

if __name__ == "__main__":


    list = []
    sumOfTheNumbers = 0

    numbersOnTheList = int(input("Enter the numbers: "))


    for i in range (numbersOnTheList):


        list.append(random.randint(0,50))


    for number in list:


        sumOfTheNumbers += number


    print(list)


    print(sumOfTheNumbers)



