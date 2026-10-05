def reverse_string(text):
    reversed_text = ""

    for char in text:
        reversed_text = char + reversed_text

    return reversed_text


if __name__ == "__main__":
    text = input("Enter a string: ")
    print(f"Reversed string = {reverse_string(text)}")
