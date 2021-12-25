""" GCD """


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


a_ = 2873622
b_ = 71436
print(f"The gcd of {a_} and {b_} is: ", gcd(a_, b_))
