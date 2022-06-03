import pygame, sys
pygame.init()
window = pygame.display.set_mode((500,500))
pygame.display.set_caption("wasans")
clock = pygame.time.Clock()

class character :
    def __init__(self):
        self.x = 50
        self.y = 50

    def draw(self):
        pygame.draw.rect(window, (147,125,255), [self.x,self.y,20,20])
saebin = character()

while True:
    window.fill((0,0,0))

    saebin.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                saebin.y -= 10
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                saebin.y += 10
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                saebin.x -= 10 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                saebin.x += 10
    pygame.display.update()
    clock.tick(30)