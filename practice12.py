def calculate_bmi(weight: float, height: float) -> float:
    bmi = weight / (height ** 2)
    return bmi

def bmi_status(bmi: float) -> str:
    if bmi < 18.5:
        return "Ozginasiz (Underweight)"
    elif 18.5 <= bmi < 25:
        return "Normalsiz (Normal weight)"
    elif 25 <= bmi < 30:
        return "Ortiqcha vazn (Overweight)"
    else:
        return "Semizlik (Obese)"

# Foydalanuvchidan og‘irlik va bo‘y olish
weight = float(input("Ogirligingizni kiriting (kg): "))
height = float(input("Boyingizni kiriting (metrda): "))

# BMI hisoblash
bmi = calculate_bmi(weight, height)
status = bmi_status(bmi)

# Natijalarni chiqarish
print(f"BMI (tana massasi indeksi): {bmi:.2f}")
print(f"Holatingiz: {status}")
