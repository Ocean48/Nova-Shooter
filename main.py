import pygame
import pyautogui

       
pygame.init()


'''   Define colours   '''
white = (255,255,255)
black = (0,0,0)
myw, myh = pyautogui.size()
size = (screen_width,screen_height) = (myw/3,myh-200)
# myw=640.0    |    myh=880

ship_x = 0
fire = False


'''   Creating a screen   '''
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


'''   Classes   '''
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("images/ship.png")  # image size 120 x 80
        self.rect = self.image.get_rect(center=(x,y))
        
    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= 3
        if keys[pygame.K_RIGHT]:
            self.rect.x += 3
        
        if (self.rect.x <= -60):
            self.rect.x = screen_width-61   
        if (self.rect.x >= screen_width-60):
            self.rect.x = -60   
        
        global ship_x
        ship_x = self.rect.x
        
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("images/bullet.png")  # image size 5 x 15
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def update(self, keys):
        global fire
        global ship_x
        
        if (keys[pygame.K_LEFT] and fire == False):
            self.rect.x -= 3
        if (keys[pygame.K_RIGHT] and fire == False):
            self.rect.x += 3
        
        
        if (self.rect.x <= -2):
            self.rect.x = ship_x+61
        if (self.rect.x >= screen_width-2):
            self.rect.x = -2 
        if (self.rect.y <= -5):
            self.rect.x = ship_x+58
            self.rect.y = screen_height-95
            fire = False
        if (fire):
            self.rect.y -= 3
        

ship = Player(0+60,screen_height-40)
player_group = pygame.sprite.Group()
player_group.add(ship)

bullet = Bullet(ship_x+58,screen_height-95)
bullet_group = pygame.sprite.Group()
bullet_group.add(bullet)

'''    Main loop    '''
gameStart = True
while gameStart == True:
        
    '''  Process event  '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # check if user want to close the window
            gameStart = False
            pygame.quit()
            quit()   
        if event.type == pygame.KEYDOWN: #if the user pressed a key down
            if event.key == pygame.K_SPACE:
                pass
        if event.type == pygame.KEYUP: #if the user pressed a key released
            if event.key == pygame.K_d:
                pass
            
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_SPACE]):
        fire = True
 
    '''   Draw   '''
    screen.fill(white)
    player_group.draw(screen)
    player_group.update(keys)
    if (fire == True):
        bullet_group.draw(screen)
    bullet_group.update(keys)
    
    pygame.display.flip()     
    clock.tick(250)
pygame.quit()