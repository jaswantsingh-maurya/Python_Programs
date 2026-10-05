def sum_of_digits(number):
    number = abs(number)
    total = 0

    while number > 0:
        total += number % 10
        number //= 10

    return total


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print(f"Sum of digits = {sum_of_digits(number)}")
