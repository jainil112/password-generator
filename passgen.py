import string
import random

def gen():
    s1 = string.ascii_letters

    s2 = string.digits

    s3 = string.punctuation

    passlen = int(input("Enter the password length: "))

    s=[]
    s.extend(s1)
    s.extend(s2)
    s.extend(s3)

    random.shuffle(s)

    pswd = ("".join(s[0:passlen]))
    print(pswd)

gen()