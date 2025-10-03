import pygame
import math

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

def drawCircle(x, y, radius, lightPosition):

    pygame.draw.circle(screen, (255,0,0), (x, y), radius)
    
    for angle in range(360):
        radians = math.radians(angle)
        newX = x + radius * math.cos(radians)
        newY = y + radius * math.sin(radians) 
           
        distanceLight = math.hypot(lightPosition[0] - newX, lightPosition[1] - newY) #Calculates the distance from the light source. (square root of the sum of squares) 
        intensity = max(0, 255 - distanceLight) # calculate the light intensity
                    
        # change the red color intensity  
        updateColor = (max(0, min(255 + intensity, 255)),
                            max(0, min(0 + intensity, 255)),
                            max(0, min(0 + intensity, 255)))
    
    pygame.draw.circle(screen, updateColor, (x,y), radius) 
            
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((255,255,255)) #white background
    
    mousePos = pygame.mouse.get_pos()
    drawCircle(400, 300, 100, mousePos) #draw at the center
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
