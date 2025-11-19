def argumentek1(*argument):
    if argument == ():
        print('ures argumentum tuple')
        return
    print(argument)
    for a in argument:
        print(a, end = ' ')

    def myPow2(x, n, m):
        res = 1
        while n != 0:
            if n % 2 == 1:
                res = (res * x) % m
            n = n // 2
            x = (x * x) % m
        return res

    def myPow3(x, n, *m):
        if m == ():
            return myPow2(x, n)

        else: return myPow2(x, n, m[0])
    print(f'myPow3(2, 10`)')
    print(f'myPow3(2, 10, 7)')

    def myPowConstTime(x, n, m):
        res = (x * x) % m

        binN = bin(n)[2:]
        for b in binN[::-1]:
            if b == '0':
                res = (res * x) % m
                x = (x * x) % m
            else:
                x = (res * x) % m
                res = (res * res) % m
        return x






