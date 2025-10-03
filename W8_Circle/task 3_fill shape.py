import pygame
import math

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Load texture
texture = pygame.image.load("D:\\GitHub\\pygame-tutorial\\W8_Circle\\rock texture.jpg").convert()
texture = pygame.transform.scale(texture, (200, 200))  # scale to circle size

def drawTexturedCircle(x, y, radius, lightPos):
    # Create a surface with per-pixel alpha
    circle_surface = pygame.Surface((radius*2, radius*2), pygame.SRCALPHA)

    # Fill surface with texture
    for i in range(0, radius*2, texture.get_width()):
        for j in range(0, radius*2, texture.get_height()):
            circle_surface.blit(texture, (i, j))

    # Mask it to a circle
    mask = pygame.Surface((radius*2, radius*2), pygame.SRCALPHA)
    pygame.draw.circle(mask, (255, 255, 255, 255), (radius, radius), radius)
    circle_surface.blit(mask, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

    # Apply lighting effect pixel by pixel
    for i in range(radius*2):
        for j in range(radius*2):
            dx = (x - radius + i) - lightPos[0]
            dy = (y - radius + j) - lightPos[1]
            dist = math.hypot(dx, dy)

            # intensity decreases with distance
            intensity = max(50, 255 - int(dist)) 
            r, g, b, a = circle_surface.get_at((i, j))
            if a > 0:  
                new_color = (
                    r * intensity // 255,
                    g * intensity // 255,
                    b * intensity // 255,
                    a
                )
                circle_surface.set_at((i, j), new_color)

    screen.blit(circle_surface, (x-radius, y-radius))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((255, 255, 255))
    mousePos = pygame.mouse.get_pos()
    drawTexturedCircle(400, 300, 100, mousePos)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
