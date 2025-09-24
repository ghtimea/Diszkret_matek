import math


def osszeg(x, y):
    return x + y


def kulombseg(x, y):
    return x - y


def szorzat(x, y):
    return x * y


def hanyados(x, y):
    return x / y


def maradek(x, y):
    return x % y


def aritMuveletek(x, y):
    eredmeny1 = x + y
    eredmeny2 = x - y
    eredmeny3 = x * y
    eredmeny4 = x / y  # valos osztas
    eredmeny5 = x // y  # osztasi egesz resz
    eredmeny6 = x % y  # osztasi maradek
    return eredmeny1, eredmeny2, eredmeny3, eredmeny4, eredmeny5, eredmeny6


def myMax(x, y):
    if x > y: return x
    if x <= y: return y


def elsoFokuEgyen(a, b):
    if a != 0:
        return -b / a
    elif b == 0:
        return 'Nincs megoldas'
    else:
        return 'Vegtelen megoldas'


from math import sqrt


def masodFokuEgyen(a, b, c):
    delta = b * b - 4 * a * c
    if delta < 0:
        return 'Komplex gyok'
    temp = sqrt(delta)
    x1 = (-b + temp) / (2 * a)
    x2 = (-b - temp) / (2 * a)
    return x1, x2


def myFloor(a):
    if a > 0: return int(a)
    if a == int(a): return int(a)
    return int(a) - 1


def myCeiling(a):
    if a < 0: return int(a)
    if a % 1 == 0: return int(a)
    return int(a) + 1


def bitToByte(bit):
    return myCeiling(bit / 8)


if __name__ == '__main__':
    # print(osszeg(1, 2))
    # print(kulombseg(2, 1))
    # print(szorzat(2, 2))
    # print(hanyados(4, 2))
    # print(maradek(4, 2))
    # x = int(input('x= '))
    # y = int(input('y= '))

    # m = elsoFokuEgyen(x, y)
    # print(f'Az {x}*x+{y} = 0 egyenlet megoldasa: {m}')

    # m = myMax(x,y)

    # e = aritMuveletek(x, y)
    # print(e)

    # a = int(input('a= '))
    # b = int(input('b= '))
    # c = int(input('c= '))

    # m = masodFokuEgyen(a, b, c)
    # print(f'A {a}*x^2 + {b}*x + {c} = 0 egyenlet megoldas: {m}')

    # a = float(input('a = '))
    # m1 = myFloor(a)
    # m2 = myCeiling(a)
    # print(f'Also egesz resz: {m1}')
    # print(f'Felso egesz resz: {m2}\n')

    a = int(input('a = '))

    m = bitToByte(a)

    print(f'Byte merete: {m}')