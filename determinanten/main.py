from math import sqrt
from random import randint, random


def solve_determinante(d):
    n = sqrt(len(d))

    if n != int(n):
        return

    n = int(n)

    if n == 1:
        return d[0]

    result = 0

    for i in range(n):
        s = 1 - (i % 2) * 2

        sub_d = []

        for _y in range(1, n):
            for _x in range(n):
                if i == _x:
                    continue

                sub_d.append(d[_x + _y * n])

        result += s * d[i] * solve_determinante(sub_d)

    return result

# determinante = [3, 4, -1,
#                 2, 1, 2,
#                 6, 3, 2]

# determinante = [1, 2,
#                 3, 4]

# format: [[x1 + y1 + z1 = c1],
#          [x2 + y2 + z2 = c2],
#          [x3 + y3 + z3 = c3]]
def solve_linear(equations):
    s = len(equations)
    nen = []
    ret = []

    for i in equations:
        if len(i) != s + 1:
            return

        for j in range(s):
            nen.append(i[j])

    for i in range(s):
        zae = nen.copy()

        for j in range(s):
            zae[i + s*j] = equations[j][s]

        ret.append(solve_determinante(zae) / solve_determinante(nen))
    
    return ret



# n = 11
# determinante = []
# for i in range(n * n):
#     determinante.append(randint(1, 9))

# determinante = [5, -5, 4, 2, 2, -3, -11, 3, -7]

# print(determinante)
# print(solve_determinante(determinante))

equations = [
    [-2, -2, 2, -2],
    [2, -2, 2, -6],
    [1, 7, 1, -11]
]

print(solve_linear(equations))