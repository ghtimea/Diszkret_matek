#7.labor feladatai
#3.feladat
def my_is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def feladat3 ():
    with open("primes.txt", "w") as f:
        count=0
        for num in range(2, 10**7):
            if my_is_prime(num):
                f.write(str(num) + " ") #fajlba csak str vagy bytes tipusu adatot lehet irni
                count += 1
                if count % 10 ==0:
                    f.write("\n")
feladat3()
from random import randint, getrandbits
from sympy import isprime #teszteli egy egesz szamrol, hogy primszam-e
def feladat1(k):
    a = 10**(k-1)
    b = 10**k-1
    while True:
        nr = randint(a, b)
        if isprime(nr):
        #if my_is_prime(nr): #csak akkor ha k <= 15
            return nr

##def eratL_(n):
    L = [True] * (n + 1)
    i = 3
    while i * i <= n + 1:
        if L[i] == True:
            for j in range(i * i, n + 1, i): L[j] = False
        i += 2
    Prim = [2]
    for i in range(3, len(L), 2):
        if L[i]: Prim += [i]
    return Prim

def eratL(n):
    L = [True] * (n + 1)
    i = 5
    while i * i <= n + 1:
        if L[i] == True:
            for j in range(i * i, n + 1, i): L[j] = False
        i += 2
        if L[i] == True:
            for j in range(i * i, n + 1, i): L[j] = False
        i += 4
    Prim = [2, 3]
    for i in range(5, len(L) - 2, 6):
        if L[i]: Prim += [i]
        if L[i + 2]: Prim += [i + 2]
    return Prim

#print (feladat1(150))
#print(feladat1(15))
#primlista = eratL(10**7)
#print(len(primlista), primlista)
#print(f'primszamok szama:{len(primlista)}, az utolso primszam:{primlista[-1]}')

def eratAB(a, b):
    if b <= 10:
        return [2,3,5,7]
    L = [True] * (b + 1)
    i = 5
    while i * i <= b + 1:
        if L[i] == True:
            for j in range(i * i, b + 1, i): L[j] = False
        i += 2
        if L[i] == True:
            for j in range(i * i, b + 1, i): L[j] = False
        i += 4
    #Prim = [2, 3]
    Prim = []
    for i in range(5, len(L) - 2, 6):
        if i >= a:
            if L[i]: Prim += [i]
            if L[i + 2]: Prim += [i + 2]
    return Prim
k=1
a=10**(k-1)
b=10**k-1
#print (eratAB(a, b))

#feladat4
def prevPrime(nr):
    if nr == 2:
        return 2
    elif nr == 3:
        return 2

    if nr%2 == 0:
        prev = nr - 1
    else:
        prev = nr - 2
    while prev >= 3:
        if isprime(prev):
            return prev
        prev -= 2

def nextPrime(nr):
    if nr == 2:
        return 3
    if nr &1 == 0: #parossag vizsgalata bitmuvelet
        nr += 1
    else:
        nr += 2
    while True:
        if isprime(nr):
            return nr
        nr += 2

def feladat4():
    #nr = getrandbits(1024) #1024 bites random szam generalasa
    nr = getrandbits(16)
    print(f'szam:{nr}')
    print(f'kovetkezo prim:{prevPrime(nr)}')
    print(f'elozo prim:{prevPrime(nr)}')

# feladat4()

import sympy.ntheory as nth
def fel5():
    nr = 5**7 * 11**4 * 41**7 * 101**5 * 1789**3
    print(f'szam:{nr}')
    result = nth.factorint(nr)
    print(result)
    print(list(result)[-1])
    print(list(result)[0])
    print(list(result.keys())[0])
    print(list(result.values())[0])

# fel5()
