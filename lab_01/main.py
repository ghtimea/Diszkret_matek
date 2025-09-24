def kiir (name1, name2):
    print(f"Hello, {name1}, datum: {name2}")

def osszeg(x, y):
    return x + y

def kulonbs(x, y):
    return x - y

def aritmMuvk(x, y):
    eredmeny1 = x+y
    eredmeny2 = x-y
    eredmeny3 = x*y
    eredmeny4 = x/y
    eredmeny5 = x//y
    eredmeny6 = x%y
    return eredmeny1, eredmeny2, eredmeny3, eredmeny4, eredmeny5, eredmeny6

def elsoFokuEgy (a, b):
    if a != 0: return -b/a
    elif b != 0: return "Nincs megoldas"
    else: "Vegtelen megoldas"



if __name__ == "__main__":
    kiir("Gheorghita Timea", "25/09/24")

    x = input("x= ")
    x= int(x)
    y = input("y= ")
    y= int(y)

    print(osszeg(3, 4)   )
    print(kulonbs(5, 6) )
    e = aritmMuvk(x, y)
    print(e)
    print(f'Osszeg: {e[0]}')





