import pygame
import random
import time
import sys
from pygame.math import Vector2
from pygame import mixer


# This is where the game runs
class Snake():
    """
    Makes snake bounding box
    Determines how snake moves - modifiying list through Vector2
    Adds all snake images needed
    Creates way for blocks to be added to snake
    """
    def __init__(self):
        # Put all the snake basics in here
        # Starts with 3 body pieces
        self.snake_body = [Vector2(4, 10), Vector2(3, 10), Vector2(2, 10)]
        self.direction = Vector2(1, 0)  # Start going to the right
        self.add_snake_block = False
        self.snake_alive = True

        # All the snake body images
        self.head_down = pygame.image.load(
            "Art/Player_Graphics/snake_head_down.png").convert_alpha()
        self.head_up = pygame.image.load(
            "Art/Player_Graphics/snake_head_up.png").convert_alpha()
        self.head_right = pygame.image.load(
            "Art/Player_Graphics/snake_head_right.png").convert_alpha()
        self.head_left = pygame.image.load(
            "Art/Player_Graphics/snake_head_left.png").convert_alpha()

        self.butt_down = pygame.image.load(
            "Art/Player_Graphics/snake_butt_down.png").convert_alpha()
        self.butt_up = pygame.image.load(
            "Art/Player_Graphics/snake_butt_up.png").convert_alpha()
        self.butt_right = pygame.image.load(
            "Art/Player_Graphics/snake_butt_right.png").convert_alpha()
        self.butt_left = pygame.image.load(
            "Art/Player_Graphics/snake_butt_left.png").convert_alpha()

        self.mid_horizontal = pygame.image.load(
            "Art/Player_Graphics/snake_mid_horizontal.png").convert_alpha()
        self.mid_vertical = pygame.image.load(
            "Art/Player_Graphics/snake_mid_vertical.png").convert_alpha()

        self.turn_down_left = pygame.image.load(
            "Art/Player_Graphics/snake_turn_down_left.png").convert_alpha()
        self.turn_down_right = pygame.image.load(
            "Art/Player_Graphics/snake_turn_down_right.png").convert_alpha()
        self.turn_up_left = pygame.image.load(
            "Art/Player_Graphics/snake_turn_up_left.png").convert_alpha()
        self.turn_up_right = pygame.image.load(
            "Art/Player_Graphics/snake_turn_up_right.png").convert_alpha()

    def draw_snake(self):
        """
        This section allows the snake to be drawn onscreen,
        and creates the conditions for what image is displayed depending
        on where the snake boxes are in relation to eachother.
        """
        self.update_head_graphics()
        self.update_butt_graphics()

        for index, block in enumerate(self.snake_body):
            snake_rect = pygame.Rect(
                int(block.x * cell_size),
                int(block.y * cell_size),
                cell_size, cell_size)

            if index == 0:
                screen.blit(self.head, snake_rect)
            elif index == len(self.snake_body) - 1:
                screen.blit(self.butt, snake_rect)
            else:
                previous_block = self.snake_body[index + 1] - block
                next_block = self.snake_body[index - 1] - block
                # This is the straight up/down/left/right section of drawing
                if (previous_block.y == -1 and next_block.y == 1 or
                        previous_block.y == 1 and next_block.y == -1):
                    screen.blit(self.mid_vertical, snake_rect)
                elif (previous_block.x == -1 and next_block.x == 1 or
                        previous_block.x == 1 and next_block.x == -1):
                    screen.blit(self.mid_horizontal, snake_rect)
                # This is the turning section of drawing
                elif (previous_block.x == -1 and next_block.y == -1 or
                        previous_block.y == -1 and next_block.x == -1):
                    screen.blit(self.turn_down_left, snake_rect)
                elif (previous_block.x == 1 and next_block.y == 1 or
                        previous_block.y == 1 and next_block.x == 1):
                    screen.blit(self.turn_up_right, snake_rect)
                elif (previous_block.x == 1 and next_block.y == -1 or
                        previous_block.y == -1 and next_block.x == 1):
                    screen.blit(self.turn_down_right, snake_rect)
                elif (previous_block.x == -1 and next_block.y == 1 or
                        previous_block.y == 1 and next_block.x == -1):
                    screen.blit(self.turn_up_left, snake_rect)

    def move_snake(self):
        """
        This section allows the snake to move forward by copying
        the snake_body list to modify it, adding a new Vector2
        to the list, and removing the last Vector2 from the list.
        If the snake touches a fruit, the add_snake_bock is set
        to True and the last Vector 2 is simply not removed
        from the list that time.
        """
        if self.add_snake_block:
            snake_body_copy = self.snake_body[:]
            snake_body_copy.insert(0, snake_body_copy[0] + self.direction)
            self.snake_body = snake_body_copy[:]
            self.add_snake_block = False
        else:
            snake_body_copy = self.snake_body[:-1]
            snake_body_copy.insert(0, snake_body_copy[0] + self.direction)
            self.snake_body = snake_body_copy[:]

    def add_block(self):
        """
        sets add_snake_block to True so that move_snake knows
        it's got to add a block
        """
        self.add_snake_block = True

    def update_head_graphics(self):
        """
        This is where the first Vector2 in the list of the snake_body checks
        to see what direction is is facing and thusly, which snake_head image
        should be on screen. It does this by looking at the first block and
        subracts the second block vectors from it. Since everything has been
        made in chuncks it allows for the clean number check of -1 or +1 in
        either the x or y of the Vector2 list.
        """
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
        """
        This is where the last Vector2 in the list of the snake_body
        checks to see what direction itis facing and thusly, which
        snake_head image should be on screen. It does this by looking at the
        second to last block, and the subracting from it the last block.
        """
        butt_relation = self.snake_body[-2] - self.snake_body[-1]
        if butt_relation.x == 1:
            self.butt = self.butt_right
        elif butt_relation.x == -1:
            self.butt = self.butt_left
        elif butt_relation.y == 1:
            self.butt = self.butt_down
        elif butt_relation.y == -1:
            self.butt = self.butt_up

    def reset_snake(self):
        """
        This allows the snake to restart at the same place with
        the same size list as the beginning
        """
        self.snake_body = [Vector2(4, 10), Vector2(3, 10), Vector2(2, 10)]
        self.direction = Vector2(1, 0)


class Fruit():
    """
    Makes bounding box for fruit
    Puts fruit image on screen
    When collided with, randomize fruit placement
    and fruit type based on weight
    """
    def __init__(self):
        self.apple = pygame.image.load(
            "Art/UI_Graphics/apple.png")
        self.golden_apple = pygame.image.load(
            "Art/UI_Graphics/golden_apple.png")
        self.fruit_list = [self.apple, self.golden_apple]
        self.fruit_weights = [0.95, 0.05]
        self.randomize()

    def draw_fruit(self):
        """
        sets the bounding box for the fruit and then draws it on the screen
        """
        fruit_rect = pygame.Rect(
            int(self.position.x * cell_size),
            int(self.position.y * cell_size),
            cell_size, cell_size)
        screen.blit(self.chosen_fruit[0], fruit_rect)

    def randomize(self):
        """
        takes a random x,y coordinate on the screen and moves
        the fruit to that spot. It also selects a fruit randomly,
        either the golden or red apple
        """
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.position = Vector2(self.x, self.y)
        self.chosen_fruit = random.choices(
            self.fruit_list, self.fruit_weights, k=1)


class Main():
    """
    This is where the looping part of the program runs,
    the part that has to be executed every time the
    screen refreshes and the logic behind the game.
    """
    def __init__(self):
        self.fruit = Fruit()
        self.snake = Snake()
        self.score = 0
        self.snake_speed = 150
        self.regular_snake_speed = 150
        self.fast_snake_speed = (int(self.regular_snake_speed / 2))
        pygame.time.set_timer(FPS, self.snake_speed)

    def updates(self):
        """
        The basic update area, checking to see where the snake moves,
        if it got a fruit, or if you died, as well as keeping the timer
        going for the music.
        """
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
        pygame.time.set_timer(FPS, self.snake_speed)

    def draw_elements(self):
        """
        Because the snake moves every second of the game,
        the draw elements need to be continually updated/refreshed.
        """
        screen.blit(background, (0, 0))
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()

    def check_collision(self):
        """
        This portion checks if the snake touched the apple
        (depending on which one) the music changes, the apple
        and it's position are randomized, the snake gets a block,
        and the score is increased
        """
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

        for block in self.snake.snake_body[1:]:
            if block == self.fruit.position:
                self.fruit.randomize()

    def check_fail(self):
        """
        setting ways for the game to end,
        such as snake touches tail or snake tries to go outside
        the screen
        """
        # check to see if snake out of bounds
        if (not 0 <= self.snake.snake_body[0].x < cell_number or
                not 0 <= self.snake.snake_body[0].y < cell_number):
            self.snake.snake_alive = False
            self.game_over()
        # check to see if snake hit tail
        for block in self.snake.snake_body[1:]:
            if block == self.snake.snake_body[0]:
                self.snake.snake_alive = False
                self.game_over()

    def draw_score(self):
        """
        The score needs to be reactive, so the numbers and letters
        have to be drawn on screen with pygame as opposed to using a jpg.
        """
        score_surface = game_font.render(
            "Score: " + str(self.score), True, (255, 255, 255))
        score_x = int(100)
        score_y = int(50)
        score_position = score_surface.get_rect(
            center=(score_x, score_y))
        screen.blit(score_surface, score_position)

    def game_over(self):
        """
        Moves to game over screen
        """
        global game_state
        game_state = "menu"
        pygame.mixer.Channel(0).pause()
        pygame.mixer.Channel(1).pause()
        self.snake.reset_snake()


class Popups():
    """
    Draws on title of Snake Game
    """
    def __init__(self) -> None:
        self.snake = Snake()
        self.main = Main()
        self.font_big = pygame.font.Font(
            "Art/Next_Sunday.ttf", 80)
        self.font_small = pygame.font.Font(
            "Art/Next_Sunday.ttf", 60)
        self.title = self.font_big.render(
            "Snake Game", True, (255, 255, 255))
        self.start_button = self.font_small.render(
            "Start", True, (color_start))
        self.quit_button = self.font_small.render(
            "Quit", True, (color_quit))
        self.restart_button = self.font_small.render(
            "Restart", True, (color_restart))

    def draw_title_popup(self):
        title_square = 600
        screen_center = 400
        # Rectangle
        title_rect = pygame.Surface((title_square, title_square))
        title_rect.fill((78, 61, 66))
        # Setting Positions
        pos_title_rect = title_rect.get_rect(
            center=(screen_center, screen_center))
        pos_title = self.title.get_rect(
            center=(screen_center, (screen_center / 1.25)))
        pos_start_button = self.start_button.get_rect(
            center=(((screen_center) / 1.5),
                    (screen_center + 75)))
        pos_quit_button = self.quit_button.get_rect(
            center=((screen_center + ((screen_center) / 2.75)),
                    (screen_center + 75)))
        screen.fill((122, 193, 122))
        # Write on Text
        if self.snake.snake_alive:  # If this is the first round through
            screen.blit(title_rect, pos_title_rect)
            screen.blit(self.title, pos_title)
            screen.blit(self.start_button, pos_start_button)
            screen.blit(self.quit_button, pos_quit_button)


# Initialize Some Stuff
pygame.mixer.pre_init(44100, -16, 2, 4080)
pygame.init()
pygame.mixer.init()

# Music
"""
Load the musics as sound
Give them thier own channel and start playing them with an infinite loop
Immediately pause the fast song
"""
main_music = pygame.mixer.Sound("Art/Music/main_theme.mp3")
fast_music = pygame.mixer.Sound("Art/Music/star_theme.mp3")
# The -1 is the loop, at negative -1 it's infinite
pygame.mixer.Channel(0).play(main_music, -1)
pygame.mixer.Channel(1).play(fast_music, -1)
pygame.mixer.Channel(1).pause()


# Screen
cell_size = 40
cell_number = 20
pygame.display.set_caption("Rachel's Snake Game")
icon = pygame.image.load(("Art/snake_head_up.png"))
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((cell_number
                                  * cell_size,
                                  cell_number
                                  * cell_size))  # Size 800x800
background = pygame.image.load("Art/UI_Graphics/background_forest.jpg")
game_font = pygame.font.Font("Art/Next_Sunday.ttf", 25)
game_state = "menu"

# Timing
FPS = pygame.USEREVENT

# Variables
main_game = Main()

# Colors
color_white = (255, 255, 255)
color_green = (122, 193, 122)
color_start = color_white
color_quit = color_white
color_restart = color_white

while True:
    # This loops through all possible events in pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if game_state == "menu":
            start_menu = Popups()
            start_menu.draw_title_popup()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    color_start = color_green
                    color_quit = color_white
                if event.key == pygame.K_SPACE \
                   or event.key == pygame.K_RETURN:  # Action is here
                    if color_start == color_green:
                        pygame.mixer.Channel(0).unpause()
                        game_state = "game"
                if event.key == pygame.K_RIGHT:
                    color_quit = color_green
                    color_start = color_white
                if event.key == pygame.K_SPACE \
                   or event.key == pygame.K_RETURN:  # Action is here
                    if color_quit == color_green:
                        pygame.quit()
                        sys.exit()

        if game_state == "game":
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
    pygame.display.update()  # Refreshes the screen
