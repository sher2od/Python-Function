def is_palindrome(text: str):
    """
    Berilgan matn palindrom ekanligini tekshiradi.

    Palindrom — bu teskari o‘qilganda ham bir xil bo‘lgan matndir.
    Masalan: 'anna', 'level', '12321'.

    Parametr:
    text (str): Tekshiriladigan matn.

    Natija:
    Agar matn palindrom bo‘lsa, "Bu so'z bir xil" deb chiqaradi.
    Aks holda, "Bir xil emas" deb chiqaradi.
    """
    if text == text[::-1]:
        print("Bu so'z bir xil")
    else:
        print("Bir xil emas")
