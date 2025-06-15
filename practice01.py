def add(a,b):
    result = a + b
    return result
    return result
'''Ikki sonni yigindisi

    Args:
    a(float): birinchi son
    b(float): ikkinchi son

    Returns:
    float:yigindi

    Raises:
    TypeError:type error

    '''

def subtract(a,b):
    result = a - b
    return result

    return result
    '''Ikki sonni ayirmasi

    Args:
    a(float): birinchi son
    b(float): ikkinchi son

    Returns:
    float:ayirmasi

    Raises:
    TypeError:type error

    '''

def multiply(a,b):
    result = a * b
    return result

    '''Ikki sonni kpaytmasi

    Args:
    a(float): birinchi son
    b(float): ikkinchi son

    Returns:
    float:kopaytmasi

    Raises:
    TypeError:type error

    '''


def divid(a,b):
    result = a / b
    return result

    '''Ikki sonni bolim=nmasi

    Args:
    a(float): birinchi son
    b(float): ikkinchi son

    Returns:
    float:bolinmasi

    Raises:
    TypeError:type error

    '''
 
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
    
