import vpython as vp
import random

GROWTH_SPEED = 0.1

class Cell:
    def __init__(self):
        self.cell = vp.sphere(pos=vp.vector(random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1)), radius=0.1, color=vp.color.white, make_trail=True, trail_radius=0.1)
        self.cell_heading = vp.vector(0, -1, 0)
        self.target_vector = self.cell_heading

    def grow(self):
        self.cell.pos += self.cell_heading * GROWTH_SPEED

    def rotate(self, axis):
        self.cell_heading = axis

class RootTip:
    def __init__(self):
        self.cells = [Cell() for _ in range(20)]

    def grow(self, heading):
        for cell in self.cells:
            cell.grow()

    def rotate(self, axis):
        for cell in self.cells:
            cell.rotate(axis)

root_tip = RootTip()
heading = vp.vector(0, -1, 0)

for i in range(100):
    vp.rate(30)
    root_tip.grow(heading)

    if i % 30 == 0:
        root_tip.rotate(axis=vp.vector(random.uniform(-1, 1), -1, random.uniform(-1, 1)))


