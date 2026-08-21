from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(width=500, height=400)
screen.colormode(255)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = {
    "Tim": Turtle(),
    "Tom": Turtle(),
    "Liz": Turtle(),
    "Bob": Turtle(),
    "Yvette": Turtle(),
    "Maria": Turtle()
}
positions = [-70,-40,-10,20,50,80]

turtleNameColor = {"name": [], "color": []}

for i, (name, turtle_obj) in enumerate(turtles.items()):
    turtle_obj.color(colors[i])
    turtle_obj.shape("turtle")
    turtle_obj.penup()
    turtleNameColor["name"].append(name)
    turtleNameColor["color"].append(colors[i])
    turtle_obj.goto(x = -230, y = positions[i])

# print(turtleNameColor)
#
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? enter a color: ")
finish_line = 230
race_on = True
while race_on:
    winners = []
    for name, turtle_obj2 in turtles.items():
        forw = random.randint(0,10)
        turtle_obj2.forward(forw)
        if turtle_obj2.xcor() > finish_line:
            winner = turtle_obj2.pencolor()
            winners.append(winner)

    if winners:
        race_on = False
        if len(winners) == 1:
            print(f"{winners[0]} wins the race!")
            if user_bet == winners[0]:
                print(f"You won the bet")
            else:
                print(f"You lost the bet")

        else:
            print(f"It is a draw race between {", ".join(winners)}!")


# print(user_bet.lower())
screen.title("Turtles")
screen.exitonclick()