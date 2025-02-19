import vpython as vp
import random

GROWTH_SPEED = 0.1
TURNING_SPEED = 0.05

FullView = vp.canvas(title='Main View', width=600, height=400, center=vp.vector(0, 0, 0), align='left')
Slider = vp.slider(canvas=FullView, bind=vp.rate, min=1, max=100, value=10, length=200, left=10, right=10, top=10, step=1)

num_cells = 6  # Number of surrounding cells
radius = 1  # Radius of the circle

class RootTip:
    all_cells = []  # Class variable to keep track of all cells
    active_cells = []  # Class variable to keep track of all active cells
    def __init__(self):
        self.cell = vp.ellipsoid(canvas=FullView, pos=vp.vector(0,0,0), length = 1, height = 1, width = 1, color=vp.vector(1,0,0))
        self.heading = vp.vector(0, -1, 0)
        RootTip.all_cells.append(self.cell)
        
        for i in range(num_cells):
            angle = (2 * vp.pi / num_cells) * i
            x = radius * vp.cos(angle)
            z = radius * vp.sin(angle)
            new_cell = vp.ellipsoid(canvas=FullView, pos=vp.vector(x, 0, z), length=1, height=1, width=1, color=vp.vector(1, 0, 0))
            RootTip.all_cells.append(new_cell)
        RootTip.active_cells = RootTip.all_cells

new_root = RootTip()

tracer = vp.sphere(canvas=FullView, pos=vp.vector(0,0,0), radius=1.5, color=vp.color.white, make_trail=True, trail_radius=1.5, trail_opacity=100, opacity=100)
tip = vp.cone(canvas=FullView, pos=vp.vector(0,0,0), axis=vp.vector(0, -0.8,0), radius=0.1, color=vp.color.orange)

heading = vp.vector(0, -1, 0)
targetVector = heading

def draw_root():
    global heading, targetVector
    targetVector = vp.vector(0, -1, 0)
    for i in range(300):
        vp.rate(Slider.value)

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