

import random


if __name__ == "__main__":


    def arithmeticMeanOfAList():


        list = []


        rangeNumber = int (input ("Enter the range of the numbers: ") )


        for i in range(rangeNumber):


            list.append (random.randrange (100) )


        print(f"The list is: {list} ")


        sumOfNumbers = 0


        for number in list:


            sumOfNumbers += number


        print (f"The sum of the list is: {sumOfNumbers} ")


        mean = sumOfNumbers / rangeNumber


        print(f"The mean of the list is: {mean} ")


    arithmeticMeanOfAList()


