import pygame, random, time, sys, button
from pygame.math import Vector2
from pygame import mixer

#This is where the game runs
class Snake():
    """
    Makes snake bounding box
    Determines how snake moves - modifiying list through Vector2
    Adds all snake images needed
    Creates way for blocks to be added to snake
    """
    def __init__(self):
        #Put all the snake basics in here
        self.snake_body = [Vector2(4, 10), Vector2(3, 10), Vector2(2, 10)] # Starts with 3 body pieces
        self.direction = Vector2(1,0)  # Start going to the right
        self.add_snake_block = False

        #All the snake body images
        self.head_down = pygame.image.load("Art/Player_Graphics/snake_head_down.png").convert_alpha()
        self.head_up = pygame.image.load("Art/Player_Graphics/snake_head_up.png").convert_alpha()
        self.head_right = pygame.image.load("Art/Player_Graphics/snake_head_right.png").convert_alpha()
        self.head_left = pygame.image.load("Art/Player_Graphics/snake_head_left.png").convert_alpha()

        self.butt_down = pygame.image.load("Art/Player_Graphics/snake_butt_down.png").convert_alpha()
        self.butt_up = pygame.image.load("Art/Player_Graphics/snake_butt_up.png").convert_alpha()
        self.butt_right = pygame.image.load("Art/Player_Graphics/snake_butt_right.png").convert_alpha()
        self.butt_left = pygame.image.load("Art/Player_Graphics/snake_butt_left.png").convert_alpha()

        self.mid_horizontal = pygame.image.load("Art/Player_Graphics/snake_mid_horizontal.png").convert_alpha()
        self.mid_vertical = pygame.image.load("Art/Player_Graphics/snake_mid_vertical.png").convert_alpha()

        self.turn_down_left = pygame.image.load("Art/Player_Graphics/snake_turn_down_left.png").convert_alpha()
        self.turn_down_right = pygame.image.load("Art/Player_Graphics/snake_turn_down_right.png").convert_alpha()
        self.turn_up_left = pygame.image.load("Art/Player_Graphics/snake_turn_up_left.png").convert_alpha()
        self.turn_up_right = pygame.image.load("Art/Player_Graphics/snake_turn_up_right.png").convert_alpha()
    
    def draw_snake(self):
        self.update_head_graphics()
        self.update_butt_graphics()

        for index,block in enumerate(self.snake_body):
            snake_rect = pygame.Rect(int(block.x * cell_size), int(block.y * cell_size), cell_size, cell_size)

            if index == 0:
                screen.blit(self.head, snake_rect)
            elif index == len(self.snake_body) - 1:
                screen.blit(self.butt, snake_rect)
            else:
                previous_block = self.snake_body[index + 1] - block
                next_block = self.snake_body[index - 1] - block
                # This is the straight up/down/left/right section of drawing
                if previous_block.y == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.y == -1:
                    screen.blit(self.mid_vertical, snake_rect)
                elif previous_block.x == -1 and next_block.x == 1 or previous_block.x == 1 and next_block.x == -1:
                    screen.blit(self.mid_horizontal, snake_rect)
                # This is the turning section of drawing
                elif previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                    screen.blit(self.turn_down_left, snake_rect)
                elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                    screen.blit(self.turn_up_right, snake_rect)
                elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                    screen.blit(self.turn_down_right, snake_rect)
                elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                    screen.blit(self.turn_up_left, snake_rect)

    def move_snake(self):
        if self.add_snake_block == True:
            snake_body_copy = self.snake_body[:]
            snake_body_copy.insert(0,snake_body_copy[0] + self.direction)
            self.snake_body = snake_body_copy[:]
            self.add_snake_block = False
        else:
            snake_body_copy = self.snake_body[:-1]
            snake_body_copy.insert(0, snake_body_copy[0] + self.direction)
            self.snake_body = snake_body_copy[:]

    def add_block(self):
        self.add_snake_block = True

    def update_head_graphics(self):
        head_relation = self.snake_body[0] - self.snake_body[1]
        if head_relation.x == 1:
            self.head = self.head_right
        elif head_relation.x == -1:
            self.head = self.head_left
        elif head_relation.y == 1:
            self.head = self.head_down
        elif head_relation.y == -1:
            self.head = self.head_up

    def update_butt_graphics(self):
        butt_relation = self.snake_body[-2] - self.snake_body[-1]
        if butt_relation.x == 1:
            self.butt = self.butt_right
        elif butt_relation.x == -1:
            self.butt = self.butt_left
        elif butt_relation.y == 1:
            self.butt = self.butt_down
        elif butt_relation.y == -1:
            self.butt = self.butt_up

    def snake_music(self):
        main_song = mixer.music.load("Art/Music/main_theme.mp3")
        #fast_song = mixer.music.load("Art/Music/star_theme.mp3")
        mixer.music.set_volume(1)
        mixer.music.play(1, 9.0)

class Fruit():
    """
    Makes bounding box for fruit
    Puts fruit image on screen
    When collided with, 
    
    """
    def __init__(self):
        self.apple = pygame.image.load("Art/UI_Graphics/apple.png")
        self.golden_apple = pygame.image.load("Art/UI_Graphics/golden_apple.png")
        self.fruit_list = [self.apple, self.golden_apple]
        self.fruit_weights = [0.95, 0.05]
        self.randomize()
    
    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.position.x * cell_size), int(self.position.y * cell_size), cell_size, cell_size)
        screen.blit(self.chosen_fruit[0], fruit_rect)
    
    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.position = Vector2(self.x, self.y)
        self.chosen_fruit = random.choices(self.fruit_list, self.fruit_weights, k=1)

class Main():
    
    def __init__(self): 
        self.fruit = Fruit()
        self.snake = Snake()
        self.score = 0        
        self.snake_speed = 150
        self.regular_snake_speed = 150  # / level to modify
        self.fast_snake_speed = (int(self.regular_snake_speed / 2)) # / level to modify
        pygame.time.set_timer(FPS, self.snake_speed) # can I optimize this?
        

    def updates(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
        pygame.time.set_timer(FPS, self.snake_speed)

    def draw_elements(self):
        screen.blit(background, (0,0))
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()

    def check_collision(self):
        #self.check_fruit()
        if self.fruit.position == self.snake.snake_body[0]:
            if self.fruit.chosen_fruit[0] == self.fruit.golden_apple:
                self.snake_speed = self.fast_snake_speed
                pygame.mixer.Channel(0).pause()
                pygame.mixer.Channel(1).unpause()
            else:
                self.snake_speed = self.regular_snake_speed
                pygame.mixer.Channel(1).pause()
                pygame.mixer.Channel(0).unpause()
            self.fruit.randomize()
            self.snake.add_block()
            self.score = (self.score + 10)

    def check_fail(self):
        #check to see if snake out of bounds
        if not 0 <= self.snake.snake_body[0].x < cell_number or not 0 <= self.snake.snake_body[0].y < cell_number:
            self.game_over()
        #check to see if snake hit tail
        for block in self.snake.snake_body[1:]:
            if block == self.snake.snake_body[0]:
                self.game_over()

    def game_over(self):
        pygame.quit()
        sys.exit()

    def draw_score(self):
        score_surface = game_font.render("Score: " + str(self.score), True, (255, 255, 255))
        score_x = int(50)
        score_y = int(50)
        score_position = score_surface.get_rect(center = (score_x, score_y))
        screen.blit(score_surface, score_position)

#Initialize Some Stuff
pygame.mixer.pre_init(44100, -16, 2, 4080)
pygame.init()
pygame.mixer.init()

#Music
"""
Load the musics as sound
Give them thier own channel and start playing them with an infinite loop
Immediately pause the fast song
"""
main_music = pygame.mixer.Sound("Art/Music/main_theme.mp3")
fast_music = pygame.mixer.Sound("Art/Music/star_theme.mp3")
pygame.mixer.Channel(0).play(main_music, -1) # The -1 is the loop, at negative -1 it's infinite
pygame.mixer.Channel(1).play(fast_music, -1)
pygame.mixer.Channel(1).pause()   

#Screen
cell_size = 40
cell_number = 20
pygame.display.set_caption("Rachel's Snake Game")
icon = pygame.image.load(("Art/snake_head_up.png"))
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size)) # Size 800x800
background = pygame.image.load("Art/UI_Graphics/background_forest.jpg")
game_font = pygame.font.Font("Art/Next_Sunday.ttf", 25)
game_state = "start_menu"

#Timing
FPS = pygame.USEREVENT

#Variables
main_game = Main()

#Colors
color_white = (255, 255, 255)
color_green = (122, 193, 122)
color_start = color_white
color_quit = color_white

while True :
    for event in pygame.event.get():  #This loops through all possible events in pygame
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == FPS:
            main_game.updates()
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

    main_game.draw_elements()
    pygame.display.update() #  Refreshes the screen


pygame.quit()
sys.exit()
