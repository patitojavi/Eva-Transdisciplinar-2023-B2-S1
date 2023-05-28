import pygame


pygame.init()


width, height = 1000, 600
negro = (0,0,0)
blanco = (255,255,255)
azul = (0, 0, 255)
verde = (0, 255, 0)
rojo = (255, 0, 0)
amarillo = (255, 255, 0)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Subsuperficies en Pygame")


surface = pygame.Surface((width, height))
surface.fill((255, 255, 255))  

subsurface1_rect = pygame.Rect(0, 0, 500,500)
subsurface2_rect = pygame.Rect(500, 0, 500, 300)
subsurface3_rect = pygame.Rect(0, 300, 500, 300)
subsurface4_rect = pygame.Rect(500, 300, 500, 300)

subsurface1 = surface.subsurface(subsurface1_rect)
subsurface2 = surface.subsurface(subsurface2_rect)
subsurface3 = surface.subsurface(subsurface3_rect)
subsurface4 = surface.subsurface(subsurface4_rect)

subsurface1.fill(blanco)  
subsurface2.fill(blanco)  
subsurface3.fill(blanco)  
subsurface4.fill(blanco)

line_color = negro
line_ancho = 2
pygame.draw.line(surface,negro,(0,300),(1000,300),line_ancho)
pygame.draw.line(surface,negro,(500,0),(500,600),line_ancho)
pygame.draw.line(surface,negro,(0,1),(1000,1),5)
pygame.draw.line(surface,negro,(0,0),(0,0),1)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.blit(surface, (0, 0))

    pygame.display.flip()


pygame.quit()