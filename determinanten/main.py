from math import sqrt


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

determinante = [3, 4, -1, 
                2, 1, 2,
                6, 3, 2]

# determinante = [1, 2,
#                 3, 4]

print(solve_determinante(determinante))                    