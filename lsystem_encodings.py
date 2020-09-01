#Koch Snowflake
SYSRULES = {"F":"F+F--F+F"}
axiom = " F++F++F"
angle = 60

#Koch Kurve 2
SYSRULES = {"F":"F+F-F-F+F"}
axiom ="F+F+F+F"
angle = 90

#QUADRATIC KOCH ISLAND
axiom = "F+F+F+F"
SYSRULES={"F":"F+F-F-FFF+F+F-F"}
angle = 90

#QUADRATIC KOCH ISLAND2
axiom = "F+F+F+F"
SYSRULES={"F":"F-FF+FF+F+F-F-FF+F+F-F-FF-FF+F"}
angle = 90

#KOCH CURVE
axiom = "F+F+F+F"
angle = 90
SYSRULES={"F":"F+F-F-FF+F+F-F"}

#Sierpinski
SYSRULES = {"A":"+F-A-F+", "F":"-A+F+A-"}
axiom = "A++A++A"
angle = 60

#SQUARE SIERPINSKI
axiom = "F+XF+F+XF"
SYSRULES= {"X":"XF-F+F-XF+F+XF-F+F-X"}
angle = 90

#Drachenkurve
SYSRULES = { "X":"X+YF+", "Y":"-FX-Y"}
axiom = "FX"
angle = 90

#TRIANGLE
axiom = "F+F+F"
SYSRULES = {"F":"F-F+F"}
angle = 120

#CROSS
axiom = "F+F+F+F"
angle = 90
SYSRULES={"F":" F+F-F+F+F"}

#TILES
axiom = "F+F+F+F"
angle = 90
SYSRULES={"F":"FF+F-F+F+FF"}

#RINGS
axiom = "F+F+F+F"
angle = 90
SYSRULES={"F":" FF+F+F+F+F+F-F"}

#KRISHNA ANKLETS
axiom = "-X--X"
SYSRULES={"X":"XFX--XFX"}
angle = 45

#BOARD
axiom = " F+F+F+F"
SYSRULES={"F":" FF+F+F+F+FF"}
angle = 90

#FASS
# Quadratic Gopher
axiom = "-YF"
SYSRULES={"X":"XFX-YF-YF+FX+FX-YF-YFFX+YF+FXFXYF-FX+YF+FXFX+YF-FXYF-YF-FX+FX+YFYF-",
"Y":"+FXFX-YF-YF+FX+FXYF+FX-YFYF-FX-YF+FXYFYF-FX-YFFX+FX+YF-YF-FX+FX+YFY"}
angle = 90
#Hexagonal Gopher
axiom = "XF"
SYSRULES={"X":"X+YF++YF-FX--FXFX-YF+","Y":"-FX+YFYF++YF+FX--FX-Y"}
angle = 60


###PLANTS
# Wheat
SYSRULES = {"X":"F-[[X]+X]+F[+FX]-X", "F":"FF"}
axiom = "X"
angle = 25

#Sticks
SYSRULES = {"X":"F[+X]F[-X]+X", "F":"FF"}
axiom = "X"
angle = 20

#bush
axiom = "F"
angle = 22.5
SYSRULES = {"F":"FF-[-F+F+F]+[+F-F-F]"}

#bush2
axiom = "F"
angle = 20
SYSRULES = {"F":"F[+F]F[-F][F]"}

#Pentadendrite
SYSRULES = {"F":"F-F-F++F+F-F"}
axiom = "F-F-F-F-F"
angle = 72

