def is_even(number: float) -> bool:
    """
    Son juftligini tekshiradi.

    Args:
        number (float): Tekshiriladigan son.

    Returns:
        bool: Agar juft bolsa True, aks holda False.
    """
    return number % 2 == 0

def print_even_message():
    number = float(input("Sonni kiriting >> "))
    if is_even(number):
        print("Bu son JUFT.")
    else:
        print("Bu son TOQ.")

print_even_message()
