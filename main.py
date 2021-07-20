import pygame,sys

from pygame.constants import MOUSEBUTTONDOWN
pygame.init()

window_x = 1920
window_y = 1009

menutype = "start"

screen = pygame.display.set_mode((window_x,window_y))

pygame.display.set_caption("乱斗三国")

background = pygame.image.load("bg.jpg")
te_logo = pygame.image.load("logo_w.png")
te_menu = pygame.image.load("menu.png")

bu_game = pygame.image.load("button_game.png")
bu_chose = pygame.image.load("button_chose.png")
while True:
    mouse_x,mouse_y = pygame.mouse.get_pos()
    mouse_down = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            mouse_down = True
    screen.fill((255,255,255))
    if menutype == "menu":
        screen.blit(background,(0,0))
        screen.blit(te_menu,(0,0))
    
    if menutype == "start":
        screen.blit(background,(0,0))
        screen.blit(te_logo,(window_x-20-124,20))
        screen.blit(bu_game,(window_x-20-124,20+40+10))
        if window_x-20-124 <= mouse_x <=window_x-20  and  70 <= mouse_y <=103:
            screen.blit(bu_chose,(window_x-20-124,20+40+10))
            if mouse_down == True:
                menutype = "menu"
    pygame.display.update()