def fib_iterative(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1

    a, b = 0, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b

if __name__ == "__main__":
    n = int(input("Enter nth Number: "))
    print(f"The {n}th Fibonacci number is: {fib_iterative(n)}")
