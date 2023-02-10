
if __name__ == "__main__":

    def find_min_max(numbers):


        min_num = numbers[0]


        max_num = numbers[0]

        for num in numbers:


            if num < min_num:


                min_num = num


            if num > max_num:


                max_num = num


        return (min_num, max_num)


    listOfNumbers = []


    ranges = int(input("Enter your range of numbers: "))


    for i in range (ranges):


        listOfNumbers.append(int(input("Enter your numbers: ")))

    print(listOfNumbers)


    min_num, max_num = find_min_max(listOfNumbers)


    print("The smallest number is: ", min_num)


    print("The largest number is: ", max_num)


