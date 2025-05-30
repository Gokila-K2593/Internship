def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer"
    elif n == 1:  
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence
n = int(input("Enter the number of Fibonacci numbers: "))
print("Fibonacci numbers are", fibonacci(n))