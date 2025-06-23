from cell import Cell
from grid import Grid
import time

def main():
    newGrid = Grid(10,10)
    newGrid.cells[0][1].set_alive()
    newGrid.cells[1][2].set_alive()
    newGrid.cells[2][0].set_alive()
    newGrid.cells[2][1].set_alive()
    newGrid.cells[2][2].set_alive()
    newGrid.display_grid()
    # input("Press Enter to display next 10 generations...")
    for i in range(1,31):
        newGrid.next_generation()
        print("GENERATION #", i)
        newGrid.display_grid()
        time.sleep(0.1)

if __name__ == "__main__":
    main()