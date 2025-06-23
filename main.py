import pygame
from pygame.locals import *
from grid import Grid
import sys

def main():
    pygame.init()

    # Window

    WIDTH, HEIGHT = 800, 600
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Game of Life")
    icon_surface = pygame.image.load('icon.png')
    pygame.display.set_icon(icon_surface)

    # Colours

    B = pygame.Color(0, 0, 0)
    W = pygame.Color(255, 255, 255)

    # timing

    FPS = pygame.time.Clock()
    FPS.tick(60)

    # Grid

    CELL_SIZE = 4
    ROWS = HEIGHT // CELL_SIZE
    COLS = WIDTH // CELL_SIZE
    GRID = Grid(ROWS, COLS, CELL_SIZE)
    paused = True
    running = True

    button_w, button_h = 80, 40
    button_y = HEIGHT - 50
    gap = 20

    total_w = 3 * button_w + 2 * gap

    start_x = (WIDTH - total_w) // 2

    buttons = {
        "play": pygame.Rect(start_x, button_y, button_w, button_h),
        "pause": pygame.Rect(start_x + button_w + gap, button_y, button_w, button_h),
        "exit": pygame.Rect(start_x + 2 * (button_w + gap), button_y, button_w, button_h),
    }


    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == MOUSEBUTTONDOWN:
                mx, my = event.pos
                if buttons["play"].collidepoint(mx, my):
                    paused = False
                elif buttons["pause"].collidepoint(mx, my):
                    paused = True
                elif buttons["exit"].collidepoint(mx, my):
                    running = False
                elif my < HEIGHT - 60:
                    r = my // CELL_SIZE
                    c = mx // CELL_SIZE
                    if 0 <= r < ROWS and 0 <= c < COLS:
                        GRID.cells[r][c].toggle()

        if not paused:
            GRID.next_generation()

        SCREEN.fill(B)

        for row in range(ROWS):
            for col in range(COLS):
                if GRID.cells[row][col].alive:
                    rect = pygame.Rect(
                        col * CELL_SIZE,
                        row * CELL_SIZE,
                        CELL_SIZE,
                        CELL_SIZE
                    )
                    pygame.draw.rect(SCREEN, W, rect)


        font = pygame.font.SysFont(None, 20)
        for name, rect in buttons.items():
            pygame.draw.rect(SCREEN, W, rect, 2)
            text = font.render(name.capitalize(), True, W)
            tx = rect.x + (rect.width - text.get_width()) // 2
            ty = rect.y + (rect.height - text.get_height()) // 2
            SCREEN.blit(text, (tx, ty))

        FPS.tick(60)
        pygame.display.update()



    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()