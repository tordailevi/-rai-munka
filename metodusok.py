import random

def feladat1():

    szam:int=2

    while (szam % 2 ==0):
        szam:int = int(input("Adjon meg egy páratlan számot: "))
    print(f"A {szam} páratlan")

def feladat2():
    szamok=[]
    szam1:int = int(random.random() * 96) +4 *7
    print(f"{szam1}")
    if (szam1 % 5 == 0):
        szamok.append(szam1)
    print(f"A számok között {len(szamok)} db 5-mal osztható van!")


def feladat3():
    szoveg:str="Szöveg"
    betu:str="a"

    return szoveg, betu

def feladat3_kiiras(szoveg):
    for i in range(0, len(szoveg), 1 ):
        if (i == "a"):
            i+=1
    print(f"A szövegben {i} a betű van!")


def feladat4():
    nevek=[]
    nev= ""

    while ():
        nev:str=str(input("Adjon meg egy nevet: "))
        if nev == "@":
            print("Ne csináld már légyszi.")
            break
        nevek.append(nev)
        return nevek
    print(f"A felhasználó {len(nevek)} nevet adott meg!")

def feladat4_kiiras(nevek):
    print(f"A felhasználó {len(nevek)} nevet adott meg!")
