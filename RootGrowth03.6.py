from vpython import sphere, vector, rate
import math
import vpython as vp
import random

#TODO: Model root tip
#TODO: Bottom Most cells produce trail
#TODO: use trail feature, use increments instead of continuous


GROWTH_SPEED = 0.1
TURNING_SPEED = 0.05

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
            targetVector.y * 0.99 - 0.01,
            targetVector.z * 0.99
        ).norm()

        tip.axis = heading
        tip.pos += heading * GROWTH_SPEED

        tracer.pos = tip.pos
        tracer.axis = heading
        vp.scene.camera.pos = tracer.pos + vp.vector(0, 0, 10)

        points.append((tip.pos.x, tip.pos.y, tip.pos.z))

    print(points)

draw_root()

class RootTip:
    def __init__(self, pos):
        self.cell = vp.ellipsoid(pos=pos, length=1, height=1, width=1, color=vp.vector(1, 0, 0))

root_cells = []

def create_root_cells():
    last_pos = None
    for point in points:
        current_pos = vp.vector(point[0], point[1], point[2])
        if last_pos is None or vp.mag(current_pos - last_pos) >= 1:
            root_cells.append(RootTip(current_pos))
            last_pos = current_pos
            vp.rate(10)  # Adjust the rate to control the speed of cell creation

create_root_cells()