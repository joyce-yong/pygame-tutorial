import pygame
import sys

pygame.init()

# Assets
backgroundImg = pygame.image.load("D:\\00 Zi Qing's Doc\\A University\\00 Degree\\Year 2\\Sem 2\\ISE\\Tutorial\\assets\\background.jpg")
characterWalkingImgs = [pygame.image.load(f"D:\\00 Zi Qing's Doc\\A University\\00 Degree\\Year 2\\Sem 2\\ISE\\Tutorial\\assets\\walking\\{i}.jpg")for i in range(1,5)]
riverImg = pygame.image.load("D:\\00 Zi Qing's Doc\\A University\\00 Degree\\Year 2\\Sem 2\\ISE\\Tutorial\\assets\\river.png")
platformImg = pygame.image.load("D:\\00 Zi Qing's Doc\\A University\\00 Degree\\Year 2\\Sem 2\\ISE\\Tutorial\\assets\\platform.png")
goalImg = pygame.image.load("D:\\00 Zi Qing's Doc\\A University\\00 Degree\\Year 2\\Sem 2\\ISE\\Tutorial\\assets\\goal.png")
treeImg = pygame.image.load("D:\\00 Zi Qing's Doc\\A University\\00 Degree\\Year 2\\Sem 2\\ISE\\Tutorial\\assets\\tree.jpeg")


# Scaling
riverImg = pygame.transform.scale_by(riverImg, (0.3))
platformImg = pygame.transform.scale_by(platformImg, (0.1))
backgroundImg = pygame.transform.scale(backgroundImg, (800, 600))
ObstacleImages = [riverImg,platformImg,goalImg, treeImg]
treeImg = pygame.transform.scale_by(treeImg, (0.5))

# Setup
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Adventure")

# Main character class
class Player(pygame.sprite.Sprite):
    # create a constructor for character
    def __init__(self):
        super().__init__()
        self.images = characterWalkingImgs
        self.currentImage = 0
        self.image = self.images[self.currentImage]
        self.rect = self.image.get_rect()
        self.rect.center = (100, 600 - 100)
        self.animationCounter = 0

    # function to move the object (player) left & right
    def move(self, direction):
        if direction == "left":
            self.rect.x -= 5
        if direction == "right":
            self.rect.x += 5

    # update the images (character move from left to right / right to left)
    def update(self, keys):
        moving = False
        if keys[pygame.K_LEFT]:
            self.move("left")
            moving = True
        elif keys[pygame.K_RIGHT]:
            self.move("right")
            moving = True

        if moving:
            self.animationCounter += 1
            print(self.animationCounter)
            if self.animationCounter % 5 == 0:
                self.currentImage = (self.currentImage + 1) % len(self.images)
                self.image = self.images[self.currentImage]
        else:
            self.animationCounter = 0
            self.currentImage = 0
            self.image = self.images[self.currentImage]

# Obstacle class
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, index, message, isGoal=False):
        super().__init__()
        self.image = ObstacleImages[index]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.message = message
        self._goal = isGoal

# Create objects
player = Player()
obstacle1 = Obstacle(150, 450, 0, "reach the river")
obstacle2 = Obstacle(350, 500, 1, "At the platform")
obstacle3 = Obstacle(500, 450, 2, "Blocked by the tree!")
goal = Obstacle(650, 500, 2, "Reach the Goal", True)

# Create sprite groups
all_sprites = pygame.sprite.Group()
obstacles = pygame.sprite.Group()

# Add obstacle & player into sprite
obstacles.add(obstacle1, obstacle2, obstacle3, goal)
all_sprites.add(player)
all_sprites.add(obstacles)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player.update(keys)

    # Check collisions
    collideObstacle = pygame.sprite.spritecollideany(player, obstacles)
    if collideObstacle:
        if collideObstacle._goal:
            print(collideObstacle.message)  # Winning message
            running = False  # End the game
        else:
            print(collideObstacle.message)

    screen.blit(backgroundImg, (0, 0))
    all_sprites.draw(screen)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

# end
pygame.time.delay(3000)  # 3 seconds
pygame.quit()
sys.exit()