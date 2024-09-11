def fibonacci_numbers(n):
    indices = list(range(n))
    
    fib = lambda x: x if x <= 1 else fib(x - 1) + fib(x - 2)
    
    fibonacci_sequence = list(map(fib, indices))
    
    return fibonacci_sequence

n = 10
print(f"Fibonacci sequence up to {n} numbers: {fibonacci_numbers(n)}")
