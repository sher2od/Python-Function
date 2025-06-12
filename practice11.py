def calculate_tax(salary: float) -> float:
    if salary > 5_000_000:
        tax = salary * 0.20  # 20% soliq
    else:
        tax = salary * 0.13  
    return tax

def calculate_net_salary(salary: float) -> float:
    tax = calculate_tax(salary)
    return salary - tax


salary = float(input("Maoshingizni kiriting: "))

tax = calculate_tax(salary)
net_salary = calculate_net_salary(salary)

print(f"Soliq miqdori: {tax:.2f} so'm")
print(f"Toza  maosh: {net_salary:.2f} so'm")
