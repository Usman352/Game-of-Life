from cell import Cell

class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.cells = [[Cell(False) for x in range(cols)]
                      for y in range(rows)]
    def get_neighbors(self, r, c):
        neighbors = []
        diff = [(-1, -1), (0, -1), (1, -1),
                (-1, 0),           (1, 0),
                (-1, 1),  (0, 1),  (1, 1)]
        for dx, dy in diff:
            #check if on board
            #check if alive
            #add to neighbours list
            nr = r + dx
            nc = c + dy
            if 0 <= nr < self.rows and 0 <= nc < self.cols:
                if self.cells[nr][nc].alive:
                    neighbors.append(self.cells[nr][nc])
        return neighbors


    def next_generation(self):
        next_states = [[False for x in range(self.cols)]
                      for y in range(self.rows)]
        for x in range(self.rows):
            for y in range(self.cols):
                curr_cell = self.cells[x][y]
                next_states[x][y] = curr_cell.alive
                neighbors = self.get_neighbors(x, y)
                if curr_cell.alive:
                    if len(neighbors) < 2 or len(neighbors) > 3:
                        next_states[x][y] = False
                else:
                    if len(neighbors) == 3:
                        next_states[x][y] = True

        for x in range(self.rows):
            for y in range(self.cols):
                self.cells[x][y].alive = next_states[x][y]


