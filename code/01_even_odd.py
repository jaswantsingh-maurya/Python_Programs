def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    return "Odd"


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print(check_even_odd(number))
