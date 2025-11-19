from decimal import Decimal, getcontext

def myPi ():
    getcontext().prec = 500
    res = 0
    for x in range (3, 0, -1):
        a = x * x
        b = 2 * x + 1
        res = a / (b + res)
    return 4 / (1 + res)

def writeFile(functionName = myPi() ,filename = "pi.txt"):
    res = functionName
    egesz = str(int(res))
    tort = str(res - egesz)
    with open(filename, "w") as f:
        f.write(egesz)
        f.write(tort)


writeFile(filename = "pi.txt")
# getcontext().prec = 500
# print (myPi())