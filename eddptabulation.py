""" EDIT DISTANCE PROBLEM using Dynamic Programming - Tabulation"""


def edit_distance(str1, str2):
    ed = [[-1 for n in range(len(str2)+1)] for m in range(len(str1) + 1)]

    for m in range(len(str1) + 1):
        ed[m][0] = m

    for n in range(len(str2) + 1):
        ed[0][n] = n

    for m in range(1, len(str1) + 1):
        for n in range(1, len(str2) + 1):
            if str1[m - 1] == str2[n - 1]:
                ed[m][n] = ed[m - 1][n - 1]
            else:
                ed[m][n] = 1 + min(ed[m][n - 1], ed[m - 1][n], ed[m - 1][n - 1])

    print("The edit distance matrix is: ")
    for i in ed:
        print(i)

    return ed[len(str1)][len(str2)]


str1 = "apple"
str2 = "ball"

print(f"The edit distance to convert given string '{str1}' into '{str2}' is {edit_distance(str1, str2)}")
