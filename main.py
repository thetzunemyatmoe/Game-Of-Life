import pygame
import time
import numpy as np


# Colors to use 
BACKGROUNG_COLOUR = (10,10,10)
GRID_COLUR = (20, 33, 61)
DIE_COLOUR = (156, 0, 0)
ALIVE_COLOUR = (252, 163, 17)

# Game of life
def gamefunction(window, cell, size, progress = False):
    update_cell = np.zeros((cell.shape[0], cell.shape[1]))
    
    for ROW, COL in np.ndindex(cell.shape):
        # Counting alive neighbours
        alive_neighbours = np.sum(cell[ROW-1: ROW+2, COL-1: COL+2]) - cell[ROW, COL]
        # Setting colour accordingly 
        cell_colour = BACKGROUNG_COLOUR if cell[ROW,COL] == 0 else ALIVE_COLOUR
        if cell[ROW, COL] != 0:
                # If a cell has no alive neighbours, one alive neighbours or more than 3 neighbours
                if (alive_neighbours < 2 or alive_neighbours > 3) and progress:
                        cell_colour = DIE_COLOUR
                        
                # If a cell has two or more and three or less neighbours
                elif alive_neighbours >= 2 and alive_neighbours <= 3 and progress: 
                    update_cell[ROW, COL] = 1 
                    cell_colour = ALIVE_COLOUR
        elif cell[ROW, COL] ==0:
            if(alive_neighbours ==3) and progress:
                update_cell[ROW, COL] = 1
                cell_colour = ALIVE_COLOUR
                
        pygame.draw.rect(window, cell_colour, (COL * size, ROW * size, size-1, size-1))
        
    return update_cell

    
 


def main():
    pygame.init()
    window = pygame.display.set_mode((800, 600))
    
    cells = np.zeros((60,80))
    window.fill(GRID_COLUR)
    gamefunction(window, cells, 10)
    
    pygame.display.flip()
    pygame.display.update()    
    
    isRunning = False
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                isRunning = not isRunning
                gamefunction(window, cells, 10)
                pygame.display.update()
            
            if pygame.mouse.get_pressed()[0]:
                position = pygame.mouse.get_pos()
                cells[position[1] // 10, position[0] // 10] = 1;
                gamefunction(window, cells, 10)
                pygame.display.update()
            
            
        
        window.fill(GRID_COLUR)
        
        if isRunning:
            cells = gamefunction(window, cells, 10, True)       
            pygame.display.update()

        time.sleep(0.01)
        
        
main()
       
            
                
                
                
                    
    
                           