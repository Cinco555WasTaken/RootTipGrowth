import vpython as vp
import random

GROWTH_SPEED = 0.1
TURNING_SPEED = 0.05
NUM_ROOTS = 5



class RootTip:
    def __init__(self, start_pos):
        self.tracer = vp.sphere(pos=start_pos, radius=0.1, color=vp.color.white, make_trail=True, trail_radius=0.1)
        self.tip = vp.cone(pos=start_pos, axis=vp.vector(0, -0.8, 0), radius=0.1, color=vp.color.orange)
        self.heading = vp.vector(0, -1, 0)
        self.targetVector = self.heading

    def grow(self):
        if random.randint(0, 99) == 0:
            self.targetVector = vp.vector(random.uniform(-1, 1), -1, random.uniform(-1, 1))

        self.heading = vp.vector(
            self.heading.x * (1 - TURNING_SPEED) + self.targetVector.x * TURNING_SPEED,
            self.heading.y * (1 - TURNING_SPEED) + self.targetVector.y * TURNING_SPEED,
            self.heading.z * (1 - TURNING_SPEED) + self.targetVector.z * TURNING_SPEED
        ).norm()
        self.tip.axis = self.heading
        self.tip.pos += self.heading * GROWTH_SPEED

        self.tracer.pos = self.tip.pos
        self.tracer.axis = self.heading

roots = [RootTip(vp.vector(random.uniform(-5, 5), 0, random.uniform(-5, 5))) for _ in range(NUM_ROOTS)]

def add_root():
    new_root = RootTip(vp.vector(random.uniform(-5, 5), 0, random.uniform(-5, 5)))
    roots.append(new_root)

button = vp.button(text="Add Root", pos=vp.scene.title_anchor, bind=lambda: add_root())



def draw_roots():
    for _ in range(1000):
        vp.rate(30)
        for root in roots:
            root.grow()

draw_roots()
