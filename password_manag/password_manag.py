from cryptography.fernet import Fernet
MASTER_PASSWORD = "master"


class InvalidMasterPassword(Exception):
    pass


"""def write_key():
    key = Fernet.generate_key()
    with open('key.key','wb') as key_file:
        key_file.write(key) 
write_key()  """

def load_key():
    with open('key.key','rb') as read_file:
        values=read_file.read()
        return values


master_pwd = input("Enter the master password : ")
if master_pwd != MASTER_PASSWORD:
    raise InvalidMasterPassword("Master password is incorrect!")

key = load_key() + master_pwd.encode()
fer = Fernet(key)

def view():
    user=input("Enter accnt for password : ")
    found = False
    with open('password.txt','r') as f:
        for line in f.readlines():
            data = line.rstrip()
            usr , passwd = data.split("|")
            
            if user == usr :
                print("user : " + usr + " | " + "password : " + fer.decrypt(passwd.encode()).decode())
                found = True
                break
    if not found:    
        print("Invalid username or no password for this user. ")


def add():
    name=input("Enter the account name : ")
    pwd=input("Enter the password for accnt : ")

    with open('password.txt','a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode()+ "\n")

                
while True:
    mode = input("Would u like to add new password or view existing ones ? (view/add/q) : ").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid input ! ")
        continue
