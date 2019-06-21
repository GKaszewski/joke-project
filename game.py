"""
Okay, so this is not a 'serious' project. I just did a little coding when I was bored in the bathroom. Anyway I decided to add this to my github because maybe I'll come back to this later.
So please don't judge me. This obviously a joke. Although it works quite well, except for the jumping. I should've add the delta time and other stuff.
Enjoy!
"""

import pygame as py

py.init()

x = 50
y = 30
velocity = 4
jumpValue = 12

deltaTime = 0

def main():
    oldtime = 0
    global x, y, velocity, jumpValue, deltaTime
    oldtime = deltaTime
    hasGround = False
    size  = (800, 600)
    screen = py.display.set_mode(size)
    py.display.set_caption('Game 2D made because of my very boring life!')
    close = False
    clock = py.time.Clock()
    while not close: 
        for event in py.event.get():
            if event.type == py.QUIT:
                close = True

        KEYS = py.key.get_pressed()

        #gravity
        y+= 10

        #simple collision checking & ground checking
        if x >= (size[0] - 40):
            x = size[0] - 40
        elif x <= 0:
            x = 0
        if y <= 0:
            y = 0
        elif y >= (size[1] - 80):
            y = size[1] - 80
            hasGround = True
        else:
            hasGround = False
        
        #movement
        if KEYS[py.K_w] and hasGround:
            y-= (jumpValue ** 2) * 0.5 

        if KEYS[py.K_a]:
            x-= velocity

        if KEYS[py.K_d]:
            x+= velocity

        screen.fill((255,255,255))
        py.draw.rect(screen, (100, 0, 0), (x, y, 40, 80))
        py.display.flip()
        clock.tick(60)
        py.display.update()
    
    py.quit()

main()