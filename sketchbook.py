import sys
import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Sketchbook")
white = (255,255,255)
black = (0, 0, 0)
yellow = (255, 255, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

def main():
    mousepos = []
    mousedown = False
    draw_color = black
    
    font_ = pygame.font.SysFont(None, 50)
    save = font_.render("Save", True, (0, 128, 128))
    save_rect = save.get_rect()
    save_rect.center = (925, 520)
    fn = 0
    
    while True:
        
        screen.fill(white)
        pygame.draw.rect(screen, black, (900, 20, 50, 50))
        pygame.draw.rect(screen, yellow, (900, 120, 50, 50))
        pygame.draw.rect(screen, red, (900, 220, 50, 50))
        pygame.draw.rect(screen, green, (900, 320, 50, 50))
        pygame.draw.rect(screen, blue, (900, 420, 50, 50))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()


        screen.blit(save, save_rect)
        

        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == MOUSEBUTTONDOWN:
                mousedown = True
                if (950 >= mouse[0] >= 900) and (170 >= mouse[1] >= 120):
                    draw_color = yellow
                elif (950 >= mouse[0] >= 900) and (270 >= mouse[1] >= 220):
                    draw_color = red
                elif (950 >= mouse[0] >= 900) and (370 >= mouse[1] >= 320):
                    draw_color = green
                elif (950 >= mouse[0] >= 900) and (470 >= mouse[1] >= 420):
                    draw_color = blue
                elif (950 >= mouse[0] >= 900) and (70 >= mouse[1] >= 20):
                    draw_color = black
                elif (965 >= mouse[0] >= 885) and (530 >= mouse[1] >= 505):
                    fn += 1
                    pygame.image.save(screen, "_.jpg")
            elif event.type == MOUSEMOTION:
                if mousedown:
                    mousepos.append(event.pos)
            elif event.type == MOUSEBUTTONUP:
                mousedown = False
 
                
        if len(mousepos) > 1:
            pygame.draw.lines(screen, draw_color, False, mousepos)


        pygame.display.update()


if __name__ == '__main__':
    main()
