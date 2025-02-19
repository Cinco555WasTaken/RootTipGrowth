import math
import vpython as vp
import random

#TODO: Fix the issue with the mouse click function
#TODO: Make cells keep heading
#TODO: Make cells split based on heading realistically
#TODO: Add more view windows (3)
#TODO: Print Table locations
#TODO: Clean up table before exporting
#TODO: Multiple different root growths at once

# Main scene
scene1 = vp.canvas(title='Main View', width=600, height=400, center=vp.vector(0, 0, 0), align='left')

# Second scene for tracking the root tip
scene2 = vp.canvas(title='Root Tip View', width=600, height=400, center=vp.vector(0, 0, 0), align='right')

zero = vp.box(canvas=scene1, pos=vp.vector(0,0.5,0), size=vp.vector(10,0.1,10), color=vp.vector(1,1,1))

class Cell:
    all_cells = []  # Class variable to keep track of all cells
    totalCells = 0
    cell_heading = vp.vector(0, -1, 0)  # Class variable to keep track of the heading of the cell
    def __init__(self):
        self.cell = vp.ellipsoid(canvas=scene1, pos=vp.vector(random.uniform(-3,3),0,random.uniform(-3,3)), length = 1, height = 1, width = 1, color=vp.vector(1,0,0))
        Cell.all_cells.append(self)  # Add the new cell to the array
        Cell.totalCells += 1

    def createCell(self, place):
        new_cell = Cell()
        new_cell.cell.pos = place
        Cell.totalCells += 1
        return new_cell

    def set_heading(self, new_heading):
        self.cell_heading = new_heading

    def split(self):
        activeCell = self.cell
        activeCellId = Cell.all_cells.index(self)
        activeCell.color = vp.vector(0,1,0)
        for i in range(10):
            activeCell.length += abs(self.cell_heading.x) * 0.1
            activeCell.height += abs(self.cell_heading.y) * 0.1
            activeCell.width += abs(self.cell_heading.z) * 0.1
            vp.rate(20)
            activeCell.pos += self.cell_heading * 0.05
        activeCell.visible = False
        Cell.totalCells -= 1
        newCell1 = self.all_cells[activeCellId].createCell(activeCell.pos - self.cell_heading / 2)
        newCell2 = self.all_cells[activeCellId].createCell(activeCell.pos + self.cell_heading / 2)

# --- Ignore This, currently does not work ---

# Function to handle mouse hover
def on_mouse_click(evt):
    # Check if the picked object is a cell
    if evt.pick is not None and hasattr(evt.pick, 'color'):
        for cell in Cell.all_cells:
            if evt.pick == cell.cell:
                cell.cell.color = vp.vector(0, 0, 1)  # Change color to blue
                break  # Exit the loop once the correct cell is found

# Bind the mouse click function
scene1.bind('click', on_mouse_click)

# --- Everything below this works again ---



def newHeading(new_heading):
    Cell.all_cells[-1].set_heading(vp.vector(new_heading.x, new_heading.y, new_heading.z))

    # Ensure the heading vector's length does not exceed 1
    heading_length = Cell.all_cells[-1].cell_heading.mag
    if heading_length > 1:
        Cell.all_cells[-1].cell_heading = Cell.all_cells[-1].cell_heading.norm()
        print(Cell.all_cells[-1].cell_heading)  

# Create the initial cell and split it
cell1 = Cell()
cell1.split()
cell2 = Cell()
cell2.split()
Cell.cell_heading = vp.vector(0, -1, 0)
# Change the heading of the last cell and split it

Cell.all_cells[-1].split()

for i in range(5):
    Cell.all_cells[-1].split()

newHeading(vp.vector(random.uniform(-1, 1), -1, random.uniform(-1, 1)))

for i in range(5):
    Cell.all_cells[-1].split()

# Print the number of cells
print(f"Number of cells: {len(Cell.all_cells)}")
print(Cell.totalCells)

# Update the second scene to follow the root tip
def update_root_tip_view():
    while True:
        vp.rate(20)
        if Cell.all_cells:
            root_tip = Cell.all_cells[-1].cell
            scene2.center = root_tip.pos
            scene2.camera.pos = root_tip.pos + vp.vector(0, 5, 10)
            scene2.camera.axis = root_tip.pos - scene2.camera.pos

# Start updating the root tip view
update_root_tip_view()
