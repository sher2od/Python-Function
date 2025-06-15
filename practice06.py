def phone_number(num: str) -> None:
    """
    Telefon raqami uzunligini tekshiradi (raqam 9 belgidan iborat bo‘lishi kerak).

    Args:
        num (str): Foydalanuvchi tomonidan kiritilgan telefon raqami (raqamlar matn ko‘rinishida).

    Returns:
        None: Natijani ekranga chiqaradi (True yoki False).
    """
    if len(num) == 9:
        print(True)
    else:
        print(False)


number = input("Telefon raqamingizni kiriting: ")
phone_number(number)
