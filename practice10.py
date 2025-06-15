def parol_tekshir(password: str) -> None:
    """
    Parol kuchini tekshiradi va foydalanuvchiga xabar beradi.

    Args:
        password (str): Foydalanuvchi tomonidan kiritilgan parol.

    Returns:
        None: Faqat natijani ekranga chiqaradi (print).
        
    Qoidalar:
        - Agar parol uzunligi 8 ta belgidan ko‘p bo‘lsa: kuchli parol deb hisoblanadi.
        - Aks holda: kuchsiz deb hisoblanadi.
    """
    if len(password) > 8:
        print("Parol kuchli — buzib bo‘lmaydi.")
    else:
        print("Parol kuchsiz — xavfli.")


parol = input("Parol kiriting >> ")
parol_tekshir(parol)

