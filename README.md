# Final Project Report

* Student Name: Rachel Creemers
* Github Username: RECreemers
* Semester: Fall 2023
* Course: CS5001

## Description 
My goal was to make the Snake Game in python, specifically focusing on the menu aspects and the implimentation of the art, as well as game features. 

The features I included were:
1) A start menu with a reactive UI
2) Sound that changes based on which fruit you ate
3) A snake that goes around the screen and grows with each apple touched
4) A fruit(sometimes red, sometimes golden, it was weighted) that would randomize it's position after the snake head touched it, but not randomize on top of the snake body
5) A score counter that would go up by 10 after each apple touch
6) A snake speed change after it touched either a golden or red apple for the first time
7) A snake that had graphics on top of the bounding box rectangles created that changed based on the snake's positioning
8) All of the art

I chose this project because I wanted to learn how you think through making a game, and what all compenents have to come together in what order. I wanted this to include the art aspect, and understand how those two pipelines swirl together. To help me figure that out, I used tutorials to help me create the basic frameworks, what HAD to be there to create a barebones version of the game, and then explore why all those parts had to be in that order, where I could modify and manipulate, and where I could go to make it feel real. It was really important to me while going through this process that I wanted to learn good habits in coding games and why those were good habits. I thought it was cute when I realized I needed to create a sprite chart!

## Key Features
So the key features that I am pretty proud of is getting the UI on the Start Menu to work. It took me a very long time to figure out how I had to nest my code to get the color to change on the text for the title screen without breaking the code. But with the start menu implimented, it feels more like a "real" game to me as opposed to a code test.

I'm also proud of the idea to have 2 fruits with different colors and sounds, to mix it up. For playing, I split the randomness to 95% red, 5% golden apple, which is better for gameplay but for testing, it will be a bit annoying to have it pop up. You can change it in the __init__ of the fruit class under "fruit_weights" if it is bothering you!

## Guide
There are 2 zipped files, "Rachel's Snake Game PC" and "Rachel's Snake Game Windows". Download the zipped file for the system you are running. Unzip the file and look for "Rachel's Snake Game" as either an exe or exec depending. Double click and you should be good to go!

## Installation Instructions
In the terminal, you have to `pip install pygame` and have python downloaded from the internet to run it. 

## Code Review

The code for the game is located in file main_5.py, since exe and exec files can't be broken into.

```python
main_music = pygame.mixer.Sound("Art/Music/main_theme.mp3")
fast_music = pygame.mixer.Sound("Art/Music/star_theme.mp3")
pygame.mixer.Channel(0).play(main_music, -1) # The -1 is the loop, at negative -1 it's infinite
pygame.mixer.Channel(1).play(fast_music, -1)
pygame.mixer.Channel(1).pause()
```

This was an important block that I found had to absolutely be outside of the classes for initialization. It established the channels that the music would play on, and started the pause/unpause switch back and forth I created for the background music change. It had to be specifically paused, not stopped, or else the music would restart every time an apple was picked up, and that was really annoying.


```python
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
```

This was a huge block in the True loop which was the gameplay. Basically, it made it so that the snake could move the direction up, down, left, and right, but if you tried to move the snake in the opposite direction of where it was currently moving (moving left, try to go right) you can't. It also had that little bit at the top - game_state = "game". I used that variable to allow the gameplay to switch from the game mode with the snake, over to the menu, where the inputs caused different things to happen, such as selecting start or quit.

```python
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
```

I was quite proud of this little spot. The way this is set up, in the future I can easily add more fruits, AND I can change the score based on what type of fruit was eaten. While it's in a super vanilla version, where there are only 2 fruit options and both give a score of +10 if picked. I also thought that the sound change up based on the golden apple was hilarious. The pause/unpause bit here though, that allowed the music to pick back up where it left off, and not restart it. I'm excited to work with this section more when I create other "power up" fruits, like a banana or peach, and then I can start setting the score to different amounts based on the fruit eaten

```python
        if game_state == "menu":
            start_menu = Popups()
            start_menu.draw_title_popup()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    color_start = color_green
                    color_quit = color_white
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:  # Action is here
                    if color_start == color_green:
                        pygame.mixer.Channel(0).unpause()
                        game_state = "game"
                if event.key == pygame.K_RIGHT:
                    color_quit = color_green
                    color_start = color_white
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:  # Action is here
                    if color_quit == color_green:
                        pygame.quit()
                        sys.exit()
```

The menu! I made the text colors change when the left and right buttons were pressed, and I was able to start adding in quality of life changes to inputs, such as being able to start with either space or return. I still want to add in a click option and a hover color change. The little bit in there that has the `pygame.mixer.Channel(0).unpause()` allowed the music to unpause again when after the game restarts. Without it, it was just silent whe you started the game back up intil you touched an apple.


```python
        if self.add_snake_block == True:
            snake_body_copy = self.snake_body[:]
            snake_body_copy.insert(0,snake_body_copy[0] + self.direction)
            self.snake_body = snake_body_copy[:]
            self.add_snake_block = False
        else:
            snake_body_copy = self.snake_body[:-1]
            snake_body_copy.insert(0, snake_body_copy[0] + self.direction)
            self.snake_body = snake_body_copy[:]
```

This is the meat and potatoes of the game. This section allows the snake to move forward by copying the snake_body list to modify it, adding a new Vector2 to the front of the list and removing the last Vector2 from the list. The what changes in the Vector2 list in the list (x,y) is determined by the self.direction, which changes based on the input of the play in the left, right, up, and down, which is going to always be a +1 or -1 in either the x or y.  If the snake touches a fruit, the add_snake_block is set to True and the last Vector 2 is simply not removed from the list that time. 

A portion that I don't really have code for but wanted to touch on was the art implimentation. I had a great time exploring that portion. I was happy to find out that when creating vector files to use, they had to be the exact same cell size, and that if you made it too big it would go outside of the cell (you can see this in the main_2 video I have, the snake is litterally outside the window because it's too big!) I love how much sense it made that if I created a high res version of a vector image that was of the correct size, for me I had the 800x800 px background, but at a resolution of 300 dpi instead of 72 dpi(normal), it made it SUPER overblown and big, which honestly makes sense because the resolution is pixels per inch. So that was really cool. I wish I had been able to figure out why the sides of the snake are a little fuzzy on the straightways, and I have some theories, but there were other visuals that needed to be attended to. 


### Major Challenges
Learning pygame, I had to quickly try to learn all the funtions and methods I could call, and WHY you called things in a certain way. Other than the basics, I didn't know how they all interacted with eachother, such as why you would use Surface instead of get_rect, and what features they offered for each.

Getting the trailing squares of the snake, and have them be position references that I could then place an image over was extremely difficult and I required a lot of help on. I understood the basics of how to make the head move, and how to make it move only in certain ways, but I couldn't figure out how to get a trail that wouldn't immediatly bump into the the head and end the game based off of how I had started to learn what pygame was capable of. Using the lists, and particularaly using lists with Vector2 (once I learned about it) was the only solution I researched that would allow for that. 

Pygame was just a really steep learning curve.

## Example Runs
I typically ran the code everytime I tried to make a change. I want to set up versioning at more regular intervals in the future, becuase there were several times where I changed something that I thought was small, and it turned out it would interrupt the flow and break the game entirely. 

For the videos that I do have, they are of where I was before I started rewriting code to make it either better to understand what I was doing better.

Version 1:
https://github.com/RECreemers/Final-for-CS5001/assets/153467146/aadc87d9-7285-4747-b7e8-6ffb5db4c3a2

Version 2:
https://github.com/RECreemers/Final-for-CS5001/assets/153467146/3900c17f-1eec-453b-bf58-584c20c07dbb

Version 3:
https://github.com/RECreemers/Final-for-CS5001/assets/153467146/14bc60e1-b1f1-48f2-8074-03e4e2043e1b


## Testing
I tested my code a lot just by running it to see if anything would come up, or if the screen broke. A lot of the time I would either get a black box with a spinning wheel or just a spinning wheel that would make me exit the test. 

Sometimes, though, I couldn't understand why some of my edits weren't working, so I would include print functions to see if the variables I changed in a function were being transmitted, and if they weren't where did it stop when going back up the chain.

But when it came to see if something functioned, I would typically try to make sure the basics worked before I did anything fancy to it. Take the moving of the snake. I started with a box and tried to make it move a set incriment across the screen as just a box, no image of a snake on it. Once I had that, I tried to make multiple boxes move across the screen following the first, no jpegs on top. Once the boxes moved appropriately in one direction, I would add on top of it different directions, and see if that would work. Only after it was function without the art could I add the bells and whistles on top of it to make it pretty. 

I did a similar thing for the fruit, adding the first thing of "this is a box". Then "when box is touched by snake head, randomly rearrange". Then "when box randomizes, +10 to the score counter, etc. 

For the pictures I have included, I show screen shots of me going through the menu creation process.

Basic Testing Image:
<img width="802" alt="Pic_1 - Basic testing image" src="https://github.com/RECreemers/Final-for-CS5001/assets/153467146/337f124c-fe53-49dd-8232-0c594eb87754">

The Visual I Got Most Of The Time While Testing:
<img width="815" alt="Pic_2 - Most common visual" src="https://github.com/RECreemers/Final-for-CS5001/assets/153467146/985da92b-85bf-4067-b385-7e63d6658931">

Troubleshooting The Menu Screen:
<img width="791" alt="Pic_3 - Troubleshooting the Menu Screen" src="https://github.com/RECreemers/Final-for-CS5001/assets/153467146/36c26a4f-31f9-4554-a946-9e12bf7a4c2d">

Got Something To Pop Up On The Menu Screen:
<img width="815" alt="Pic_4 - Finally got something to pop up" src="https://github.com/RECreemers/Final-for-CS5001/assets/153467146/3320f263-9569-4213-bd55-9d9363bf6c6e">

Starting To Add Layers With Colors And Pygame Colors:
<img width="1393" alt="Pic_5 - Adding Layes and playing with colors and pygame colors" src="https://github.com/RECreemers/Final-for-CS5001/assets/153467146/8d8fa5c9-0578-46e4-a8fa-917216e0c8f2">

Menu Is Now Attractive:
<img width="1345" alt="Pic_6 - Menu is now attractive" src="https://github.com/RECreemers/Final-for-CS5001/assets/153467146/9128112b-0ddf-458d-bc4f-74fdf383b30a">


## Missing Features / What's Next
I didn't get to a lot of things:
    1) Levels
    2) Game Over Screen - would list score, and ask if you wanted to restart with the lightup text
    3) A Saved Highscore
    4) A clickable Sound Button to make the music stop
    5) Fixing a bug where if you type the keys too quickly, the snake dies
    6) Changing when the snake resets into a little later in the code so that you don't get the visual hiccup
    7) Make the menu text also clickable, with a color change when the cursor moved over it
    8) Changable Backgrounds and skins

Levels and Gameover Screen: I could not figure out how to manipulate the menu. I tried a bunch to just keep things in the same menu function and just change the text that was set on top of it, but whenever I tried to create more logic branches I kept breaking flow or it wouldn't trigger. I am going to keep playing with it and see if I can fix that, because I really thought it would make it feel/look more like a "real game"

Saved Highscore - I had the idea to have the code check a separate document with "highscore = xxxx" on it, (xxxx being some numbers), and if the number was higher than the one on the separate txt file, then it would update the txt file with the new number and then display that number on screen whenever the highscore would pop up at the game_over screen.

Sound button: I got a bit sick of the music as I continually tested it to see if it would work, and I would have loved to be able to click a corner sound icon, have the icon switch to one with a strike through it, and mute the sound

Bug Fix: I kept trying to look up how to limit the timelength for when the code would accept new keydown input, but I couldn't understand how to impliment it. I know this exists, I just haven't grasped it yet.

Snake Reset Visual Hiccup: I know WHY this is happening (I push the snake back into the original place BEFORE the menu screen refreshes), but when I tried to move the resetting of the snake to a later point in the code, it kept breaking the flow.

Clickable Buttons: I found a tutorial for buttons, followed it, wrote out the code, but in the end I couldn't impliment it in time with everything.

Changable Background: This was a stretch goal if I got all those other things done above.

## Final Reflection
I learned an absolute boatload in this course. I'm still a bit shakey on understanding classes and writing files from the script, but I'm happy that while I'm working through the logic and reading code, I'm starting to ACTUALLY read it as opposed to just recognizing the pictures and what they mean, ie, when I see == I don't think to myself "Oh, double equals" anymore, I think "is", which is EXTREMELY helpful.

I'm pretty happy that I've also learned how to debug a bunch of things. The print("DEBUG") thing helped me for many of my homeworks and helped quite a bit in my snake game to help me figure how what was changing when, and why. Being able to read the ValueErrors and the debug screen was also huge for me, and saved me a lot of time when I couldn't figure out what I had changed mid final. 

I want to explore more about the UX UI features provided by pygame, and how to deal with the flow of control in the main True loop because I feel like I only scratched the surface of what that area is capable of. From the research I did, the music capabilites of pygame are fine, but there isn't a lot of fine control there as I think you can only have like 6 or 8 different music channels, so if I wanted to create a game with more intricate sounds coming in, as opposed to the hammer/nail job I implimented in this one, I'll either need to dig deeper to find more libraries that deal with that or just a differnt coding language. 

My key takeaways is that I need to drill the basics more in general if I want to be creative with programming, and I'm confident that the next semester and summer will provide that for me. It also became very clear to me how I'm playing with a very small toolbox in python right now, and am excited to see what other things the program will allow me to do in the future. Lastly, I'm happy to be able to start to read and sift through code so I can learn some other programming languages in a bit. 

