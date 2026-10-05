def reverse_number(number):
    sign = -1 if number < 0 else 1
    number = abs(number)

    reversed_number = 0
    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number //= 10

    return sign * reversed_number


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print(f"Reversed number = {reverse_number(number)}")
