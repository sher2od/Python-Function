def is_palindrome(text: str):
    if text[::-1] == text:
        print("Bu soz bir xil")
    else:
        print("Birxil emas")

matin = input("matin >> ")
is_palindrome(matin)