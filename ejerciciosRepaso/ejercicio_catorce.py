

import random


if __name__ == "__main__":


    def arithmeticMeanOfAList():


        list = []


        range_number = int (input ("Enter the range of the numbers: ") )


        for i in range(range_number):


            list.append (random.randrange (100) )


        print(f"The list is: {list} ")


        sum_of_numbers = 0


        for number in list:


            sum_of_numbers += number


        print (f"The sum of the list is: {sum_of_numbers} ")


        mean = sum_of_numbers / range_number


        print(f"The mean of the list is: {mean} ")


    arithmeticMeanOfAList()


