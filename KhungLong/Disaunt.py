import pygame
from pygame.constants import KEYDOWN
pygame.init  #KHoi tao game
screen = pygame.display.set_mode((600,300)) # thiet lap ma hinh 
pygame.display.set_caption("KHỦNG LONG OC CHOS") #ten game 
pygame.font.init()
pygame.mixer.init()
WHITE = (255,255,255) # rgb: to hop ba mua (đỏ, xanh lá ,màu xanh nước biển) 
RED = (255,0,0)
backGround_x = 0
backGround_y = 0
dinosaur_x = 150
dinosaur_y = 230
tree_x = 550
tree_y = 230
x_vector = 5
y_vecor = 7
souce = 0 
font = pygame.font.SysFont('san',35)
font1 = pygame.font.SysFont('san',35)
# thêm hình ảnh vào game mình đã cài đặt 
backGround = pygame.image.load('background.jpg')
dinosaur =  pygame.image.load('dinosaur.png') 
tree =  pygame.image.load('tree.png')
sound1 = pygame.mixer.Sound('tick.wav')
sound2 = pygame.mixer.Sound('te.wav')
clock = pygame.time.Clock() 
jump = False
pausing = False
running = True
while running:
    clock.tick(60)
    screen.fill(WHITE)
    backGround_1 = screen.blit(backGround,(backGround_x,backGround_y))
    backGround_2 = screen.blit(backGround,(backGround_x+600,backGround_y))
    souce_txt = font.render('Score:'+ str(souce),True,RED)
    #ghi len man hinh 
    screen.blit(souce_txt,(5,5))
    tree_ret = screen.blit(tree,(tree_x,tree_y))
    if backGround_x+600<=0:
        backGround_x = 0 
    tree_x-=x_vector
    if tree_x <= -20:
        tree_x = 550 
        souce +=1
    if 230 >=dinosaur_y>=80:
        if jump == True:
            dinosaur_y -= y_vecor
    else:
        jump = False 
    if dinosaur_y <230:
        if jump == False:
            dinosaur_y+= y_vecor    
    dinosaur_ret = screen.blit(dinosaur,(dinosaur_x,dinosaur_y))
    if dinosaur_ret.colliderect(tree_ret):
        pygame.mixer.Sound.play(sound2)
        pausing = True
        gameOver_txt = font.render('GAME OVER',True,RED)
        screen.blit(gameOver_txt,(250,150))
        x_vector = 0
        y_vecor = 0

    tree_ret = screen.blit(tree,(tree_x,tree_y))
 
    backGround_x -= x_vector
    for event  in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if dinosaur_y == 230:
                    pygame.mixer.Sound.play(sound1)
                    jump = True  
                if pausing :
                    backGround_x = 0
                    backGround_y = 0
                    dinosaur_x = 150
                    dinosaur_y = 230
                    tree_x = 550
                    tree_y = 230
                    x_vector = 5
                    y_vecor = 7
                    souce = 0 
                    font = pygame.font.SysFont('san',35)
                    font1 = pygame.font.SysFont('san',35)
                    pausing = False

    pygame.display.flip() #cap nhat mau 
pygame.quit()         

