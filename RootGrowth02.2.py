from vpython import sphere, vector, cone, label, rate, color
import random

# Constants
DEFLECTION_ANGLE = 0.1  # radians
TURNING_SHARPNESS = 0.05  # radians per step
TIME_BETWEEN_DEFLECTIONS = 10  # steps
ROOT_SPEED = 0.1  # units per step

# Root tip representation
root_tip = sphere(pos=vector(0, 0, 0), radius=0.1, color=color.green)
root_direction = vector(0, -1, 0)
target_direction = root_direction

# Cone for root tip's direction
root_cone = cone(pos=root_tip.pos, axis=root_direction, radius=0.05, color=color.green)

# Step counter label
step_counter = label(pos=vector(0, 0, 0), text='Step: 0', height=10, box=False)

def draw_root():
    global root_tip, root_direction, target_direction
    step = 0

    while True:
        rate(30)  # Control the speed of the simulation

        # Randomly change the target direction at intervals
        if step % TIME_BETWEEN_DEFLECTIONS == 0:
            deflection = vector(random.uniform(-DEFLECTION_ANGLE, DEFLECTION_ANGLE),
                                random.uniform(-DEFLECTION_ANGLE, DEFLECTION_ANGLE),
                                random.uniform(-DEFLECTION_ANGLE, DEFLECTION_ANGLE))
            target_direction = root_direction + deflection

        # Gradually adjust the root's direction towards the target direction
        root_direction = root_direction + TURNING_SHARPNESS * (target_direction - root_direction)
        root_direction = root_direction.norm()

        # Update the root's position
        root_tip.pos += ROOT_SPEED * root_direction

        # Update the cone's position and direction
        root_cone.pos = root_tip.pos
        root_cone.axis = root_direction

        # Update the step counter
        step_counter.pos = root_tip.pos + vector(0, 0.5, 0)
        step_counter.text = f'Step: {step}'

        step += 1

# Run the simulation
draw_root()