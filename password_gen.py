import random
import string
 

def generate_password(min_length,numbers=True,special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    
    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special    
    pwd = ""
    meet_crit = False 
    has_number = False
    has_special = False

    while not meet_crit or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char
        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True
        meet_crit = True

        if numbers:
            meet_crit = has_number
        if special_characters:
            meet_crit = meet_crit and has_special 
    return pwd
           

min_length=int(input("Enter the length of the password : "))
has_numb=input("Do you want numbers in password (y/n): ").lower() == "y"
has_spcl=input("Do you want spcl characters in password (y/n): ").lower() == "y"

a=generate_password(min_length,has_numb,has_spcl)
print(f"The generated password is = {a}")





        