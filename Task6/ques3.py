def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def largest_prime_less_than(n):
    num = n - 1 
    while num > 1:
        if is_prime(num):
            return num
        num -= 1  
    return None  
n = int(input("Enter a number:"))
result = largest_prime_less_than(n)
if result:
    print("Largest prime number less than", n, "is:", result)
else:
    print("No prime number found.")