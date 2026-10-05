def find_missing_number(numbers, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(numbers)
    return expected_sum - actual_sum


if __name__ == "__main__":
    n = int(input("Enter n: "))
    numbers = list(map(int, input(f"Enter {n - 1} numbers from 1 to {n}: ").split()))
    print(f"Missing number = {find_missing_number(numbers, n)}")
