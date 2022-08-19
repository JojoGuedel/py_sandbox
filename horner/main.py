TOLERANCE = 5

def horner(indecies, x_0):
    output = []

    for i, e in enumerate(indecies):
        if i == 0:
            output.append(e)
            continue
        
        output.append(round(x_0 * output[i - 1] + e, TOLERANCE))

    print(x_0, output)

    if len(output) > 2:
        horner(output[0:-1], x_0)

# Aufgabe 5c
indecies = [2, -3, -5, 8]
x_0 = 4

print(" " * len(str(x_0)), indecies)
horner(indecies, x_0)