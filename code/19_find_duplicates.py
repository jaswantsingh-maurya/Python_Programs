def find_duplicates(numbers):
    seen = set()
    duplicates = []

    for number in numbers:
        if number in seen and number not in duplicates:
            duplicates.append(number)
        else:
            seen.add(number)

    return duplicates


if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print(find_duplicates(numbers))
