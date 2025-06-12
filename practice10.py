def parol_tekshir(password):
    if len(password) > 8:
        print("parol kuchli buzib bolamaydi")
    else:
        print("Parol kuchsiz")

parol = input("Parol kiriting >> ")
parol_tekshir(parol)

