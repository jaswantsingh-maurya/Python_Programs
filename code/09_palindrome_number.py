def is_palindrome(number):
    if number < 0:
        return False
    return number == int(str(number)[::-1])


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    if is_palindrome(number):
        print(f"{number} is Palindrome")
    else:
        print(f"{number} is Not Palindrome")
