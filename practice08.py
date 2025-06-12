def c_to_f(celsius):
    return (celsius * 9/5) + 32

def f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5/9

print("==========Temperatura aylantirish===========")
print("1. Celsius → Fahrenheit")
print("2. Fahrenheit → Celsius")

tanlov = input("Tanlovingizni kiriting (1 yoki 2): ")

if tanlov == "1":
    c = float(input("Celsius qiymatini kiriting: "))
    f = c_to_f(c)
    print(f"{c}°C = {f:.2f}°F")
elif tanlov == "2":
    f = float(input("Fahrenheit qiymatini kiriting: "))
    c = f_to_c(f)
    print(f"{f}°F = {c:.2f}°C")
else:
    print("Notogri tanlov!")
