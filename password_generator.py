import random 
import secrets
import string
def generatepassword():
    characters = string.ascii_letters + string.digits + string.punctuation
    while True:
        length=input("Password length : ")
        try:
            length=int(length)
        except ValueError:
            continue
        password = ''.join(random.choice(characters) for c in range(length))
        print(password)
def generatepasswordsecure():
    characters = string.ascii_letters + string.digits + string.punctuation
    while True:
        length=input("Password length : ")
        try:
            length=int(length)
        except ValueError:
            continue
        password = ''.join(secrets.choice(characters) for c in range(length))
        print(password)
# print("1. Use a strong password generation system\n2. Use a random password generation system")
while True:
    print("1. Use a strong password generation system\n2. Use a random password generation system")
    use=input("Select your option (1/2) : ")
    if use=="1" or use=="Use a strong password generation system" or use=="s" or use=="strong" or use=="Strong":
        generatepasswordsecure()
    elif use=="2" or use=="Use a random password generation system" or use=="r" or use=="random" or use=="Random":
        generatepassword()
    else:
        continue