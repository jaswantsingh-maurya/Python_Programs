def is_palindrome_string(text):
    cleaned_text = text.lower()
    return cleaned_text == cleaned_text[::-1]


if __name__ == "__main__":
    text = input("Enter a string: ")
    if is_palindrome_string(text):
        print("Palindrome")
    else:
        print("Not Palindrome")
