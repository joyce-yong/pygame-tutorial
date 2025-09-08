import pygame

pygame.init()

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Geometry shape")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0,0,255)

# draw a shape
def drawShape(surface, color, points):
    pygame.draw.polygon(surface, color, points)

running = True
ScreenCenterX, ScreenCenterY = 400, 300
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill(WHITE)

    pointsA = [(ScreenCenterX, ScreenCenterY - 50), (ScreenCenterX - 50, ScreenCenterY + 50), (ScreenCenterX + 50, ScreenCenterY + 50)]
    pointsB = [ (ScreenCenterX-50, ScreenCenterY), (ScreenCenterX-50, ScreenCenterY+50),(ScreenCenterX+50,ScreenCenterY+50),(ScreenCenterX+50,ScreenCenterY)]

    drawShape(window, RED, pointsA)
    drawShape(window, BLUE, pointsB)
    
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
