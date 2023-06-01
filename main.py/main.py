import pygame, sys

gravedad = True
SPEED= 5
FPS= 25
ancho= 800
alto=600
centro= (ancho//2, alto //2)
ROJO= (255, 0, 0)
AZUL= (0,0,255)
VERDE= (0,255,0)
BLANCO= (255,255,255)
AMARILLO= (255,255,0)
NEGRO= (0,0,0)
CYAN= (0,255,255)
pygame.init()

display = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Mi primer juego")
clock = pygame.time.Clock()

pepe= pygame.surface.Surface((120, 80))
pepe.fill(CYAN)
rect_pepe= pepe.get_rect()
rect_pepe.center= centro
while True:
    clock.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()

    display.fill(ROJO)
    
    if gravedad:
        if rect_pepe.bottom <= alto:
            rect_pepe.centery = rect_pepe.centery + SPEED
        else: 
            gravedad = False
    
    else:
        if rect_pepe.top >= 0:
            rect_pepe.centery = rect_pepe.centery - SPEED
        else:
            gravedad= True
            
    display.blit(pepe, rect_pepe)

    pygame.draw.line(display, NEGRO, (ancho//2, 0), (ancho//2, alto))
    pygame.display.flip()

  







































  ##  pygame.draw.rect(display, ROJO, (150, 70, 100, 70),5 )
    ##pygame.draw.rect(display, VERDE, (470,48, 70, 60))
    ##pygame.draw.circle(display, CYAN, (600,200), 120)
   ## pygame.draw.ellipse(display, AMARILLO, (580, 389,400), 7)
    ##pygame.draw.line(display, AZUL, (0,0), (ancho, alto), 5)