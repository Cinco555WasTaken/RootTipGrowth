import vpython as vp
import random

tip = vp.sphere(pos=vp.vector(0,0,0), radius=0.1, color=vp.color.white, make_trail=True)
vp.rate(30)



def draw_root():
    for i in range(300):
       tip.pos += vp.vector(0, -0.1, 0)
        
draw_root()