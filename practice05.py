from random import randint

password = randint(1,10)

def sirli_son(n):
    if n == password:
        print("Topdingiz")
    else:
        print("Toplomadingiz")

number = int(input("Butun son kiriting "))
sirli_son(number)