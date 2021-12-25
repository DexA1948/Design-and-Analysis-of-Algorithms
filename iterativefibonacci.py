""" Fibonacci Sequence"""


def fibonacci(a, b, n):
    print(a)
    print(b)
    for i in range(1, n-1):
        a, b = b, a+b
        print(b)


fibonacci(1, 1, 10)
