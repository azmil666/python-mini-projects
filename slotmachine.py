import time
import sys
import random 
balance=0

def deposit():
    global balance
    amnt = int(input("Enter money you wanna deposit : "))
    while amnt < 0 :
        print("please enter valid number ")
        amnt = int(input("Enter money you wanna deposit : "))
        

    balance = balance + amnt
    print(f"You deposited {amnt}.Your current balance is {balance}.")
    return balance
    
def slotmachine():
    choice = ["🟥","🟦","🟩"]
    print(choice)
    input(" Press button to start : ")
    

    slot=[]
    for i in range(3):
        a=random.choice(choice)
        for i in range(10):
            sys.stdout.write("\rSpinning... " + random.choice(choice))
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write("\rStopped on: " + a + "   \n")
        sys.stdout.flush()
        slot.append(a)
    return slot

def logic():
        global balance
        a=input("You wanna start the game (press any) s to stop ? :").lower()
        if a == "s":
            return False
        
        bet=int(input("Enter amount u wanna bet on : "))
        if bet>0 and bet <= balance:
            slots=slotmachine()
            if slots[0]==slots[1]==slots[2]:
                balance = balance + (2*bet)
                print(f"You betted {bet} and now have yourself {balance} .")
                keep=input("wanna keep playing or quit? (q for quit) : ").lower()
                if keep == "q":
                    return False
            else:
                balance = balance - bet    
                print(f"You lost {bet} and now have yourself {balance} .")
                keep=input("wanna keep playing or quit? (q for quit) : ").lower()
                if keep == "q":
                    return False
        else:
            print("Invalid BET")
        return True

print("=" * 67)
print("SLOT MACHINE") 
print("FOR EACH LOSS YOU LOSE THE BET WHEN U WIN ITS DOUBLE")  
print("=" * 67)
while True:
    choice=input("You wanna deposit (y/n) and other to exit : ").lower()
    if choice == "y":
        balance=deposit()
        while logic():
            pass
        #choice=input("Enter anything else than y to exit this window : ")
    elif choice == "n":
        while logic():
            pass
        #choice=input("Enter anything else than n to exit this window : ")
    else :
        break
print(f"After all your efforts you now have {balance}")    



