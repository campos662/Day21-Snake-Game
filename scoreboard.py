from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.higher_score = int(self.get_higher_score())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Higher score: {self.higher_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.higher_score:
            self.higher_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.score))
            self.score = 0
        self.score = 0

    def get_higher_score(self):
        with open("data.txt") as file:
            contents = file.read()
            return contents





    #def game_over(self):
     #   self.goto(0, 0)
      #  self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
