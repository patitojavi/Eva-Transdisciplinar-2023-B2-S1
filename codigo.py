import pygame 

width = 1280
height = 720
rojo = (255,0,0)
negro =(0,0,0) 
screen = pygame.display.set_mode((width, height))

def init():
    pygame.init()
    pygame.display.set_caption('Plano Inclinado(Dinamica) - B2-S1')

def tri_rec(x, y, base, height, color):
    x1, y1 = x, y + height
    x2, y2 = x + base, y + height
    x3, y3 =  x + base, y
    pygame.draw.polygon(screen, color, [(x1, y1), (x2, y2), (x3, y3)])

def cuad_inclinado():
    pass


init()
running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255)) 
    tri_rec(200, 200, 1050, 500,(negro))
    pygame.display.flip()


pygame.quit()