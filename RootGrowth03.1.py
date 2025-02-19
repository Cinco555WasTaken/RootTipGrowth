import math
import vpython as vp

heading = vp.vector(0, -1, 0)

zero = vp.box(pos=vp.vector(0,0,0), size=vp.vector(10,0.1,10), color=vp.vector(1,1,1))

class Cell:
    all_cells = []  # Class variable to keep track of all cells
    totalCells = 0

    def __init__(self):
        self.cell = vp.ellipsoid(pos=vp.vector(0,0,0), length = 1, height = 1, width = 1, color=vp.vector(1,0,0))
        self.cell_heading = vp.vector(0, -1, 0)
        self.target_vector = self.cell_heading
        Cell.all_cells.append(self)  # Add the new cell to the array
        Cell.totalCells += 1

    def createCell(self, place):
        new_cell = Cell()
        new_cell.cell.height = 2
        new_cell.cell.pos = place
        Cell.totalCells += 1
        if(Cell.totalCells % 2 == 0):
            for i in range(10):
                self.cell.height -= 0.1
                self.cell.pos += self.cell_heading * 0.05
                vp.rate(40)
        if(Cell.totalCells % 2 == 1):
            for i in range(10):
                self.cell.height -= 0.1
                self.cell.pos -= self.cell_heading * 0.05
                vp.rate(40)
                
            
        return new_cell
    
    def split(self):
        activeCell = self.cell
        activeCellId = Cell.all_cells.index(self)
        activeCell.color = vp.vector(0,1,0)
        for i in range(10):
            activeCell.height += 0.1
            vp.rate(7)
            activeCell.pos += self.cell_heading * 0.05
        activeCell.visible = False
        Cell.totalCells -= 1
        newCell1 = self.all_cells[activeCellId].createCell(activeCell.pos)
        newCell2 = self.all_cells[activeCellId].createCell(activeCell.pos)
        

# Create the initial cell and split it
cell1 = Cell()
cell1.split()

for i in range(10):
    cell = Cell.all_cells[-1]
    cell.split()

# Print the number of cells
print(f"Number of cells: {len(Cell.all_cells)}")
print(Cell.totalCells)