# Simple implementation of l-systems using python turtle graphics
# More Information can be found here: https://en.wikipedia.org/wiki/L-system
# L-Systems can be used to create fractals or artificial plants
# To get good results, play around with the axiom, angle and SYSRULES
# Additional l-system encodings can be found in lsystem_encodings.py

import turtle

# Constants to create the images
# Rules of the current image, creates a tree-like structure
axiom = "F"
angle = 20
SYSRULES = {"F": "F[+F]F[-F][F]"}

iterationNr = 4  # Amount of times, that rule replacement
stepSize = 15  # Amount of pixels the turtle takes with each step
initialHeading = 90  # Initial angle, in which the turtle is 'looking'. 0 - straight up, 90 - to the right
initialPos = (0, 0)  # Initial position on the plane, (0,0) corresponds to the middle of the field

# pen and background color as hex rgb values, pen size in pixels
penclr = "#000000"
bgclr = "#FFFFFF"
pensz = 3

screen = turtle.getscreen()

# Setup of the turtle
def set_turtle(alpha_zero):
    # Make a new invisible turtle
    turtle.hideturtle()
    r_turtle = turtle.Turtle()
    r_turtle.hideturtle()

    #Set initial angle for turtle
    r_turtle.setheading(alpha_zero)

    #Set colors and pensize
    screen = r_turtle.getscreen()
    r_turtle.pensize(pensz)
    screen.bgcolor(bgclr)
    r_turtle.pencolor(penclr)

    #Place turtle at initial coordinates)
    r_turtle.penup()
    r_turtle.goto(initialPos)
    r_turtle.pendown()

    #Makes it, so that drawings appear instantly. Screen gets manually refreshed, after everything gets drawn
    turtle.tracer(0,0)

    return r_turtle


# Converts model-string into commands for the turtle
def draw_lsystem(turtle, model, stepSize, angle):
    stack = []
    for command in model:
        turtle.pendown()
        if command in ['F', 'A']:
            turtle.forward(stepSize)
        elif command == 'B':
            turtle.backwards(stepSize)
        elif command == 'f':
            turtle.penup()
            turtle.forward(stepSize)
            turtle.down()
        elif command == '+':
            turtle.left(angle)
        elif command == '-':
            turtle.right(angle)
        elif command == '[':
            stack.append((turtle.position(), turtle.heading()))
        elif command == ']':
            turtle.penup()
            pos, head = stack.pop()
            turtle.setpos(pos)
            turtle.setheading(head)

#Used to expand the model-strings, either returns a rule for a given character or the character itself, if no rules apply to it
def rule(argument):
    if argument in SYSRULES:
        return SYSRULES[argument]
    return argument

#Deterministically creates a model consisting of commands for the turtle
#From the starting axiom and an iterationNr create a model by replacing each symbol with the body of the rule containing it
def generateModel(axiom, iterationNr):
    model = [axiom]
    for rounds in range(iterationNr):
        next_seq = model[-1]
        next_axiom = [rule(char) for char in next_seq]
        model.append(''.join(next_axiom))
    return model


def main():
    # Generate a model from the axiom, rules and iterationNr
    model = generateModel(axiom, iterationNr)

    # initialize turtle
    r_turtle = set_turtle(initialHeading)

    # Draw the l-system on the screen using the parameters
    draw_lsystem(r_turtle, model[-1], stepSize, angle)
    
    screen.update()
    screen.exitonclick()


main()
