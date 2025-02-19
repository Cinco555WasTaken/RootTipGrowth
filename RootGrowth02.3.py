import vpython as vp
import random

GROWTH_SPEED = 0.1
TURNING_SPEED = 0.05

tracer = vp.sphere(pos=vp.vector(0,0,0), radius=0.1, color=vp.color.white, make_trail=True, trail_radius=0.1)
tip = vp.cone(pos=vp.vector(0,0,0), axis=vp.vector(0, -0.8,0), radius=0.1, color=vp.color.orange)

heading = vp.vector(0, -1, 0)
targetVector = heading

def draw_root():
    global heading, targetVector
    targetVector = vp.vector(0, -1, 0)
    for i in range(300):
        vp.rate(30)

        if i % 100 == 0:
            targetVector = vp.vector(random.uniform(-1, 1), -1, random.uniform(-1, 1))

        heading = vp.vector(
            heading.x * (1 - TURNING_SPEED) + targetVector.x * TURNING_SPEED,
            heading.y * (1 - TURNING_SPEED) + targetVector.y * TURNING_SPEED,
            heading.z * (1 - TURNING_SPEED) + targetVector.z * TURNING_SPEED
        ).norm()
        tip.axis = heading
        tip.pos += heading * GROWTH_SPEED

        tracer.pos = tip.pos
        tracer.axis = heading
        vp.scene.camera.pos = tracer.pos + vp.vector(0, 0, 10)

draw_root()
