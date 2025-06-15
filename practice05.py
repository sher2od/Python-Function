from random import randint

password = randint(1, 10)

def check_guess(secret: int, guess: int) -> bool:
    """
    Foydalanuvchi taxmini togriligini tekshiradi.

    Args:
        secret (int): Kompyuter tanlagan sirli son.
        guess (int): Foydalanuvchi kiritgan son.

    Returns:
        bool: True agar togri topsa, False aks holda.
    """
    return secret == guess

def print_result():
    guess = int(input("1 dan 10 gacha son kiriting: "))
    if check_guess(password, guess):
        print("Topdingiz!")
    else:
        print(f"Topolmadingiz! Togri javob: {password}")

print_result()



