import pygame

pygame.init()
okno = pygame.display.set_mode((600, 600))
pygame.display.set_caption("PySnake - Test")
hodiny = pygame.time.Clock()

bezi = True
while bezi:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            bezi = False

    okno.fill((20, 20, 30))
    pygame.display.flip()
    hodiny.tick(60)

pygame.quit()