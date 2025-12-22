import pygame

pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('射擊遊戲(取自YouTube Coding With Russ)')


class Soldier(pygame.sprite.Sprite): #explain-124
    def __init__(self, x, y, scale):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('img/player/Idle/0.png') #玩家小綠人
        self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale) )) # 圖片尺寸調整 explain-78
        self.rect = self.image.get_rect()
        self.rect.center = (x, y) # 確保物體在正中間
    
    def draw(self): # 自己可以重複使用 像是player.draw()
        screen.blit(self.image, self.rect) #explain-65



player =Soldier(200, 200, 3)
player2 =Soldier(400, 200, 3)

run = True # explain-1
while run:



    
    player.draw()
    player2.draw()

    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            run = False


    pygame.display.update() # explain-54



# pygame.quit()
