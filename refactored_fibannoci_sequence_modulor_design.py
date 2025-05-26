import turtle
import math

def setup_turtle(speed=0):# Function to set up the turtle with a given speed
    """Initializes a turtle with the specified speed."""
    t = turtle.Turtle()
    t.speed(speed)# Set the speed of the turtle
    return t # Return the turtle object

def draw_square(t, length):# Function to draw a square with a given length
    """Draws a square with the given side length."""
    for _ in range(4):# Loop to draw each side of the square
        t.forward(length)
        t.left(90)

def draw_fibonacci_spiral(t, n, scale=10):# Function to draw a Fibonacci spiral with a specified number of segments and scale
    """Draws a Fibonacci spiral with 'segments' number of squares and arcs."""
    a, b = 0, 1
    for _ in range(n):# Loop through the number of segments
        side = b * scale # Scale the Fibonacci number for visibility
        draw_square(t, side)
        t.circle(side, 90)
        a, b = b, a + b

def draw_modulor_figure(t, height):
    """Draws a simple human figure based on the golden ratio."""
    phi = 1.618
    navel = height / phi

    # Spine
    t.penup()
    t.goto(0, 0)
    t.setheading(90)
    t.pendown()
    t.forward(height)

    # Head
    t.penup()
    t.goto(0, height)
    t.pendown()
    t.circle(5)

    # Arms
    t.penup()
    t.goto(0, navel)
    t.setheading(0)
    t.pendown()
    t.forward(20)
    t.backward(40)

    # Legs
    for angle in [-60, -120]:
        t.penup()
        t.goto(0, 0)
        t.setheading(angle)
        t.pendown()
        t.forward(30)

def draw_modulor_diagram(t, base_height):
    """Draws the Modulor diagram with labels and a human figure."""
    phi = 1.618
    heights = [base_height / (phi ** i) for i in range(4)]

    t.penup()
    t.goto(0, 0)
    t.setheading(90)
    t.pendown()

    for h in heights:
        t.forward(h)
        t.write(f"{round(h, 1)}", font=("Arial", 10, "normal"))
        t.backward(h)
        t.left(90)
        t.forward(20)
        t.right(90)

    draw_modulor_figure(t, base_height)

def main():
    screen = turtle.Screen()
    screen.title("Fibonacci Spiral + Modulor Diagram")
    screen.bgcolor("white")

    pen = setup_turtle()

    # Draw Fibonacci Spiral
    pen.penup()
    pen.goto(-200, -150)
    pen.setheading(0)
    pen.pendown()
    draw_fibonacci_spiral(pen, n=7)

    # Draw Modulor + Figure
    pen.penup()
    pen.goto(200, -50)
    pen.setheading(90)
    pen.pendown()
    draw_modulor_diagram(pen, base_height=183)

    turtle.done()

main()
