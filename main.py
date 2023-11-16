import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen_height = 400
top_margin = 20
bottom_margin = 20

# Set up the screen
screen.setup(width=500, height=screen_height)

# Define colors for turtles
color = ["red", "green", "yellow", "blue", "orange", "purple", "pink", "brown", "black", "violet"]

# Set the maximum number of turtles
max_turtles = 10


def create_turtles(turtles):
    # Initialize an empty list to store turtle objects
    turtle_list = []

    # Calculate the total space available for the turtles
    available_height = screen_height - top_margin - bottom_margin

    # Calculate the gap between turtles
    gap = available_height / (turtles - 1)

    for i in range(turtles):
        # Create a turtle object with a specified shape
        turtle_obj = Turtle(shape="turtle")
        turtle_obj.color(color[i])

        # Calculate the y-coordinate for each turtle
        y_coordinate = -(screen_height / 2) + top_margin + i * gap

        # Set up the turtle's initial position
        turtle_obj.penup()
        turtle_obj.goto(x=-230, y=y_coordinate)
        turtle_obj.pendown()

        # Add the turtle object to the list
        turtle_list.append(turtle_obj)
    return turtle_list


def start_race(turtles, user_bet):
    race = True
    result = []
    while race:
        for turtle_item in turtles:
            turtle_item.penup()
            turtle_item.forward(random.randint(0, 10))
            if turtle_item.xcor() >= 230:
                turtle_color = turtle_item.color()
                if turtle_item.color() == user_bet:
                    result.append("Yayyy!!! You Win :)")
                    result.append(f"The winner turtle color is {turtle_color[0]}")
                else:
                    result.append("Sorry!!! You Lose :)")
                    result.append(f"The winner turtle color is {turtle_color[0]}")
                race = False
                break
    return result


def get_user_input():
    # Ensure the user enters a valid number of turtles (less than or equal to 10)
    while True:
        no_of_turtles = screen.textinput(title=f"Number of Turtles in this Race (Max: {max_turtles})",
                                         prompt="Please enter the number of turtles you want in this race: ")

        if no_of_turtles.isdigit() and 1 <= int(no_of_turtles) <= max_turtles:
            break

    no_of_turtles = int(no_of_turtles)

    # Get user's bet for the race
    user_bet = screen.textinput(title="Make Your Bet",
                                prompt=f"Which turtle will win the race? Enter the color [{', '.join(color[:no_of_turtles])}]: ")

    return no_of_turtles, user_bet


while True:
    user_input = get_user_input()
    turtle_list = create_turtles(user_input[0])
    winner = start_race(turtle_list, user_input[1])
    title = winner[0]
    message = winner[1]
    play = screen.textinput(title=title,
                            prompt=f"{message}. Do you want to play the game again? Type 'yes' or 'no': ")
    if play.lower() == 'no':
        turtle.bye()
    else:
        turtle.clearscreen()
