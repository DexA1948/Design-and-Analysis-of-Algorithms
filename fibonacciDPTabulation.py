""" Fibonacci using tabulation """


def fibonacci(n):
    A = [0, 1]
    for i in range(2, n+1):
        A.append(A[i-1] + A[i-2])
    return A[n]


print(f"Fibonacci(5): {fibonacci(5)}")
