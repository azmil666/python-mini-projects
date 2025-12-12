import random

def dice():
    choice = random.randint(1,6)
    return choice

print(""" Reach score 30 to win ! Land '1' You lose it all ! """)
score=0
final_score=30
start=input("Enter your choice wanna start ? (Y) : ").lower()
if start != "y":
    quit()


while score < final_score:
    role = dice()
    opt = input("Enter any to role (no to stop): ").lower()
    if opt == "no":
        
        print(f"You scored {score} !")
        break
    
    else:
        if role == 1:
            print("Oops u landed 1 , You lost it all ")
            score = 0
        else:    
            score += role
            print(f"You landed {role} and current score is {score} .")

if score == final_score:
    print("You won You Scored Exactly 30 !")
elif score > final_score:
    print(f"You Won You Scored {score} which is more than 30 !")    
else:
    print(f"You are safe you scored {score}")





