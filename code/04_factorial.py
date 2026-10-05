def factorial(number):
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    result = 1
    for i in range(1, number + 1):
        result *= i
    return result


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print(f"Factorial = {factorial(number)}")
