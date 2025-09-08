# Lab 1 Recap
# Q1
# i = 0
#
# while i != -1:
#     i = int(input("type a number"))
# else:
#     print("you've got the correct number!")

# Q2
# def multiplyList(lst, num):
#     return [element * num for element in lst]
#
# a = [1, 2, 3, 4]
# b = 5
#
# updated_list = multiplyList(a, b)
# print(updated_list)

# Exercise a
# matrix1 = [
# [-1, 0],
# [0, 1],
# ]
#
# matrix2 = [
# [-1, 2],
# [3, -2],
# ]
#
# rmatrix = [
#     [0, 0],
#     [0, 0],
#     ]
#
# for i in range(len(matrix1)):
#     for j in range(len(matrix1[0])):
#         rmatrix[i][j] = matrix1[i][j] - matrix2[i][j]
#
# for r in rmatrix:
#     print(r)
#
# # Exercise b
# matrix1 = [
#  [1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9],
#  ]
# rmatrix = [
#  [0, 0, 0],
#  [0, 0, 0],
#  [0, 0, 0],
#  ]
#
# for i in range(len(matrix1)):
#     for j in range(len(matrix1[0])):
#         rmatrix[i][j] = matrix1[i][j] * 10
#
# for r in rmatrix:
#     print(r)

# ----------------------------------------
# Lab 2 - Media Acquisition

# # Capture Image
# import cv2
# cam = cv2.VideoCapture(0)
#
# if not cam.isOpened():
#     print("not able to open computer camera")
#     exit()
#
# while True:
#     result, image = cam.read()
#     cv2.imshow('Captured Image', image)
#
#     key = cv2.waitKey(1) & 0xFF
#     if cv2.waitKey(1) == ord('c'):
#         cv2.imwrite("myimage.png", image)
#     elif cv2.waitKey(1) == ord('q'):
#         break
# cv2.destroyAllWindows()
# cam.release()


# # Capture video
# import cv2
#
# cam = cv2.VideoCapture(0)
#
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# videoWriter = cv2.VideoWriter('myvideo.avi', fourcc, 20.0,
#                               (640, 480))
#
# if not cam.isOpened():
#     print("not able to open computer camera")
#     exit()
#
# while True:
#     result, image = cam.read()
#     if not result:
#         print("Not able to capture frame (stream ending)")
#     cv2.imshow('Captured Image', image)
#
#     videoWriter.write(image)
#     if cv2.waitKey(1)  == ord('q'):
#         break
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
# cam.release()

# Sound Recording
# import sounddevice as sd
# import wavio
#
# duration = 5
# fs = 44100
# channels = 2
#
# print("start recording...")
#
# audio = sd.rec(int(duration * fs), samplerate = fs, channels = channels)
# sd.wait()
#
# wavio.write("mysound.wav", audio, fs, sampwidth = 2)
# print("completed recording")

# Screen Recording
# import dxcam
# import cv2
#
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# videoWriter = cv2.VideoWriter('myScrCapture.mp4', fourcc, 20.0, (1920, 1080))
#
# camera = dxcam.create(output_idx = 0, output_color = "BGR")
# camera.start(target_fps = 20, video_mode = True)
# print("Start recording.......")
#
# for i in range(500):
#     videoWriter.write(camera.get_latest_frame())
#
# videoWriter.release()
# camera.stop()
# print("Completed recording")

# Capture video and audio
# import subprocess
#
# output_file = "output.mp4v"
#
# # FFmpeg command to record from default camera + default microphone
# command = [
#     "ffmpeg",
#     "-y",                      # overwrite if file exists
#     "-f", "dshow",             # Windows DirectShow
#     "-i", "video=Integrated Camera:audio=Microphone (Realtek Audio)",  # change to your device names
#     "-vcodec", "libx264",      # video codec
#     "-preset", "ultrafast",    # encoding speed
#     "-crf", "23",              # quality
#     "-acodec", "aac",          # audio codec
#     output_file
# ]
#
# print("Recording... Press Ctrl+C to stop.")
# try:
#     subprocess.run(command)
# except KeyboardInterrupt:
#     print("\nStopped recording.")

# ---------------- PYGAME
# import pygame
# import sys
#
# pygame.init()
#
# screen = pygame.display.set_mode((1000, 800))
# background_color = (0, 128, 255)
# pygame.display.set_caption("my Game Windows")
#
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     screen.fill(background_color)
#     pygame.display.flip()
#
# pygame.quit()
# sys.exit()

# ------------------- Import image and background
# import pygame
# import sys
#
# def resizeObject(originObject, scaledFactor):
#     scaledObject = pygame.transform.scale_by(originObject, scaledFactor)
#     return (scaledObject)
#
# pygame.init()
#
# screen = pygame.display.set_mode((1000, 800))
# background_color = (0,128, 255)
# pygame.display.set_caption("my Game Windows")
#
# background = pygame.image.load("D:\\00 Zi Qing's Doc\\A University\\00 Degree\\Year 2\\Sem 2\\ISE\\Tutorial\\background.svg")
#
# character = pygame.image.load("D:\\00 Zi Qing's Doc\\A University\\00 Degree\\Year 2\\Sem 2\\ISE\\Tutorial\\pochacco.svg")
#
# UpdatedBackground = pygame.transform.scale(background, (1000, 800))
# updatedcharacter = resizeObject(character, 0.5)
#
# charRectBlock = updatedcharacter.get_rect()
#
# charRectBlock.center = (800, 500)
#
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_LEFT]:
#         charRectBlock.x -= 5
#     if keys[pygame.K_RIGHT]:
#         charRectBlock.x += 5
#     if keys[pygame.K_UP]:
#         charRectBlock.y -= 5
#     if keys[pygame.K_DOWN]:
#         charRectBlock.y += 5
#
#     screen.fill(background_color)
#
#     screen.blit(UpdatedBackground, (0, 0))
#     screen.blit(updatedcharacter, charRectBlock)
#
#     pygame.display.flip()
#
# print("closing...")
# pygame.quit()
# sys.exit()

# ---------------- RESIZE
# import pygame
# import sys
#
# def resizeObject(originObject, scaledFactor):
#     scaledObject = pygame.transform.scale_by(originObject, scaledFactor)
#     return (scaledObject)
#
# pygame.init()
#
# screen = pygame.display.set_mode((1000, 800))
# # background_color = (0, 128, 255)
# pygame.display.set_caption("my Game Windows")
#
# background = pygame.image.load("D:\\00 Zi Qing's Doc\\A University\\00 Degree\\Year 2\\Sem 2\\ISE\\Tutorial\\background.svg")
#
# character = pygame.image.load("D:\\00 Zi Qing's Doc\\A University\\00 Degree\\Year 2\\Sem 2\\ISE\\Tutorial\\pochacco.svg")
#
# UpdatedBackground = pygame.transform.scale(background, (1000, 800))
# updatedcharacter = resizeObject(character, 0.5)
#
# charRectBlock = updatedcharacter.get_rect()
#
# charRectBlock.center = (400, 500)
#
# font = pygame.font.Font(None, 36)
#
# dialogue = [
#     "Welcome to the ISE class!",
#     "It is Monday Zzzz....",
#     "Greeting.....",
#     "Jiayou"
# ]
#
# currLine = 0
# diaTime = 0
# diaInterval = 3000
# clock = pygame.time.Clock()
#
# def renderDialogue():
#     global currLine
#     if currLine < len(dialogue):
#         contentSurface = font.render(dialogue[currLine], True, (255,0,0))
#         textRect = contentSurface.get_rect(center = (200, 50))
#         screen.blit(contentSurface, textRect)
#
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_LEFT]:
#         charRectBlock.x -= 5
#     if keys[pygame.K_RIGHT]:
#         charRectBlock.x += 5
#     if keys[pygame.K_UP]:
#         charRectBlock.y -= 5
#     if keys[pygame.K_DOWN]:
#         charRectBlock.y += 5
#
#     diaTime += clock.get_time()
#     if diaTime >= diaInterval:
#         currLine += 1
#         diaTime = 0
#
#     # screen.fill(background_color)
#
#     screen.blit(UpdatedBackground, (0, 0))
#     screen.blit(updatedcharacter, charRectBlock)
#     renderDialogue()
#
#     pygame.display.flip()
#
#     clock.tick(60)
#
# print("closing...")
# pygame.quit()
# sys.exit()

# --------------- TIMER
# import pygame
# import sys
#
# def resizeObject(originObject, scaledFactor):
#     scaledObject = pygame.transform.scale_by(originObject, scaledFactor)
#     return (scaledObject)
#
# pygame.init()
#
# screen = pygame.display.set_mode((1000, 800))
# background_color = (0, 128, 255)
# pygame.display.set_caption("my Game Windows")
#
# background = pygame.image.load("D:\\00 Zi Qing's Doc\\A University\\00 Degree\\Year 2\\Sem 2\\ISE\\Tutorial\\background.svg")
#
# character = pygame.image.load("D:\\00 Zi Qing's Doc\\A University\\00 Degree\\Year 2\\Sem 2\\ISE\\Tutorial\\pochacco.svg")
#
# UpdatedBackground = pygame.transform.scale(background, (1000, 800))
# updatedcharacter = resizeObject(character, 0.5)
#
# charRectBlock = updatedcharacter.get_rect()
#
# charRectBlock.center = (400, 500)
#
# font = pygame.font.Font(None, 36)
#
# dialogue = [
#     "Welcome to the ISE class!",
#     "It is Monday Zzzz....",
#     "Greeting.....",
#     "Jiayou"
# ]
#
# currLine = 0
# diaTime = 0
# diaInterval = 3000
# clock = pygame.time.Clock()
#
# def renderDialogue():
#     global currLine
#     if currLine < len(dialogue):
#         contentSurface = font.render(dialogue[currLine], True, (255,0,0))
#         textRect = contentSurface.get_rect(center = (200, 50))
#         screen.blit(contentSurface, textRect)
#
# GameTime = 60
# countdownEvent = pygame.USEREVENT + 1
# pygame.time.set_timer(countdownEvent, 1000)
#
# def displayTimer():
#     TimerSurface = font.render(f"Time: {GameTime}", True, (0,0,0))
#     TimerRect = TimerSurface.get_rect(topright = (950, 50))
#     TimerBackground = pygame.Rect(TimerRect.left - 2, TimerRect.top - 2, TimerRect.width + 2, TimerRect.height + 2)
#     pygame.draw.rect(screen, (255, 255, 255), TimerBackground)
#     screen.blit(TimerSurface, TimerRect)
#
#
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == countdownEvent:
#             GameTime -= 1
#             if GameTime <= 0:
#                 GameTime = 0
#
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_LEFT]:
#         charRectBlock.x -= 5
#     if keys[pygame.K_RIGHT]:
#         charRectBlock.x += 5
#     if keys[pygame.K_UP]:
#         charRectBlock.y -= 5
#     if keys[pygame.K_DOWN]:
#         charRectBlock.y += 5
#
#     diaTime += clock.get_time()
#     if diaTime >= diaInterval:
#         currLine += 1
#         diaTime = 0
#
#     screen.fill(background_color)
#
#     screen.blit(UpdatedBackground, (0, 0))
#     screen.blit(updatedcharacter, charRectBlock)
#     renderDialogue()
#     displayTimer()
#
#     pygame.display.flip()
#
#     clock.tick(60)
#
# print("closing...")
# pygame.quit()
# sys.exit()

# --------------------------------------
# W4
# import pygame
# import sys
#
# pygame.init()
#
# # Assets
# backgroundImg = pygame.image.load("C:\\Users\\User\\OneDrive\\APU Degree\\Y2 Sem 2\\ISE\\Week 4 Tutorial\\background.jpg")
# characterWalkingImgs = [pygame.image.load(f"C:\\Users\\User\\OneDrive\\APU Degree\\Y2 Sem 2\\ISE\\Week 4 Tutorial\\{i}.png")for i in range(1,5)]
# riverImg = pygame.image.load("C:\\Users\\User\\OneDrive\\APU Degree\\Y2 Sem 2\\ISE\\Week 4 Tutorial\\river.png")
# platformImg = pygame.image.load("C:\\Users\\User\\OneDrive\\APU Degree\\Y2 Sem 2\\ISE\\Week 4 Tutorial\\platform.png")
# goalImg = pygame.image.load("C:\\Users\\User\\OneDrive\\APU Degree\\Y2 Sem 2\\ISE\\Week 4 Tutorial\\goal.png")
#
# # Scaling
# riverImg = pygame.transform.scale_by(riverImg, (0.3))
# platformImg = pygame.transform.scale_by(platformImg, (0.1))
# backgroundImg = pygame.transform.scale(backgroundImg, (800, 600))
# ObstacleImages = [riverImg,platformImg,goalImg]
#
# # Setup
# screen = pygame.display.set_mode((800, 600))
# pygame.display.set_caption("My Adventure")
#
# # Main character class
# class Player(pygame.sprite.Sprite):
#     # create a constructor for character
#     def __init__(self):
#         super().__init__()
#         self.images = characterWalkingImgs
#         self.currentImage = 0
#         self.image = self.images[self.currentImage]
#         self.rect = self.image.get_rect()
#         self.rect.center = (100, 600 - 100)
#         self.animationCounter = 0
#
#     # function to move the object (player) left & right
#     def move(self, direction):
#         if direction == "left":
#             self.rect.x -= 5
#         if direction == "right":
#             self.rect.x += 5
#
#     # update the images (character move from left to right / right to left)
#     def update(self, keys):
#         moving = False
#         if keys[pygame.K_LEFT]:
#             self.move("left")
#             moving = True
#         elif keys[pygame.K_RIGHT]:
#             self.move("right")
#             moving = True
#
#         if moving:
#             self.animationCounter += 1
#             print(self.animationCounter)
#             if self.animationCounter % 5 == 0:
#                 self.currentImage = (self.currentImage + 1) % len(self.images)
#                 self.image = self.images[self.currentImage]
#         else:
#             self.animationCounter = 0
#             self.currentImage = 0
#             self.image = self.images[self.currentImage]
#
# # Obstacle class
# class Obstacle(pygame.sprite.Sprite):
#     def __init__(self, x, y, index, message, isGoal=False):
#         super().__init__()
#         self.image = ObstacleImages[index]
#         self.rect = self.image.get_rect()
#         self.rect.topleft = (x, y)
#         self.message = message
#         self._goal = isGoal
#
# # Create objects
# player = Player()
# obstacle1 = Obstacle(150, 450, 0, "reach the river")
# obstacle2 = Obstacle(350, 500, 1, "At the platform")
# goal = Obstacle(650, 500, 2, "Reach the Goal", True)
#
# # Create sprite groups
# all_sprites = pygame.sprite.Group()
# obstacles = pygame.sprite.Group()
#
# # Add obstacle & player into sprite
# obstacles.add(obstacle1, obstacle2, goal)
# all_sprites.add(player)
# all_sprites.add(obstacles)
#
# # Game loop
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     keys = pygame.key.get_pressed()
#     player.update(keys)
#
#     # Check collisions
#     collideObstacle = pygame.sprite.spritecollideany(player, obstacles)
#     if collideObstacle:
#         if collideObstacle._goal:
#             print(collideObstacle.message)  # Winning message
#             running = False  # End the game
#         else:
#             print(collideObstacle.message)
#
#     screen.blit(backgroundImg, (0, 0))
#     all_sprites.draw(screen)
#
#     pygame.display.flip()
#     pygame.time.Clock().tick(60)
#
# # end
# pygame.time.delay(3000)  # 3 seconds
# pygame.quit()
# sys.exit()

# ===================

import pygame
import sys

pygame.init()

# setup
WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Movement example")

characterSprite = pygame.image.load(r"D:\\00 Zi Qing's Doc\\A University\\00 Degree\\Year 2\\Sem 2\\ISE\\Tutorial\\w4\\Walk.png").convert_alpha()

characterSprite = pygame.transform.scale_by(characterSprite,0.3)
spriteSheetWidth = characterSprite.get_width()
spriteSheetHeight = characterSprite.get_height()

numWalkingFrames = 4
characterFrameWidth = spriteSheetWidth // numWalkingFrames
characterFrameHeight = spriteSheetHeight // 2  # 2 rows

# Extract frames
def extractFrames(sheet, row, numFrames):
    frames = []
    for i in range(numFrames):
        frame = sheet.subsurface(pygame.Rect(i * characterFrameWidth, row * characterFrameHeight, characterFrameWidth, characterFrameHeight))
        frames.append(frame)
    return frames

walkingRightFrames = extractFrames (characterSprite, 0, numWalkingFrames)
walkingLeftFrames = [pygame.transform.flip(walkingframe, True, False) for walkingframe in walkingRightFrames]

jumpingFrame = extractFrames (characterSprite, 1, 1)[0]

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.walkingRightFrames = walkingRightFrames
        self.walkingLeftFrames = walkingLeftFrames
        self.jumpingFrame = jumpingFrame
        self.image = self.walkingRightFrames[0]
        self.rect = self.image.get_rect(midbottom=(WIDTH // 2, HEIGHT - 50))
        self.velocityY = 0
        self.onGround = True
        self.frameIndex = 0
        self.direction = 0
        self.facingRight = True


    def update(self):
        keys = pygame.key.get_pressed()
        self.direction = 0

        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
            self.direction = -1
            self.facingRight = False
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
            self.direction = 1
            self.facingRight = True
        if keys[pygame.K_SPACE] and self.onGround:
            self.velocityY = -15
            self.onGround = False

        self.velocityY += 1
        self.rect.y += self.velocityY

        if self.rect.bottom >= HEIGHT - 50:
            self.rect.bottom = HEIGHT - 50
            self.velocityY = 0
            self.onGround = True

        # Animation
        if not self.onGround:
            self.image = self.jumpingFrame
        elif self.direction != 0:
            self.frameIndex = (self.frameIndex + 1) % len(self.walkingRightFrames)
            if self.facingRight:
                self.image = self.walkingRightFrames[self.frameIndex]
            else:
                self.image = self.walkingLeftFrames[self.frameIndex]
        else:
            self.image = self.walkingRightFrames[0] if self.facingRight else self.walkingLeftFrames[0]

player = Player()
allSprites = pygame.sprite.Group(player)

clock = pygame.time.Clock()
running = True
while running:
        screen.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        allSprites.update()
        allSprites.draw(screen)

        pygame.display.flip()
        clock.tick(30)

pygame.quit()
sys.exit()


