from turtle import Turtle
import random


COLOR_LIST = ["red","yellow", "green", "orange", "blue", "purple"]
Y_POSITIONS = [-250, -150, -50, 60, 150, 250]

class Racer(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.all_turtles = []
        
        
    def create_racer(self):
        for index_position in range(0,6):
            new_turtle = Turtle(shape="turtle")
            new_turtle.penup()
            new_turtle.speed(5)
            new_turtle.turtlesize(2)
            new_turtle.color(COLOR_LIST[index_position])
            new_turtle.goto(x=-480, y=Y_POSITIONS[index_position])
            self.all_turtles.append(new_turtle)
        
        
    def start_race(self):
         for turtles in self.all_turtles:
             moves = random.randint(0, 10)
             turtles.forward(moves)
         
    def winner(self):
        for turtle in racer.all_turtles:
            if turtle.xcor() > 440:
                race_is_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"You Won! The {winning_color} color is the winner!")
                else:
                    print(f"You Lost! The {winning_color} color is the winner!")
    
    def print_winner(self, user):
        self.user = user
        self.penup()
        self.goto(x=0, y=320)
        self.write(f"Your choice is {user}, good luck!", align="center", font=("courier", 20, "bold"))
        
        
    def print_result(self, final_result):
        self.final_result = final_result
        self.penup()
        self.goto(x=0, y=290)
        self.write(f"The winner is {final_result}!", align="center", font=("courier", 20, "bold"))
        
           
        
        