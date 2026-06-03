from tabulate import tabulate

class TemperatureConverter:
    @staticmethod
    def c_to_f(c):
        return (c * 9/5) + 32

    @staticmethod
    def c_to_k(c):
        return c + 273.15

    @staticmethod
    def f_to_c(f):
        return (f - 32) * 5/9

    @staticmethod
    def f_to_k(f):
        return (f - 32) * 5/9 + 273.15

    @staticmethod
    def k_to_c(k):
        return k - 273.15

    @staticmethod
    def k_to_f(k):
        return (k - 273.15) * 9/5 + 32

def main():
    print("Temperature Converter")
    print("1. Convert Celsius")
    print("2. Convert Fahrenheit")
    print("3. Convert Kelvin")
    choice = input("Enter choice (1-3): ")
    try:
        val = float(input("Enter temperature value: "))
        table = []
        if choice == "1":
            f = TemperatureConverter.c_to_f(val)
            k = TemperatureConverter.c_to_k(val)
            table = [["Celsius", f"{val:.2f}"], ["Fahrenheit", f"{f:.2f}"], ["Kelvin", f"{k:.2f}"]]
        elif choice == "2":
            c = TemperatureConverter.f_to_c(val)
            k = TemperatureConverter.f_to_k(val)
            table = [["Fahrenheit", f"{val:.2f}"], ["Celsius", f"{c:.2f}"], ["Kelvin", f"{k:.2f}"]]
        elif choice == "3":
            c = TemperatureConverter.k_to_c(val)
            f = TemperatureConverter.k_to_f(val)
            table = [["Kelvin", f"{val:.2f}"], ["Celsius", f"{c:.2f}"], ["Fahrenheit", f"{f:.2f}"]]
        else:
            print("Invalid choice")
            return
        print(tabulate(table, headers=["Scale", "Value"], tablefmt="grid"))
    except ValueError:
        print("Invalid number input")

if __name__ == "__main__":
    main()
