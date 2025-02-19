from vpython import sphere, vector, rate, color, cone
from vpython import label, button, scene
import random


# Declaring constants
deflectionAngleMin = 2
deflectionAngleMax = 5
turningSharpness = 0.02
timeBetweenDeflections = 100
rootSpeed = 0.1
maxGrowLength = 400

# Create a sphere to represent the root tip
root = sphere(pos=vector(0, 0, 0), radius=0.1, color=color.blue, make_trail=True)
root.trail_radius = 0.1
rootTip = cone(pos=vector(0, 0, 0), radius=0.1, color=color.orange, axis=vector(0, 0, 0))

deflectionAngleRange = deflectionAngleMax - deflectionAngleMin  # Calculate the range of available deflection angles

targetVector = vector(0, -1, 0)  # Initial direction pointing downwards
currentAngle = targetVector

def draw_root():
    step_counter = label(pos=vector(0, 1, 0), text='Steps: 0', height=20, box=False)
    global currentAngle, targetVector
    for i in range(maxGrowLength):
        rate(30)  # Control the speed of the animation
        step_counter.text = 'Steps: ' + str(i)  # Update the step counter label
        step_counter.pos = root.pos + vector(3, 0.5, 3)  # Update the step counter position
        if i % timeBetweenDeflections == 0:
            angle = random.gauss(-deflectionAngleRange + deflectionAngleMin, deflectionAngleRange + deflectionAngleMin)
            axis = vector(random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1)) 
            targetVector = currentAngle.rotate(angle=angle, axis=axis) 

        if i % timeBetweenDeflections == timeBetweenDeflections / 2:
            targetVector = vector(0, -1, 0)

        if currentAngle.diff_angle(targetVector) > turningSharpness:
            currentAngle = currentAngle.rotate(angle=turningSharpness, axis=currentAngle.cross(targetVector))

        root.pos += currentAngle * rootSpeed

        rootTip.pos = root.pos
        rootTip.axis = currentAngle

        scene.camera.pos = root.pos + vector(0, 0, 10) # Attempting to move the camera with the root

# Draw the root
draw_root()