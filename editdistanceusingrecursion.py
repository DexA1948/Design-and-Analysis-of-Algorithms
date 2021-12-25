""" EDIT DISTANCE PROBLEM using Recursion and Backtracking - Bruteforce"""


def edit_distance(str1, str2, m, n):
    # if index of str1 is -1 we need n+1 insertions
    if m == -1:
        return n+1

    # if index of str2 is -1 we need m+1 removals
    if n == -1:
        return m+1

    if str1[m] == str2[n]:
        return edit_distance(str1, str2, m-1, n-1)

    cost = 0

    cost = 1 + min(edit_distance(str1, str2, m, n-1), edit_distance(str1, str2, m-1, n),
                   edit_distance(str1, str2, m-1, n-1))
    return cost


print(edit_distance("abz", "xyz", 2, 2))


