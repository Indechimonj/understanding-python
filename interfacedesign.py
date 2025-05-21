import turtle# import the turtle module
import math# import the math module

#Code to understand the turtle module 
#Question 1:The process of encapsulation.
#Write a function called square that takes a parameter named t, which is a turtle.
#It should use the turtle to draw a square.
#Write a function call that passes bob as an argument to square, and then run the program again.
def square(t):
    for i in range(4):# loop to print vertical lines
        t.forward(100)# method to move the turtle forward
        t.right(90)# turn the turtle right
bob=turtle.Turtle()# create a turtle object

square(bob)# call the square function

#Question 2:The process of generalization.
#Add another parameter, named length, to square. 
#Modify the body so length of the sides is length, and then modify the function call to provide a second argument.
#Run the program again. Test your program with a range of values for length.
def square(t, length):
    for i in range(4):# loop to print vertical lines
        t.forward(length)# method to move the turtle forward.We can change the length of the square by changing the value of length
        t.right(90)# method turn the turtle right
square(bob, 200)# call the square function with length 200


#Question 3:The process of generalization.Instead of drawing squares,polgon functions are used to draw regular polygons with any number of sides.
#Make a copy of square and change the name to polygon. 
#Add another parameter named n and modify the body so it draws an n-sided regular polygon.
#Hint:The exterior angles of an n-sided regular polygon are 360/n degrees
def polygon(t, length, n):
    for i in range(n):# loop to print vertical lines
        t.forward(length)# method to move the turtle forward
        t.right(360/n)# method turn the turtle right
polygon(bob, 100, 5)# call the polygon function with length 100 and n=5

#Question 4: The process of clean interface design
#Write a function called circle that takes a turtle, t, and radius, r, as parameters.
#The function draws an approximate circle by calling polygon with an appropriate length and number of sides. 
#Test your function with a range of values of r.
#Hint: figure out the circumference of the circle and make sure that length * n =circumference.
def circle(t, r):
    circumfrence=2*math.pi*r# calculate the circumference of the circle.
    n=int(circumfrence/3)+1# this method is used to calculate the number of sides
    length=circumfrence/n# this method is used to calculate the length of each side
    polygon(t, length, n)# call the polygon function with length and n
circle(bob, 100)# call the circle function with radius 100
polygon(bob, 50, 5)# call the polygon function with length 50 and n=5

#Question 5: The process of refactoring
#Make a more general version of circle called arc that takes an additional parameter angle, which determines what fraction of a circle to draw. 
# angle is in units of degrees, so when angle=360, arc should draw a complete circle.
def polyline(t,n,length, angle):
    for i in range(n):# loop to print vertical lines
        t.forward(length)# method to move the turtle forward
        t.right(angle)# method turn the turtle right
def polygon(t, length, n):
    angle=360/n# this method is used to calculate the angle
    polyline(t, n, length, angle)# call the polyline function with length and n
def arc(t, r, angle):
    arc_length=2*math.pi*r*angle/360# calculate the arc length
    n=int(arc_length/3)+1# this method is used to calculate the number of sides
    step_length=arc_length/n# this method is used to calculate the length of each side
    step_angle=angle/n# this method is used to calculate the angle
    polyline(t, n, step_length, step_angle)# call the polyline function with length and n
arc(bob, 200, 90)# call the arc function with radius 100 and angle 90



turtle.mainloop()# keep the window open
