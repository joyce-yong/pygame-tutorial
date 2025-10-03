import pygame
import math

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

def drawCircle(x, y, radius, lightPosition):
    for angle in range(360):
        radians = math.radians(angle)
        newX = x + radius * math.cos(radians)
        newY = y + radius * math.sin(radians) 
        
        # Calculates distance from light source
        distanceLight = math.hypot(lightPosition[0] - newX, lightPosition[1] - newY)  
        intensity = max(0, 255 - distanceLight)  # calculate the light intensity
                    
        # change the red color intensity  
        updateColor = (
            max(0, min(255 + intensity, 255)),
            max(0, min(0 + intensity, 255)),
            max(0, min(0 + intensity, 255))
        )

        # Draw a line from center to the edge
        pygame.draw.line(screen, updateColor, (x, y), (newX, newY))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((255,255,255))  # white background
    
    mousePos = pygame.mouse.get_pos()
    drawCircle(400, 300, 100, mousePos)  # draw at the center
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
