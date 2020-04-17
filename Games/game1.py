import pygame
pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption('First Game')
x = 50
y = 50
width = 40
height = 60
vel = 5
run = True
isJump = False
jumpCount = 10
while run:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            print('Shutting down the game')
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 500 - width - vel:
        x += vel
    if keys[pygame.K_UP] and y > vel:
        y -= vel
    if keys[pygame.K_DOWN] and y < 500 - width - vel:
        y += vel
    if keys[pygame.K_SPACE]:
        isJump = True
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (250, 0, 0), (x, y, width, height))
    pygame.display.update()
    #print('this is the main game loop')
pygame.quit()
