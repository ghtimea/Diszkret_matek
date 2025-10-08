from datetime import time


def osztasiM1 (n, a =2):
    all = open('hatvany.txt', 'w')
    print('%3s%4s%12s%3s%3i' % ('a', 'i','(a^i)', 'mod', n), file = all)
    for i in range(1, n):
        print ('%3i%4i%10i' % (a, i, pow(a, i, n)), file = all)

    all.close()

    def osztasiM2(n, a=2):
        with open('hatvany.txt', 'w') as all:
            print('%3s%4s%12s%3s%3i' % ('a', 'i', '(a^i)', 'mod', n), file=all)

    for i in range(1, n):
        print('%5i%5i%10i' % (a, i, pow(a, i, n)), file=all)

    def osztasiM3(n):
        with open('hatvanyok.txt', 'w') as all:
            for i in range(1, n):
                print('%4i' % i, file=all, end=' ')
                for a in range(1, n):
                    print('%10i' % pow(a, i, n), file=all, end=' ')
                print(file=all)

    def beolvasFloat(n):
        L = []
        for i in range(n):
            try:
                 L += [float(input("elem = "))]
            except:
                print("hibas bemenet")
                return
        return L

    def myPowLin(x, n):
        res = 1
        for i in range(n):
            res *= x
        return res

    def myPow1(x, n):
        res = 1

        while True:
            if n % 2 == 1:
                res = res * x
            n = n // 2
            if n == 0: break
            x = x * x
        return res

    def myPow2(x, n, m):
        res = 1

        while True:
            if n % 2 == 1:
                res = (res * x)%m
            n = n // 2
            if n == 0: break
            x =( x * x)%m
        return res

    def osztasiM4(n, a=2):
        with open('hatvany.txt', 'w') as all:
            print('%3s%4s%12s%3s%3i' % ('a', 'i', '(a^i)', 'mod', n), file=all)

    for i in range(1, n):
        print('%5i%5i%10i' % (a, i, pow(a, i, n)), file=all)
        print('%5i%5i%10i' % (a, i, myPow2(a, i, n)), file=all)

    def main ():
        x = int (input('x='))
        for n in range (1, 10):
            st=time()
            myPow1(x, 10**n)
            fs = time()
            print(round(fs-st,4))
        print("/n")
        for n in range(1, 16):
            st=time()
            myPowLin(x, 10**n)
            fs = time()
            print(round(fs-ts, 4))

