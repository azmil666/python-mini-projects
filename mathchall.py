import time
import random

OPERATORS = ["+","*","-"]

print("MATH CHALLENGE ANSWER ALL 10 QUESTIONS ! ")


def problem():
    left=random.randint(3,12)
    right=random.randint(3,12)
    operators=random.choice(OPERATORS)

    exp = str(left) + " " + operators + " " + str(right)
    answr=eval(exp)
    return answr,exp
input("Enter when ready : ")
time1=time.time()
wrong=0
for i in range(10):
    answr,exp=problem()
    value=9-i

    while True:
        guess = input(f"ANSWER -> Whats {exp} : ")
        if guess == str(answr):
            print(f"Great now {value} more to go ! ")
            break
        else:
            wrong += 1
time2=time.time()
total=round(time2-time1,4)
print(f"You finished the challenge u got {wrong} wrong and it took you {total} seconds ! ")            
