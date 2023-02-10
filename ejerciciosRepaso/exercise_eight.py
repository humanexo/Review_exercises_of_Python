
if __name__ == "__main__":


    lista = []


    ranges = int(input("Enter your range of numbers: "))


    for i in range(ranges):


        lista.append(int(input("Enter your numbers: ")))


    def reverse_list(lista):


        return lista[::-1]


    reverse_list(lista)


    print(f"This is the origin list {lista}")


    print(f"This is the reverse list {reverse_list(lista)}")
