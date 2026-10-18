from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open (r"C:\Users\imraa\Desktop\data.txt", mode = "r") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.goto(-150, 260)
        self.hideturtle()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="left", font=("Arial", 20, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open (r"C:\Users\imraa\Desktop\data.txt", mode = "w") as file:
                file.write(str(self.score))
        # self.score = 0
        self.update_scoreboard()


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

