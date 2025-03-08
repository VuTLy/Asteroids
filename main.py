# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

def main():

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #initalizing game screen
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #building FPS
    clock = pygame.time.Clock()
    dt = 0

    #set variable
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    #Creating Group of class to be update
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    #Create container then create PLAYER object
    Player.containers = (updateable, drawable)
    player = Player(x, y)

    #game loop
    while(True):
        #limit frame rate to 60fps
        dt = clock.tick(60) / 1000

        # Handle events (e.g., quitting the game)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
        
        #calls update on group
        updateable.update(dt)



        # Clear the screen, render stuff, etc.
        screen.fill((0,0,0))
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        


if __name__ == "__main__":
    main()