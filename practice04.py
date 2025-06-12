def get_grade(score):
    if  100 >= score >= 90:
        print("A")
    elif 90 >= score >= 80:
        print("B")
    elif 80 >= score >= 70:
        print("C")
    elif 70 >= score >= 60:
        print("F")
    else:
        print("Siz bu ball bilan yiqildingiz ")


ball = int(input("Balingizni kiritingchi "))
get_grade(ball)