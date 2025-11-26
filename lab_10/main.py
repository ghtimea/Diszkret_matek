# p = 2*q + 1, ahol p, q primszam
# safeprime: 5 = 2*2 + 1, 7 = 2*3 + 1, 11 = 2*5 + 1
# notsafeprime: 13 = 2*6 + 1, 17 = 2*8 + 1, 19 = 2*9 + 1

from sympy import isprime

def fel_6 (x):
    with open("safe_prime.txt", "w") as f1, open ("not_safe_prime.txt", "w") as f2:
        p = 5;
        sz1, sz2 = 0, 0
        while p <= x:
            q = (p - 1) // 2
            if isprime(q) and isprime(p):
                f1.write(str(p) + "\n")
                sz1 += 1
            else:
                f2.write(str(p) + "\n")
                sz2 += 1
            p += 2
        f1.write("Safe primek szama: " + str(sz1))
        f2.write("Nem safe primek szama: " + str(sz2))

# fel_6(200)
from lab_10.main_09 import eratL

def testMersenne(p):
    if p == 2:
        return True

    Mp = (1 << p) - 1
    s = 4
    for _ in range(p - 2):
        s = (s * s - 2) % Mp

    return s == 0


def fel_7(k):
    primLista = eratL(k)

    for p in primLista:
        if testMersenne(p):
            Mp = (1 << p) - 1
            print(p, Mp)
            k -= 1
            if k == 0:
                return

# fel_7(50)








