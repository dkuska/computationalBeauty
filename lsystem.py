import turtle

#bush2
axiom = "F"
angle = 20
SYSRULES = {"F":"F[+F]F[-F][F]"}


iterationNr = 4
stepSize = 15
initialHeading =  90

initialPos = (-0,-300)

pensz = 3

penclr = "#000000"
bgclr = "#FFFFFF"# "#E9E7DA" #

saveStr = "./plants/rbush2.eps"



screen = turtle.getscreen()

def set_turtle(alpha_zero):

    turtle.hideturtle()
    r_turtle = turtle.Turtle()  # recursive turtle
    r_turtle.screen.title("L-System Derivation")

    r_turtle.speed(0)  # adjust as needed (0 = fastest)
    r_turtle.setheading(alpha_zero)  # initial angle
    r_turtle.hideturtle()

    r_turtle.pensize(pensz)

    r_turtle.penup()
    r_turtle.goto(initialPos)
    r_turtle.pendown()

    screen = r_turtle.getscreen()
   # screen.tracer(0,0)
    screen.bgcolor(bgclr)
    r_turtle.pencolor(penclr)


    return r_turtle

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

def rule(argument):
    if argument in SYSRULES:
        return SYSRULES[argument]
    return argument

def generateModel(axiom, iterationNr):
    model = [axiom]
    for round in range(iterationNr):
        next_seq = model[-1]
        next_axiom = [rule(char) for char in next_seq]
        model.append(''.join(next_axiom))
    return model

def main():

    #Generate a model from the axiom, rules and iterationNr
    #Model can also be used to
    model = generateModel(axiom,iterationNr)

    #init turtle
    r_turtle = set_turtle(initialHeading)

    draw_lsystem(r_turtle, model[-1],stepSize, angle)

   # screen.update()
  #  screen.getcanvas().postscript(file=saveStr)
    screen.exitonclick()

main()


