def calculate_tax(salary: float) -> float:
    """
    Berilgan maoshga qarab soliq miqdorini hisoblaydi.

    Parametrlar:
    salary (float): Ish haqining summasi.

    Return:
    float: Hisoblangan soliq miqdori.
    """
    if salary > 5_000_000:
        tax = salary * 0.20  # 20% soliq
    else:
        tax = salary * 0.13  # 13% soliq
    return tax
    

def calculate_net_salary(salary: float) -> float:
    """
    Soliqdan keyingi sof maoshni hisoblaydi.

    Parametrlar:
    salary (float): Ish haqining summasi.

    Return:
    float: Soliq ushlab qolingandan keyingi sof maosh.
    """
    tax = calculate_tax(salary)
    return salary - tax


salary = float(input("Maoshingizni kiriting: "))

tax = calculate_tax(salary)
net_salary = calculate_net_salary(salary)

print(f"Soliq miqdori: {tax:.2f} so'm")
print(f"Toza  maosh: {net_salary:.2f} so'm")
