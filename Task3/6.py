def is_armstrong(n):
    return n == sum(int(digit) ** len(str(n)) for digit in str(n))
n = int(input("Enter a number: "))
if is_armstrong(n):
    print(n, "is an Armstrong number")
else:
    print(n, "is not an Armstrong number")