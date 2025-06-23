class Cell:
    def __init__(self, alive):
        self.alive = alive
    def set_alive(self):
        self.alive = True
    def toggle(self):
        self.alive = not self.alive