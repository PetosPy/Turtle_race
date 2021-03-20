from turtle import Turtle, Screen
import random
from racer import Racer

screen = Screen()
screen.setup(height=800, width=1000)


racer = Racer()
user_bet = screen.textinput(title="Make your bet", prompt= "Which turtle will win the race? Enter a colour: ")

race_is_on = False

if user_bet:
    race_is_on = True
    print(f"Your choice is {user_bet}, good luck!")

racer.create_racer()

racer.print_winner(user_bet)
while race_is_on:
    
    racer.start_race()
    # Check for winner
    for turtle in racer.all_turtles:
        if turtle.xcor() > 450:
            race_is_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                racer.print_result(winning_color)
            else:
                racer.print_result(winning_color)
        
        
    
    
    


        

           



























screen.exitonclick()



