from vpython import sphere, vector, rate
import math
import vpython as vp
import random

#TODO: Model root tip

GROWTH_SPEED = 0.1
TURNING_SPEED = 0.05
DOWNWARD_PREFERENCE = 0.01

tracer = vp.sphere(pos=vp.vector(0,0,0), radius=0.1, color=vp.color.white, make_trail=True, trail_radius=0.1)
tip = vp.cone(pos=vp.vector(0,0,0), axis=vp.vector(0, -0.8,0), radius=0.1, color=vp.color.orange)

heading = vp.vector(0, -1, 0)
targetVector = heading

points = []
def draw_root():
    global heading, targetVector
    targetVector = vp.vector(0, -1, 0)
    for i in range(300):
        vp.rate(100)

        if i % 100 == 0:
            targetVector = vp.vector(random.uniform(-1, 1), -1, random.uniform(-1, 1))

        heading = vp.vector(
            heading.x * (1 - TURNING_SPEED) + targetVector.x * TURNING_SPEED,
            heading.y * (1 - TURNING_SPEED) + targetVector.y * TURNING_SPEED,
            heading.z * (1 - TURNING_SPEED) + targetVector.z * TURNING_SPEED
        ).norm()
        
        # Slowly curve back downwards
        targetVector = vp.vector(
            targetVector.x * 0.99,
            targetVector.y * 0.99 - DOWNWARD_PREFERENCE,
            targetVector.z * 0.99
        ).norm()

        tip.axis = heading
        tip.pos += heading * GROWTH_SPEED

        tracer.pos = tip.pos
        tracer.axis = heading
        #vp.scene.camera.pos = tracer.pos + vp.vector(0, 0, 10)
        vp.scene.camera.near = 0.01  # Set the near clipping plane to a smaller value

        points.append((tip.pos.x, tip.pos.y, tip.pos.z, heading.x, heading.y, heading.z))
    # Hide the tip and tracer
    tip.visible = False
    tracer.visible = False
    tracer.clear_trail()
    print(points)

draw_root()

class RootTip:
    def __init__(self, pos, axis):
        self.cell = vp.ellipsoid(pos=pos, length=1.5, height=0.5, width=0.5, color=vp.vector(1, 0, 0))
        self.cell.axis = axis

root_cells = []

def create_root_cells():
    last_pos = None
    for point in points:
        current_pos = vp.vector(point[0], point[1], point[2])
        current_axis = vp.vector(point[3], point[4], point[5])
        if last_pos is None or vp.mag(current_pos - last_pos) >= 1:
            root_cells.append(RootTip(current_pos, current_axis))
            last_pos = current_pos
            vp.rate(10)  # Adjust the rate to control the speed of cell creation

create_root_cells()