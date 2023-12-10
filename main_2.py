import pygame
import random
import time
import button
import sys
from pygame.math import Vector2

class Fruit():
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        #draws the rectangle
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        window.blit(apple, fruit_rect)
        #pygame.draw.rect(window, (126,166,114), fruit_rect)
    
    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

class Snake():
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False

        self.head_down = pygame.image.load("Art/snake_head_down.png").convert_alpha()
        self.head_up = pygame.image.load("Art/snake_head_up.png").convert_alpha()
        self.head_right = pygame.image.load("Art/snake_head_right.png").convert_alpha()
        self.head_left = pygame.image.load("Art/snake_head_left.png").convert_alpha()

        self.butt_down = pygame.image.load("Art/snake_butt_down.png").convert_alpha()
        self.butt_up = pygame.image.load("Art/snake_butt_up.png").convert_alpha()
        self.butt_right = pygame.image.load("Art/snake_butt_right.png").convert_alpha()
        self.butt_left = pygame.image.load("Art/snake_butt_left.png").convert_alpha()

        self.mid_horizontal = pygame.image.load("Art/snake_mid_horizontal.png").convert_alpha()
        self.mid_vertical = pygame.image.load("Art/snake_mid_vertical.png").convert_alpha()

        self.turn_down_left = pygame.image.load("Art/snake_turn_down_left.png").convert_alpha()
        self.turn_down_right = pygame.image.load("Art/snake_turn_down_right.png").convert_alpha()
        self.turn_up_left = pygame.image.load("Art/snake_turn_up_left.png").convert_alpha()
        self.turn_up_right = pygame.image.load("Art/snake_turn_up_right.png").convert_alpha()

    def draw_snake(self):
        self.update_head_graphics()
        self.update_butt_graphics()

        for index,block in enumerate(self.body):
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)

            if index == 0:
                window.blit(self.head, block_rect) # if it's the start of the list, it's the head
            elif index == len(self.body) - 1:
                window.blit(self.butt, block_rect) # if it's the end of the list, it's the butt
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    window.blit(self.mid_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    window.blit(self.mid_horizontal, block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        window.blit(self.turn_down_left, block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        window.blit(self.turn_down_right, block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        window.blit(self.turn_up_left, block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        window.blit(self.turn_up_right, block_rect)

    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1, 0): self.head = self.head_left
        elif head_relation == Vector2(-1, 0): self.head = self.head_right
        elif head_relation == Vector2(0, 1): self.head = self.head_up
        elif head_relation == Vector2(0, -1): self.head = self.head_down
    
    def update_butt_graphics(self):
        butt_relation = self.body[-2] - self.body[-1]
        if butt_relation == Vector2(-1, 0): self.butt = self.butt_left
        elif butt_relation == Vector2(1, 0): self.butt = self.butt_right
        elif butt_relation == Vector2(0, -1): self.butt = self.butt_up
        elif butt_relation == Vector2(0, 1): self.butt = self.butt_down

    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:] # this bit right here is the addition of a block
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:    
            body_copy = self.body[:-1] # this is the movement, where it keeps adding one to the front and subtracking from the back
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

class Main():
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
            #add another block to the snake
    
    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()
        #check is snake is outside the screen
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
        #check is snake hits itself

    def game_over():
        pygame.quit()
        sys.exit()
            
# Default Amounts
_SNAKE_SPEED = 60

# Default Variables
direction = "RIGHT"
change_to = direction
running = True

# Initialize the pygame
pygame.init()

#Cell Sizes
cell_size = 40
cell_number = 20

# Initialize the game window
pygame.display.set_caption("Rachel's Snake Game")
icon = pygame.image.load(("Art/snake_head_up.png"))
pygame.display.set_icon(icon)
window = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size,))

# Images
bg = pygame.image.load("Background_Space.jpeg")
game_over_screen = pygame.image.load("game_over_screen.png")
apple = pygame.image.load("fruit.png").convert_alpha()

# FPS controller
fps = pygame.time.Clock()
window_update = pygame.USEREVENT
pygame.time.set_timer(window_update, 150)

#load button
start_img = pygame.image.load('start.png').convert_alpha()
exit_img = pygame.image.load('end.png').convert_alpha()
play_again_img = pygame.image.load('play_again.png').convert_alpha()

#create button instances
start_button = button.Button(100, 200, start_img, 1)
exit_button = button.Button(450, 200, exit_img, 1)
play_again = button.Button(100,200, play_again_img, 1)

main_game = Main()

def background(x, y):
   window.blit(bg, (x, y)) # Draws the Background

# Main Function
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == window_update:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)


    #if start_button.draw(window):
        #game_running()
    
    if exit_button.draw(window):
        running = False

        #This is the main chunk of the game


    background(0, 0)  # Bottom Layer
    #player(player_X, player_Y) # Top Layer
    main_game.draw_elements()
    pygame.display.update() #Refreshes
    fps.tick(_SNAKE_SPEED)
    # Controls
    

