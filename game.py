"""
Okay, so this is not a 'serious' project. I just did a little coding when I was bored in the bathroom. Anyway I decided to add this to my github because maybe I'll come back to this later.
So please don't judge me. This obviously a joke. Although it works quite well, except for the jumping. I should've add the delta time and other stuff.
Enjoy!
"""

import pygame as py
from engine import Player

py.init()

size  = (640, 480)
screen = py.display.set_mode(size)

x = 50
y = 30
velocity = 4
jumpValue = 12

playerSize = (80, 110)

background = py.image.load('graphics/bg.png')
character = Player(50, 30, 80, 110, 'graphics/character.png')

deltaTime = 0

def rendering():
    screen.blit(background, (0, 0))
    character.draw(screen)
    py.display.flip()
    py.display.update()

def main():
    oldtime = 0
    global x, y, velocity, jumpValue, deltaTime
    oldtime = deltaTime
    hasGround = False
    py.display.set_caption('Game 2D made because of my very boring life!')
    close = False
    clock = py.time.Clock()
    clock.tick(60)
   
    while not close: 
        for event in py.event.get():
            if event.type == py.QUIT:
                close = True

        KEYS = py.key.get_pressed()
        
        character.applyGravity()

        #simple collision checking & ground checking
        if character.x >= (size[0] - character.size[0]):
            character.x = size[0] - character.size[0]
        elif character.x <= 0:
            character.x = 0
        if character.y <= 0:
            character.y = 0
        elif character.y >= (size[1] - character.size[1]):
            character.y = size[1] - character.size[1]
            character.hasGround = True
        else:
            character.hasGround = False
        
        #movement
        if KEYS[py.K_w] and character.hasGround:
            character.y -= (character.jumpValue ** 2) * 0.5 

        if KEYS[py.K_a]:
            character.x -= character.velocity

        if KEYS[py.K_d]:
            character.x += character.velocity

        rendering()
    
    py.quit()

main()