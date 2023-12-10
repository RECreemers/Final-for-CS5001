import pygame

pygame.init()  # This initialized the pygame features

snake_speed = 15
dis_width = 800
dis_height = 600

dis = pygame.display.set_mode((dis_width, dis_height))  # This sets the default size of the game window

# Caption and Icon (Title Screen)
pygame.display.set_caption(("Snake Game"))
icon = pygame.image.load(("Snake_Head.png"))
pygame.display.set_icon(icon)

# FPS (frames per second) controller
fps = pygame.time.Clock()

#Player
playerImg = pygame.image.load("Snake_Head.png")  # This is the picture of the main character
playerX = 300
playerY = 300
playerX_change = 0
playerY_change = 0
direction = "RIGHT"
change_to = direction

def player(x, y):
    dis.blit(playerImg,(x, y))

running = True  # This is the game loop right here
while running:

    dis.fill((0, 0, 0))
    #add bg image here

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  #Kicks you out of the while loop
    
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            change_to = "LEFT"
        if event.key == pygame.K_RIGHT:
            change_to = "RIGHT"
        if event.key == pygame.K_UP:
            change_to = "UP"
        if event.key == pygame.K_DOWN:
            change_to = "DOWN"

    #checks to makes sure you don't go backwards
    if change_to == "LEFT" and direction != "RIGHT":
        direction = "LEFT"
    if change_to == "RIGHT" and direction != "LEFT":
        direction = "RIGHT"
    if change_to == "UP" and direction != "DOWN":
        direction = "UP"
    if change_to == "DOWN" and direction != "UP":
        direction = "DOWN"

    if direction == "LEFT":
        playerX += -1
    if direction == "RIGHT":
        playerX += 1
    if direction == "UP":
        playerY += -1
    if direction == "DOWN":
        playerY += 1

    playerX += playerX_change
    playerY += playerY_change   # This how much the character moves left or right
   
    #Bounding Box
    if playerX <= 32:
        playerX = 32
    elif playerX >= 736:
        playerX = 736
    playerY += playerY_change  # This how much the character moves left or right
    if playerY <= 32:
        playerY = 32
    elif playerY >= 536:
        playerY = 536
    player(playerX, playerY)

    pygame.display.update()
    fps.tick(snake_speed)