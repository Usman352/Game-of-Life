from cell import Cell

class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.cells = [[Cell(False) for x in range(cols)]
                      for y in range(rows)]
    def get_neighbors(self, r, c):
        neighbors = []
        neighbor_indices = [(c-1, r-1),
                            (c-1, r),
                            (c-1, r+1),
                            (c, r-1),
                            (c, r+1),
                            (c+1, r-1),
                            (c+1, r),
                            (c+1, r+1)]
        for x in range(self.rows):
            for y in range(self.cols):
                if (x, y) == (r, c):
                    continue
                if (x, y) in neighbor_indices and self.cells[x][y].alive:
                    neighbors.append(self.cells[x][y])
        return neighbors

    def next_generation(self):
        for x in range(self.rows):
            for y in range(self.cols):
                currCell = self.cells[x][y]
                neighbors = self.get_neighbors(x, y)
                if currCell.alive:
                    if len(neighbors) < 2 or len(neighbors) > 3:
                        currCell.toggle()
                else:
                    if len(neighbors) == 3:
                        currCell.set_alive()

