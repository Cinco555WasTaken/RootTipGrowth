import vpython as vp
import random

# Main scene
scene1 = vp.canvas(title='Main View', width=600, height=400, center=vp.vector(0, 0, 0), align='left')

# Second scene for tracking the root tip
scene2 = vp.canvas(title='Root Tip View', width=600, height=400, center=vp.vector(0, 0, 0), align='right')

zero = vp.box(canvas=scene1, pos=vp.vector(0,0.5,0), size=vp.vector(10,0.1,10), color=vp.vector(1,1,1))

class Cell:
    all_cells = []  # Class variable to keep track of all cells
    totalCells = 0
    def __init__(self, pos, heading=vp.vector(0, -1, 0)):
        self.cell = vp.ellipsoid(canvas=scene1, pos=pos, length=1, height=1, width=1, color=vp.vector(1,0,0))
        self.heading = heading
        Cell.all_cells.append(self)
        Cell.totalCells += 1

    def split(self):
        activeCell = self.cell
        activeCell.color = vp.vector(0,1,0)
        for _ in range(10):
            activeCell.height += abs(self.heading.y) * 0.1
            activeCell.width += abs(self.heading.z) * 0.1
            vp.rate(20)
            activeCell.pos += self.heading * 0.05
        activeCell.visible = False
        Cell.totalCells -= 1
        newCell1 = Cell(activeCell.pos - self.heading / 2, self.heading)
        Cell(activeCell.pos - self.heading / 2, self.heading)
        Cell(activeCell.pos + self.heading * 1.5, self.heading)
# Function to handle mouse click
def on_mouse_click(evt):
    if evt.pick is not None and hasattr(evt.pick, 'color'):
        for cell in Cell.all_cells:
            if evt.pick == cell.cell:
                cell.cell.color = vp.vector(0, 0, 1)
                break

# Bind the mouse click function
scene1.bind('click', on_mouse_click)

# Create the initial cells and split them
initial_pos1 = vp.vector(random.uniform(-3, 3), 0, random.uniform(-3, 3))
cell1 = Cell(initial_pos1)
initial_pos2 = vp.vector(random.uniform(-3, 3), 0, random.uniform(-3, 3))
cell2 = Cell(initial_pos2)

# Function to grow cells
def grow_cells():
    for i in range(5):

        cell2.split()
# Start growing cells
grow_cells()

# Print the number of cells
print(f"Number of cells: {len(Cell.all_cells)}")
print(Cell.totalCells)

# Update the second scene to follow both root tips
def update_root_tip_view():
    while True:
        vp.rate(20)
        if len(Cell.all_cells) >= 2:
            root_tip1 = Cell.all_cells[-2].cell
            root_tip2 = Cell.all_cells[-1].cell
            scene2.center = (root_tip1.pos + root_tip2.pos) / 2
            scene2.camera.pos = scene2.center + vp.vector(0, 5, 10)
            scene2.camera.axis = scene2.center - scene2.camera.pos

# Start updating the root tip view
update_root_tip_view()
