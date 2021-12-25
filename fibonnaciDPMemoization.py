""" Fibonacci using DP Memoization """


def fib(n):  # initializes the array and calls recurrence function
    memoize = [-1 for x in range(n + 1)]
    return calcFibRecur(memoize, n)


def calcFibRecur(memoize, n):
    if n < 2:
        return n

    if memoize[n] >= 0:
        return memoize[n]

    return calcFibRecur(memoize, n - 1) + calcFibRecur(memoize, n - 2)


print(f"The 7th Fibonacci term is: ", fib(7))
