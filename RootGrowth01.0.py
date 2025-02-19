import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Declaring constants
deflectionAngleMin = 12
deflectionAngleMax = 13
turningSharpness = 0.5
timeBetweenDeflections = 100
rootSpeed = 1

step_counter = turtle.Turtle()
step_counter.speed(0)
step_counter.color("black")
step_counter.penup()
step_counter.hideturtle()
step_counter.goto(screen.window_width()//2 - 60, screen.window_height()//2 - 40)

# Create a turtle to draw the root
root = turtle.Turtle()
root.speed(0)
root.color("black")
root.penup()
root.goto(0, 200)
root.pendown()

root.hideturtle()



deflectionAngleRange = deflectionAngleMax - deflectionAngleMin # Calculate the range of available deflection angles

targetAngle = 270 + random.gauss(-deflectionAngleRange+deflectionAngleMin, deflectionAngleRange+deflectionAngleMin)
root.setheading(targetAngle)
def draw_root():
    for i in range(700): # Draw 300 steps
        
        if(i % timeBetweenDeflections == 0):
            angle = random.gauss(-deflectionAngleRange+deflectionAngleMin, deflectionAngleRange+deflectionAngleMin) # Randomly select an angle within the available range
           
        

            targetAngle = root.heading()+angle
            
        if(i % timeBetweenDeflections == timeBetweenDeflections/2):
            targetAngle = 270

            
        currentAngle = root.heading()
        if currentAngle < targetAngle:
            root.setheading(currentAngle + turningSharpness)
        elif currentAngle > targetAngle:
            root.setheading(currentAngle - turningSharpness)

        root.forward(rootSpeed)
       
# Draw the root
draw_root()

# Hide the turtle and display the result

screen.mainloop()