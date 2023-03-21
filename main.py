import pygame
import pyautogui

       
pygame.init()


'''   Define colours   '''
white = (255,255,255)
black = (0,0,0)
myw, myh = pyautogui.size()
size = (screen_width,screen_height) = (myw/3,myh-200)
# myw=640.0    |    myh=880


'''   Creating a screen   '''
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


'''   Classes   '''
# class Player(pygame.sprite.Sprite):
#     def __init__(self, x, y):
#         super().__init__()
#         self.image = p
        


'''    Main loop    '''
gameStart = True
while gameStart == True:
        
    '''  Process events  '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # check if user want to close the window
            gameStart = False
            pygame.quit()
            quit()
 
    '''   Draw   '''
    screen.fill(white)
    pygame.draw.rect(screen, black, (100,100, 120, 80))
    
    pygame.display.flip()     
    clock.tick(100)
pygame.quit()