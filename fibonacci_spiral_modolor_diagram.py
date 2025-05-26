"""The program is supposed to draw the infamous fibannocci sequence spiral and the modolor diagram using turtle graphics"""

import turtle # import turtle graphics library
import math #import the modules for math


def draw_fibonacci_spiral(t, n):# function to draw fibonacci spiral with parameters t for turtle and n for number of segments
    """Draws a Fibonacci spiral with n segments."""
    a, b = 0, 1  # Initialize the first two Fibonacci numbers
    for i in range(n):# create a loop 

        for i in range(4):  # Draw a square for each Fibonacci number
         t.forward(b * 10)  # Scale the Fibonacci number for visibility
         t.left(90)  # Turn right by 90 degrees
        t.circle(b * 10, 90)  # Draw a quarter circle with radius b * 10

        a, b = b, a + b  # Update Fibonacci numbers

def draw_modolor_figure(t, base=100):
    """Draws a simple human figure in the Modulor diagram."""
    phi = 1.618
    height = base  # Full height of the figure
    mid = height / phi  # Navel at golden ratio

    # Draw vertical line (spine)
    t.penup()
    t.goto(0, 0)
    t.setheading(90)
    t.pendown()
    t.forward(height)

    # Head
    t.penup()
    t.goto(0, height)
    t.pendown()
    t.circle(5)  # Simple circle for head

    # Arms
    t.penup()
    t.goto(0, mid)
    t.setheading(0)
    t.pendown()
    t.forward(20)
    t.backward(40)

    # Legs (open)
    t.penup()
    t.goto(0, 0)
    t.setheading(-60)
    t.pendown()
    t.forward(30)

    t.penup()
    t.goto(0, 0)
    t.setheading(-120)
    t.pendown()
    t.forward(30)


def draw_modolor_diagram(t, base=100):# function to draw modolor diagram with parameters t for turtle and base for the base length
    phi=1.618 #this is the golden ratio
    heights=[base, base/phi, base/phi**2, base/phi**3]  # Heights of the rectangles

    t.penup()  # Lift the pen to move without drawing
    t.goto(0,0)  # Center the diagram
    t.setheading(90)  # Set the initial heading 
    t.pendown()

    for h in heights:
        t.forward(h)
        t.write(f"{round(h,1)}",font=("Ariel",10,"normal"))
        t.backward(h)
        t.left(90)
        t.forward(20)
        t.right(90)
        
    draw_modolor_figure(t, base)


def main():
        screen=turtle.Screen()
        screen.title("Fibonacci Spiral and Modolor Diagram")
        screen.bgcolor("white")
        bob= turtle.Turtle() # create a turtle object named bob
        bob.speed(0)

        bob.penup()  # Lift the pen to move without drawing
        bob.goto(-200,-100)  # Center the diagram
        bob.setheading(0)  # Set the initial heading 
        bob.pendown()
        draw_fibonacci_spiral(bob,8)  # Draw the Fibonacci spiral with 8 segments

        bob.penup()  # Lift the pen to move without drawing
        bob.goto(200,-50)  # Center the diagram
        bob.setheading(90)  # Set the initial heading 
        bob.pendown()
        draw_modolor_diagram(bob, base=183) 

        turtle.done()  # Finish the drawing and keep the window open

main()  # Call the main function to run the program

        
        
