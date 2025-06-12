def add(a,b):
    result = a + b
    return result

def subtract(a,b):
    result = a - b
    return result

def multiply(a,b):
    result = a * b
    return result

def divid(a,b):
    result = a / b
    return result
 
def main():
    a = int(input("a >> "))
    op = input("+,/,*,- ")
    b = int(input("b >> "))

    if op == "+":
        print(add(a,b))
    elif op == "-":
        print(subtract(a,b))
    elif op == "*":
        print(multiply(a,b))
    elif op == "/":
        print(divid(a,b))
    else:
        print("error")
        
main()
    




























































