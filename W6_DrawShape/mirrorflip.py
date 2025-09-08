import pygame
import math

pygame.init()

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Geometry shape")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0,0,255)
BLACK = (0,0,0)

# draw a shape
def drawShape(surface, color, points):
    pygame.draw.polygon(surface, color, points)

# rotate the shape
def rotate(point, angle, center):
    angleRadian = math.radians(angle)
    x, y = point
    cx, cy = center
    x -= cx
    y -= cy
    newX = x * math.cos(angleRadian) - y * math.sin(angleRadian)
    newY = x * math.sin(angleRadian) + y * math.cos(angleRadian)
    return newX + cx, newY + cy

running = True
angle = 0
scale = 1
mirrorX, mirrorY = 1, 1  # mirror flags
ScreenCenterX, ScreenCenterY = 400, 300

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN: # transformation
            if event.key == pygame.K_LEFT:
                ScreenCenterX -= 10
            elif event.key == pygame.K_RIGHT:
                ScreenCenterX += 10
            elif event.key == pygame.K_UP:
                ScreenCenterY -= 10
            elif event.key == pygame.K_DOWN:
                ScreenCenterY += 10
            elif event.key == pygame.K_r:
                angle += 5
            elif event.key == pygame.K_a:
                angle -= 5
            elif event.key == pygame.K_s:
                scale += 0.1
            elif event.key == pygame.K_c:
                scale -= 0.1
            elif event.key == pygame.K_h:   # Flip horizontally
                mirrorX *= -1
            elif event.key == pygame.K_v:   # Flip vertically
                mirrorY *= -1

    window.fill(WHITE)

    # Triangle roof
    pointsA = [(ScreenCenterX, ScreenCenterY - 50),
               (ScreenCenterX - 50, ScreenCenterY + 50),
               (ScreenCenterX + 50, ScreenCenterY + 50)]

    # Square body
    pointsB = [(ScreenCenterX-50, ScreenCenterY),
               (ScreenCenterX-50, ScreenCenterY+50),
               (ScreenCenterX+50, ScreenCenterY+50),
               (ScreenCenterX+50, ScreenCenterY)]

    # Door
    pointsC = [(ScreenCenterX-10, ScreenCenterY+10),
               (ScreenCenterX-10, ScreenCenterY+50),
               (ScreenCenterX+10, ScreenCenterY+50),
               (ScreenCenterX+10, ScreenCenterY+10)]

    def transform(points):
        return [rotate(((x - ScreenCenterX) * scale * mirrorX + ScreenCenterX,
                        (y - ScreenCenterY) * scale * mirrorY + ScreenCenterY),
                        angle, (ScreenCenterX, ScreenCenterY)) for x, y in points]

    TpointsA = transform(pointsA)
    TpointsB = transform(pointsB)
    TpointsC = transform(pointsC)

    drawShape(window, RED, TpointsA)
    drawShape(window, BLUE, TpointsB)
    drawShape(window, BLACK, TpointsC)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
