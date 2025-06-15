def get_grade(score: int) -> None:
    """
    Ball asosida bahoni chiqaradi.

    Args:
        score (int): Talabaning olgan balli (0 dan 100 gacha bo'lishi kerak).

    Returns:
        None: Natijani ekranga chiqaradi (print).

    Baholar:
        90-100 -> A
        80-89  -> B
        70-79  -> C
        60-69  -> F
        0-59   -> "Siz bu ball bilan yiqildingiz"
    """
    if 100 >= score >= 90:
        print("A")
    elif 90 > score >= 80:
        print("B")
    elif 80 > score >= 70:
        print("C")
    elif 70 > score >= 60:
        print("F")
    else:
        print("Siz bu ball bilan yiqildingiz")


ball = int(input("Balingizni kiritingchi: "))
get_grade(ball)
