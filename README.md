# Final Project Report

* Student Name: Rachel Creemers
* Github Username: Rachel Creemers
* Semester: Fall 2023
* Course: CS5001

## Description 
General overview of the project, what you did, why you did it, etc. 

My goal was to make the Snake Game in python. 
The features I included were:
    1) A start menu with a reactive UI
    2) Sound that changes based on which fruit you ate
    3) A snake that goes around the screen and grows with each apple touched
    4) A fruit(sometimes red, sometimes golden, it was weighted) that would randomize it's position after the snake head touched it, but not randomize on top of the snake body
    5) A score counter that would go up by 10 after each apple touch
    6) A snake speed change after it touched either a golden or red apple for the first time
    7) A snake that had graphics on top of the boundingbox rectangles created that changed based on the snake's positioning

    I chose this game because I've been wanting to learn how to code a game for a while, and this seemed like a good way to dip my feet into it. I also wanted to go with the snake game build style that would make it so you could include artwork for the sprite, because user experience is important for me to figure out if I want to make an enjoyable game in the future.  


## Key Features
    So the key features that I am pretty proud of is getting the UI on the Start Menu to work. It took me a very long time to figure out how I had to nest my code to get the color to change on the text for the title screen without breaking the code. But with the start menu implimented, it feels more like a "real" game to me as opposed to a code test.

    I'm also proud of the idea to have 2 fruits with different colors and sounds, to mix it up. For playing, I split the randomness to 95% red, 5% golden apple, which is better for gameplay but for testing, it will be a bit annoying to have it pop up. You can change it in the __init__ of the fruit class under "fruit_weights" if it is bothering you!

## Guide
How do we run your project? What should we do to see it in action? - Note this isn't installing, this is actual use of the project.. If it is a website, you can point towards the gui, use screenshots, etc talking about features. 

There will be 2 zipped files, "Rachel's Snake Game PC" and "Rachel's Snake Game Windows". Download the zipped file for the system you are running. Unzip the file and look for "Rachel's Snake Game" as either an exe or exec dependind. Double click and you should be good to go!

## Installation Instructions
If we wanted to run this project locally, what would we need to do?  If we need to get API key's include that information, and also command line startup commands to execute the project. If you have a lot of dependencies, you can also include a requirements.txt file, but make sure to include that we need to run `pip install -r requirements.txt` or something similar.

In the terminal, you have to `pip install pygame` and have python downloaded from the internet to run it. 

## Code Review
Go over key aspects of code in this section. Both link to the file, include snippets in this report (make sure to use the [coding blocks](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#code)).  Grading wise, we are looking for that you understand your code and what you did. 

Okay, so there are a lot of "Key Aspects" to this code, and for each function in each class I have documentation at the top to let you know what is happening at each point.

I guess the part where the most action occurs is at

### Major Challenges
Learning pygame, I had to quickly try to learn all the funtions and methods I could call, and WHY you called things in a certain way. Other than the basics, I didn't know how they all interacted with eachother, such as why you would use Surface instead of get_rect, and what features they offered for each.

Getting the trailing squares of the snake, and have them be position references that I could then place an image over was extremely difficult and I required a lot of help on. I understood the basics of how to make the head move, and how to make it move only in certain ways, but I couldn't figure out how to get a trail that wouldn't immediatly bump into the the head and end the game based off of how I had started to learn what pygame was capable of. Using the lists, and particularaly using lists with Vector2 (once I learned about it) was the only solution I researched that would allow for that. 

Pygame was just a really steep learning curve.

## Example Runs
Explain how you documented running the project, and what we need to look for in your repository (text output from the project, small videos, links to videos on youtube of you running it, etc)

So I didn't see this until I started working on the UI, so I have some pictures of that, and I have the code to show you where I stopped and started rewriting it each time. I basically got to "pygames opens and closes, and a box moves across the screen" on main_1 before I hopped over to a tutorial because I could tell my filing wasn't going to be nearly neat enough to pull off what I wanted. I then followed along with the tutorial for main_2, and then tried to rewrite main_2 from memory in main_3 and worked through (partially) a logic sudocode to really make sure I was understanding the math and WHY everything was happening when it was. After I had a cute working snake game with sound in main_3, I moved onto main_4 where the final is, and where I tried adding the features that made a game playable for the average user (menus). 

## Testing
I tested my code a lot just by running it to see if anything would come up, or if the screen broke. A lot of the time I would either get a black box with a spinning wheel or just a spinning wheel that would make me exit the test. 

Sometimes, though, I couldn't understand why some of my edits weren't working, so I would include print functions to see if the variables I changed in a function were being transmitted, and if they weren't where did it stop when going back up the chain.

But when it came to see if something functioned, I would typically try to make sure the basics worked before I did anything fancy to it. Take the moving of the snake. I started with a box and tried to make it move a set incriment across the screen as just a box, no image of a snake on it. Once I had that, I tried to make multiple boxes move across the screen following the first, no jpegs on top. Once the boxes moved appropriately in one direction, I would add on top of it different directions, and see if that would work. Only after it was function without the art could I add the bells and whistles on top of it to make it pretty. 

I did a similar thing for the fruit, adding the first thing of "this is a box". Then "when box is touched by snake head, randomly rearrange". Then "when box randomizes, +10 to the score counter, etc. 

> _Make it easy for us to know you *ran the project* and *tested the project* before you submitted this report!_


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
Write at least a paragraph about your experience in this course. What did you learn? What do you need to do to learn more? Key takeaways? etc.

I learned an absolute boatload in this course. I'm still a bit shakey on understanding classes and writing files from the script, but I'm happy that while I'm working through the logic and reading code, I'm starting to ACTUALLY read it as opposed to just recognizing the pictures and what they mean, ie, when I see == I don't think to myself "Oh, double equals" anymore, I think "is", which is EXTREMELY helpful.

I'm pretty happy that I've also learned how to debug a bunch of things. The print("DEBUG") thing helped me for many of my homeworks and helped quite a bit in my snake game to help me figure how what was changing when, and why. Being able to read the ValueErrors and the debug screen was also huge for me, and saved me a lot of time when I couldn't figure out what I had changed mid final. 

I think I need to drill down more on organization of the files and breaking things down. I was frusterated for multiple hours in making my game because I kept accidentally breaking flow and I couldn't figure out why, and it actively stopped me from adding in a few featurs I really wanted to complete. And if I want to keep building cute things, I NEED to be able to keep the pipeline organized. It would also be extremely useful to find out more ways you SHOULD NOT impliment certain code to make it work.

My key takeaways is that I need to drill the basics more in general if I want to be creative with programming, and I'm confident that the next semester and summer will provide that for me. It also became very clear to me how I'm playing with a very small toolbox in python right now, and am excited to see what other things the program will allow me to do in the future. Lastly, I'm happy to be able to start to read and sift through code so I can learn some other programming languages, as I've had my eye on Godot for the last few months.

