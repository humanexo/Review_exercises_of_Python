
if __name__ == "__main__":


    def fahrenheitToCelsius():
        gradesFahrenheit = float(input("Enter your grades in Fahrenheit: "))


        gradesCelsius = (gradesFahrenheit - 32) * 0.5555
        print(f"The grades Fahrenheit {gradesFahrenheit} in grades Celsius is {gradesCelsius}")

    fahrenheitToCelsius()
