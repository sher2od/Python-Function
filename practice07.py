

def check_answer(user_answer, correct_answer):
    if user_answer.strip().lower() == correct_answer.strip().lower():
        print("Togri javob!")
    else:
        print("Notogri javob. Togri javob:", correct_answer)

soz = input("O'zbekiston poytaxti >> ")

check_answer(soz,"Toshkent")

