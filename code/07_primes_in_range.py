from math import isqrt


def is_prime(number):
    if number < 2:
        return False

    for i in range(2, isqrt(number) + 1):
        if number % i == 0:
            return False

    return True


def primes_in_range(start, end):
    return [number for number in range(start, end + 1) if is_prime(number)]


if __name__ == "__main__":
    start = int(input("Enter start: "))
    end = int(input("Enter end: "))
    print(primes_in_range(start, end))
