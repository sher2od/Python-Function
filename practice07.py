def ask_question() -> str:
    """
    Foydalanuvchiga savol beradi va javobini qaytaradi.

    Returns:
        str: Foydalanuvchining kiritgan javobi.
    """
    print("Savol: O‘zbekiston poytaxti qaysi shahar?")
    user_answer = input("Javobingiz: ")
    return user_answer.strip()


def check_answer(user_answer: str, correct_answer: str) -> None:
    """
    Foydalanuvchining javobini to‘g‘ri javob bilan solishtiradi va natijani chiqaradi.

    Args:
        user_answer (str): Foydalanuvchining kiritgan javobi.
        correct_answer (str): To‘g‘ri javob.
    """
    if user_answer.lower() == correct_answer.lower():
        print("To‘g‘ri javob! 👏")
    else:
        print(f"Noto‘g‘ri. To‘g‘ri javob: {correct_answer}")


def main():
    correct = "Toshkent"
    user_ans = ask_question()
    check_answer(user_ans, correct)


main()
