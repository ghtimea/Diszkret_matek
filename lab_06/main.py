def exEuclid(a = 19, b = 59):
    x0, x1, y0, y1 = 1, 0, 0, 1

    while True:
        q = a // b
        r = a - q * b
        a = b
        b = r
        if b == 0:
            return a, x1, y1
        x2 = x0 - q * x1
        y2 = y0 - q * y1
        x0, x1, y0, y1 = x1, x2, y1, y2

a, b = 59, 19

# d, xk, yk = exEuclid(a, b)
# print(d, xk, yk, f", {d} = {a} * {xk} + {b} * {yk}, Ellenorzes: {d == a * xk + b * yk}")

def diophantosz(a = 19, b = 59, c = 1706):
    d, xk, yk = exEuclid(a, b)
    temp = c//d
    x0 = xk * temp
    y0 = yk * temp
    n1 = -x0 / (b//d)
    n2 = y0 / (a//d)
    if n1 > n2:
        temp = n1
        n1 = n2
        n2 = temp
    n1, n2 = int(n1), int(n2)

    for n in range(n1, n2+1):

        x = x0 + n *(b // d)
        y = y0 - n *(a // d)
        if x > 0 and y > 0:
          print (f"{c} = {a} * {x} + {b} * {y}, Ellenorzes: {c == a * x + b * y}")

# diophantosz(200, 500, 5100)

def diophantosz2(a = 19, b = 59, c = 1706):
    d, xk, yk = exEuclid(a, b)
    temp = c//d
    x0 = xk * temp
    y0 = yk * temp
    n1 = -x0 / (b//d)
    n2 = y0 / (a//d)
    if n1 > n2:
        temp = n1
        n1 = n2
        n2 = temp
    n1, n2 = int(n1), int(n2)
    M = []
    for n in range(n1, n2+1):

        x = x0 + n *(b // d)
        y = y0 - n *(a // d)
        if x > 0 and y > 0:
            M += [(x, y)]

    return M
def fel7_2():
    M = diophantosz2(200, 500, 5100)
    print(M)
    x, y = M[0]
    maxi = x + y
    for x, y in M[1:]:
        if x + y > maxi:
            maxi = x + y
    print (f"Maximalisan rendelt telefonok szama: {maxi}")

fel7_2()






