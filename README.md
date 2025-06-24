# Conway’s Game of Life

A Python implementation of Conway’s Game of Life using an object-oriented design and a Pygame-based GUI.

## Features

* **Object-Oriented Core**: Clean separation of `Cell` and `Grid` classes handling state and rules.
* **Interactive GUI**: Pygame window with a black background and white cells.
* **Play/Pause/Exit Controls**: Clickable buttons to start, pause, or exit the simulation.
* **Cell Toggling**: Click on individual grid cells to set them alive or dead before running.
* **Adjustable Grid Size**: Grid dimensions and cell pixel size are automatically calculated from window size.

## File Structure

```
Game-of-Life/
├── cell.py         # Cell class definition
├── grid.py         # Grid class with neighbor logic and generation updates
├── main.py         # Pygame application entry point
├── icon.png        # Window icon image (32×32 PNG)
└── README.md       # Project overview and instructions
```

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Usman352/Game-of-Life.git
   cd Game-of-Life
   ```

2. **Create a venv** (optional but recommended)

   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\\Scripts\\activate    # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install pygame
   ```

## Usage

Run the main application:

```bash
python main.py
```

* **Click** on cells to toggle them alive/dead.
* **Play** button: start automatic generation updates.
* **Pause** button: stop the simulation on the current generation.
* **Exit** button: close the window.

## Customization

* **Window size**: Modify `WIDTH` and `HEIGHT` in `main.py`.
* **Cell size**: Change `CELL_SIZE` in `main.py` (default is 4 pixels).
* **Frame rate**: Adjust the tick rate in the game loop (`FPS.tick(60)`).

## Algorithm Details

1. **Neighbor Counting**: For each cell, the eight adjacent cells are checked.
2. **Game Rules**:

   * A live cell with fewer than 2 or more than 3 live neighbors dies.
   * A live cell with 2 or 3 neighbors survives.
   * A dead cell with exactly 3 neighbors becomes alive.

## License

This project is open source and available under the MIT License.
