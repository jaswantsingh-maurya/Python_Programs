def check_number(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print(check_number(number))
