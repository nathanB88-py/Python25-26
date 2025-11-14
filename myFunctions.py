import turtle
import math

# --- Setup ---
turtle.setup(800, 800)
turtle.bgcolor("black")

bob = turtle.Turtle()
bob.speed(0)
bob.hideturtle()
turtle.tracer(0, 0)


def draw_circle(radius, color):
    """Draw a filled circle centered on screen."""
    bob.penup()
    bob.goto(0, -radius)
    bob.pendown()
    bob.fillcolor(color)
    bob.begin_fill()
    bob.circle(radius)
    bob.end_fill()

def draw_ring(radius, thickness, color):
    """Draw a ring (circle outline with given thickness)."""
    bob.penup()
    bob.goto(0, -radius)
    bob.pendown()
    bob.pensize(thickness)
    bob.pencolor(color)
    bob.circle(radius)

def draw_tomoe(radius, angle):
    """Draw tomoe-like comma shapes along a circle."""
    bob.penup()
    bob.goto(0, 0)
    bob.setheading(angle)
    bob.forward(radius)
    bob.pendown()

    bob.setheading(angle + 90)
    bob.fillcolor("black")
    bob.begin_fill()
    bob.circle(12, 180)
    bob.left(120)
    bob.forward(25)
    bob.left(120)
    bob.circle(12, 180)
    bob.end_fill()

def gradient_rinnegan():
    """Draw gradient purple background for Rinnegan illusion."""
    colors = "#1a001a", "#260026", "#330033", "#400040",
    "#4d004d", "#590059", "#660066", "#730073",
    "#800080", "#8c008c", "#990099", "#a600a6",
    "#b300b3", "#bf00bf", "#cc00cc"

    r = 300
    for c in colors:
        draw_circle(r, c)
        r -= 15

# --- Draw the Rinnegan ---
gradient_rinnegan()

# Concentric rings
for r in range(80, 301, 40):
    draw_ring(r, 4, "#220022")

# Central pupil
draw_circle(25, "black")

# Tomoe details (3 at 120° intervals)
for angle in [0, 120, 240]:
    draw_tomoe(140, angle)

# Additional inner tomoe ring
for angle in [60, 180, 300]:
    draw_tomoe(80, angle)

turtle.update()
turtle.done()



  
