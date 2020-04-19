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
pygame.display.set_caption('Bubble Sort')
width = 40
height = 60
vel = 5
run = True
isJump = False
jumpCount = 10
unsorted = [5, 4, 3, 2, 1]
win.fill((0, 0, 0))
bg = pygame.image.load("C:\\Work\\git\\python\\Games\\img\\bg.png")
win.blit(bg, (0, 0))
font = pygame.font.SysFont("comicsansms", 24)
text_header = font.render('       Bubble Sort      ', True, (255, 0, 0))
header_rect = text_header.get_rect()
header_rect.y = 200
win.blit(text_header, header_rect)
outerCounter = 0
x = 0
y = 0
printArray(pygame, win, unsorted)
while run:
    while x < len(unsorted):
        y = 0
        while y < len(unsorted) - 1:
            if unsorted[y] > unsorted[y + 1]:
                temp = unsorted[y]
                unsorted[y] = unsorted[y + 1]
                unsorted[y+1] = temp
                #print('making swap')
            printArray(pygame, win, unsorted)
            y = y + 1
        printArray(pygame, win, unsorted)
        x = x + 1
    #print('In the main loop1')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            print('Shutting down visualization')
    pygame.time.delay(2000)

