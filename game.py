import pygame
pygame.init()

w, h = 400, 400

win = pygame.display.set_mode((w,h))
clock = pygame.time.Clock()
player = pygame.Rect(180, 180, 40, 40)
run = True

while run:
    clock.tick(60)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]: player.x -= 5
    if key[pygame.K_RIGHT]: player.x += 5
    if key[pygame.K_UP]: player.y -= 5
    if key[pygame.K_DOWN]: player.y += 5
    win.fill((255,255,255))
    pygame.draw.rect(win, (0,0,255), player)
    pygame.display.flip()

pygame.quit()
