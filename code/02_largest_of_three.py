def largest_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


if __name__ == "__main__":
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))
    c = int(input("Enter Third Number: "))
    print(f"{largest_of_three(a, b, c)} is Largest")
