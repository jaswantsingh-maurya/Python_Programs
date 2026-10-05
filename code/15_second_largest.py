def second_largest(numbers):
    unique_numbers = sorted(set(numbers))

    if len(unique_numbers) < 2:
        raise ValueError("List must contain at least two different numbers.")

    return unique_numbers[-2]


if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print(f"Second largest = {second_largest(numbers)}")
