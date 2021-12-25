"""This is how to use multiline comments and get function.__doc__"""
# """Multiline comments
# hahaha"""
#
#
# # single line comment
# # #Hello what this do?
#
# def fun():
#     """# this is yea"""
#     return 0
#
#
# print(fun.__doc__)


# linear congruential method for generating random numbers in SAM
"""
def linearcongruentialmethod(x, a, c, m, n):
    randomlist = []
    for i in range(0, n):
        x = (a*x + c) % m
        print(x, end="\n")


linearcongruentialmethod(63, 19, 0, 100, 10)
"""

