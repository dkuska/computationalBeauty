# Simple implementation of l-systems using python turtle graphics
# More Information can be found here: https://en.wikipedia.org/wiki/L-system
# L-Systems can be used to create fractals or artificial plants
# To get good results, play around with the axiom, angle and system_rules
# Additional l-system encodings can be found in lsystem_encodings.py

import turtle

# Constants to create the images
# Rules of the current image, creates a tree-like structure
system_rules = {"X": "F-[[X]+X]+F[+FX]-X", "F": "FF"}
axiom = "X"
angle = 25

iterationNr = 5  # Amount of times, that rule replacement
stepSize = 5  # Amount of pixels the turtle takes with each step
initialHeading = 90  # Initial angle, in which the turtle is 'looking'. 0 - straight up, 90 - to the right
initialPos = (0, 0)  # Initial position on the plane, (0,0) corresponds to the middle of the field

# pen and background color as hex rgb values, pen size in pixels
pen_color = "#000000"
background_color = "#FFFFFF"
pen_size = 3

screen = turtle.getscreen()


# Setup of the turtle
def set_turtle(alpha_zero):
    global screen
    # Make a new invisible turtle
    turtle.hideturtle()
    r_turtle = turtle.Turtle()
    r_turtle.hideturtle()

    # Set initial angle for turtle
    r_turtle.setheading(alpha_zero)

    # Set colors and pensize
    screen = r_turtle.getscreen()
    r_turtle.pensize(pen_size)
    screen.bgcolor(background_color)
    r_turtle.pencolor(pen_color)

    # Place turtle at initial coordinates)
    r_turtle.penup()
    r_turtle.goto(initialPos)
    r_turtle.pendown()

    # Makes it, so that drawings appear instantly. Screen gets manually refreshed, after everything gets drawn
    turtle.tracer(0, 0)

    return r_turtle


# Converts model-string into commands for the turtle
def draw_lsystem(turtle_, model, step_size, angle_):
    stack = []
    for command in model:
        turtle_.pendown()
        if command in ['F', 'A']:
            turtle_.forward(step_size)
        elif command == 'B':
            turtle_.backwards(step_size)
        elif command == 'f':
            turtle_.penup()
            turtle_.forward(step_size)
            turtle_.down()
        elif command == '+':
            turtle_.left(angle_)
        elif command == '-':
            turtle_.right(angle_)
        elif command == '[':
            stack.append((turtle_.position(), turtle_.heading()))
        elif command == ']':
            turtle_.penup()
            pos, head = stack.pop()
            turtle_.setpos(pos)
            turtle_.setheading(head)


# Used to expand the model-strings, either returns a rule for a given character or the character itself, if no rules apply to it
def rule(argument):
    if argument in system_rules:
        return system_rules[argument]
    return argument


# Deterministically creates a model consisting of commands for the turtle
# From the starting axiom and an iterationNr create a model by replacing each symbol with the body of the rule containing it
def generate_model(axiom_, iteration_nr_):
    model = [axiom_]
    for rounds in range(iteration_nr_):
        next_seq = model[-1]
        next_axiom = [rule(char) for char in next_seq]
        model.append(''.join(next_axiom))
    return model


def main():
    # Generate a model from the axiom, rules and iterationNr
    model = generate_model(axiom, iterationNr)

    # initialize turtle
    r_turtle = set_turtle(initialHeading)

    # Draw the l-system on the screen using the parameters
    draw_lsystem(r_turtle, model[-1], stepSize, angle)

    screen.update()
    screen.exitonclick()


main()
