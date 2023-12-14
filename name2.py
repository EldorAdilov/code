import re

regex = r"^(\+998\d{2}\s)?\(?\d{3}\)?[\s.-]\d{2}[\s.-]\d{2}$"
regex1 = r"^([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
regex2 = r"[A-Za-z0-9@#$%^&+=]{8,20}"


def is_valid(phone: str) -> str:
    if re.fullmatch(regex, phone):
        return True
    else:
        return False

def is_valid1(email: str) -> str:
    if re.fullmatch(regex1, email):
        return True
    else:
        return False

def is_valid2(parol: str) -> str:
    if re.fullmatch(regex2, parol):
        return True
    else:
        return False

raqam = input("Telefon raqam kiriting: misol(+998XX XXX-XX-XX) ")
emaill= input("Emailingizni kiriting: ")
paroll = input("Parol kiriting: misol(katta va kichik harf va belgilardan, kamida 8 ta belgi bo'lsin) ")
if is_valid(raqam):
    print("Telefon raqamingiz to'g'ri")
else:
    print("Telefon raqamingiz nato'g'ri")

if is_valid1(emaill):
    print("Emailingiz to'g'ri")
else:
    print("Emalingiz nato'g'ri")

if is_valid2(paroll):
    print("Parol to'g'ri")
else:
    print("Parol nato'g'ri")