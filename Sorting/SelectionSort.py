import pygame


def printArray(pygame, win, unsorted):
    x = 50
    y = 250
    i = 0
    delay = 1000
    print(unsorted)
    for data in unsorted:
        rect = pygame.draw.rect(win, (124, 252, 0), (x + i, y, width, height))
        text = font.render(str(data), True, (255, 0, 0))
        text_rect = text.get_rect()
        text_rect.x = x + i + (width / 3)
        text_rect.y = y + width / 3
        win.blit(text, text_rect)
        i = i + width + width
    pygame.display.update()
    pygame.time.delay(delay)
    pygame.event.get()



pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Selection Sort')
width = 40
height = 60
vel = 5
run = True
isJump = False
jumpCount = 10
unsorted = [5, 4, 10, 45,  3, 2]
win.fill((0, 0, 0))
bg = pygame.image.load("C:\\Work\\git\\python\\Games\\img\\bg.png")
win.blit(bg, (0, 0))
font = pygame.font.SysFont("comicsansms", 24)
text_header = font.render('       Selection Sort      ', True, (255, 0, 0))
header_rect = text_header.get_rect()
header_rect.y = 200
win.blit(text_header, header_rect)
outerCounter = 0
x = 0
y = 0
minElement = 0
minElementId = 0
printArray(pygame, win, unsorted)
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            print('Shutting down visualization')
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            print('Starting the sort')
            #looping over all the elements
            printArray(pygame, win, unsorted)
            for i, val in enumerate(unsorted):
                minElement = val
                minElementId = i
                for j, valElement in enumerate(unsorted):
                    if j <= i:
                        continue

                    if valElement < minElement:
                        minElement = valElement
                        minElementId = j

                #At end of this we know the least elemet
                temp = val
                unsorted[i] = minElement
                unsorted[minElementId] = val
                printArray(pygame, win, unsorted)

            printArray(pygame, win, unsorted)

    pygame.time.delay(1000)

