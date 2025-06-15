def calculate_age(birth_year: int, current_year: int) -> int:
    """
    Tugilgan yil va joriy yil asosida yoshni hisoblaydi.

    Args:
        birth_year (int): Foydalanuvchining tugilgan yili.
        current_year (int): Hozirgi yil.

    Returns:
        int: Foydalanuvchining yoshi.
    """
    return current_year - birth_year


birth_year = int(input("Tugilgan yilingizni kiriting: "))
current_year = 2025

age = calculate_age(birth_year, current_year)
print(f"Sizning yoshingiz: {age} yosh")

if age >= 18:
    print("Siz balogat yoshiga yetgansiz.")
else:
    print("Siz balogat yoshiga yetmagansiz.")
