import turtle
import time
import random

WIDTH, HEIGHT = 500,500
COLORS = [
    "firebrick", "cyan", "darkblue", "aquamarine", "deeppink",
     "bisque", "black", "blue",
    "blueviolet", "brown", "burlywood", "cadetblue", "green",
    "chocolate", "coral", "cornflowerblue"]

def get_number_of_racers():
    racers = int(input("Enter no of racers you wanna input (2-10) : "))
    while racers <=1 or racers > 10 :
        print("Please enter a valid number.")
        racers = int(input("Enter no of racers you wanna input (2-10) : "))
    return racers     

def race(colors):
    turtles = create_turtles(colors)
    while True:
        for racer in turtles:
            distance = random.randrange(1,20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 -10 :
                return colors[turtles.index(racer)]


def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors)+ 1)

    for i,color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)

        racer.penup()
        racer.setpos( -WIDTH//2 + (i+1) * spacingx, -HEIGHT//2 +20)
        racer.pendown()
        turtles.append(racer)
    return turtles



def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title('Turtle Racing')

racers = get_number_of_racers()
init_turtle()
random.shuffle(COLORS)
colors = COLORS[:racers]
print(colors)
winner = race(colors)
print("The winner is the turtle : ",winner)
time.sleep(5)