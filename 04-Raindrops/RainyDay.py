import pygame
import sys

import time
import random


class Raindrop:
    def __init__(self, screen, x, y):
        """ Creates a Raindrop sprite that travels down at a random speed. """
        # Initialize this Raindrop, as follows:
        #     - Store the screen.
        #     - Set the initial position of the Raindrop to x and y.
        #     - Set the initial speed to a random integer between 5 and 15.
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = random.randint(5,15)
        #   Use instance variables:   screen  x  y  speed.


    def move(self):
        """ Move the self.y value of the Raindrop down the screen (y increase) at the self.speed. """
        #Change the  y  position of this Raindrop by its speed.
        self.y += self.speed


    def off_screen(self):
        """ Returns true if the Raindrop y value is not shown on the screen, otherwise false. """
        # Note: this will be used for testing, but not used in the final version of the code for the sake of simplicity.
        #  Return  True  if the  y  position of this Raindrop is greater than 800.
        return self.y > self.screen.get_height()



    def draw(self):
        """ Draws this sprite onto the screen. """
        # Draw a vertical line that is 5 pixels long, 2 pixels thick,
        #      from the current position of this Raindrop (use either a black or blue color).
        pygame.draw.line(self.screen, (70, 193, 238), (self.x, self.y), (self.x, self.y+5), 2)



class Hero:
    def __init__(self, screen, x, y, with_umbrella_filename, without_umbrella_filename):
        """ Creates a Hero sprite (Mike) that does not move. If hit by rain he'll put up his umbrella. """
        # Initialize this Hero, as follows:
        #     - Store the screen.
        #     - Set the initial position of this Hero to x and y.
        #     - Create an image of this Hero WITH    an umbrella to the given with_umbrella_filename.
        #     - Create an image of this Hero WITHOUT an umbrella to the given without_umbrella_filename.
        #     - Set the "last hit time" to 0.
        #   Use instance variables:
        #      screen  x  y  image_umbrella   image_no_umbrella  last_hit_time.

        self.screen = screen
        self.x = x
        self.y = y
        self.image_umbrella = pygame.image.load(with_umbrella_filename)
        self.image_no_umbrella = pygame.image.load(without_umbrella_filename)
        self.last_hit_time = 0



    def draw(self):
        """ Draws this sprite onto the screen. """
        # Draw (blit) this Hero, at this Hero's position, WITHOUT an umbrella:
        self.screen.blit(self.image_no_umbrella, (self.x, self.y))
        #Instead draw (blit) this Hero, at this Hero's position, as follows:
        #     If the current time is greater than this Hero's last_hit_time + 1,
        #       draw this Hero WITHOUT an umbrella,
        #       otherwise draw this Hero WITH an umbrella.
        if time.time() > self.last_hit_time + 1:
            currentImage = self.image_no_umbrella
        else:
            currentImage = self.image_umbrella
        self.screen.blit(currentImage, (self.x, self.y))


    def hit_by(self, raindrop):
        """ Returns true if the given raindrop is hitting this Hero, otherwise false. """
        # Return True if this Hero is currently colliding with the given Raindrop.
        heroHitBox = pygame.Rect(self.x, self.y, 170, 172)
        return heroHitBox.collidepoint(raindrop.x, raindrop.y)



class Cloud:
    def __init__(self, screen, x, y, image_filename):
        """ Creates a Cloud sprite that will produce Raindrop objects.  The cloud will be moving around. """
        # : Initialize this Cloud, as follows:
        #     - Store the screen.
        #     - Set the initial position of this Cloud to x and y.
        #     - Set the image of this Cloud to the given image filename.
        #     - Create a list for Raindrop objects as an empty list called raindrops.
        self.screen =screen
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_filename)

        #   Use instance variables:
        #      screen  x  y  image   raindrops.
        self.raindrops = []



    def draw(self):
        """ Draws this sprite onto the screen. """
        # : Draw (blit) this Cloud's image at its current position.
        self.screen.blit(self.image, (self.x, self.y))

    def rain(self):
        """ Adds a Raindrop to the array of raindrops so that it looks like the Cloud is raining. """
        # : Append a new Raindrop to this Cloud's list of raindrops,
        #     where the new Raindrop starts at:
        #       - x is a random integer between this Cloud's x and this Cloud's x + 300.
        #       - y is this Cloud's y + 100.]
        x = random.randint(self.x, self.x+300)
        drop = Raindrop(self.screen, x, self.y+100)
        self.raindrops.append(drop)


def main():
    """ Main game loop that creates the sprite objects, controls interactions, and draw the screen. """
    #Initialize the game, display a caption, and set   screen   to a 1000x600 Screen.
    pygame.init()
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("Rainy Day")

    # Make a Clock
    clock = pygame.time.Clock()

    #  As a temporary test, make a new Raindrop called test_drop at x=320 y=10
    test_drop = Raindrop(screen, 320, 10)
    #  Make a Hero, named mike, with appropriate images, starting at position x=200 y=400.
    mike = Hero(screen, 200, 400, with_umbrella_filename="Mike_umbrella.png", without_umbrella_filename="Mike.png")
    #  Make a Hero, named alyssa, with appropriate images, starting at position x=700 y=400.
    alyssa = Hero(screen, 700, 400, with_umbrella_filename="Alyssa_umbrella.png", without_umbrella_filename="Alyssa.png")
    #  Make a Cloud, named cloud, with appropriate images, starting at position x=300 y=50.
    cloud = Cloud(screen, 300, 50, "cloud.png")

    # Enter the game loop, with a clock tick of 60 (or so) at each iteration.
    while True:
        clock.tick(60)

        #Make the pygame.QUIT event stop the game.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            #elif #continue later


        #  Inside the game loop (AFTER the events loop above), get the list of keys that are currently pressed.
        #     Arrange so that the Cloud moves:
        #       5 pixels (or 10 pixels) to the right if the Right Arrow key (pygame.K_RIGHT) is pressed.
        #       5 pixels (or 10 pixels) to the left  if the Left  Arrow key (pygame.K_LEFT)  is pressed.
        #       5 pixels (or 10 pixels) up           if the Up    Arrow key (pygame.K_UP)    is pressed.
        #       5 pixels (or 10 pixels) down         if the Down  Arrow key (pygame.K_DOWN)  is pressed.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pressedKeys = pygame.key.get_pressed()
        if pressedKeys[pygame.K_RIGHT]:
            cloud.x += 5
        if pressedKeys[pygame.K_LEFT]:
            cloud.x -= 5
        if pressedKeys[pygame.K_DOWN]:
            cloud.y += 5
        if pressedKeys[pygame.K_UP]:
            cloud.y -= 5


        # DISCUSS: If you want something to happen once per key press, put it in the events loop above
        #          If you want something to continually happen while holding the key, put it after the events loop.

        # Inside the game loop, draw the screen (fill with white)
        screen.fill((255,255,255) )

        #  Draw the Cloud.
        cloud.draw()

        # Remove the temporary testdrop code from this function and refactor it as follows:
        #  Make the Cloud "rain", then:
        cloud.rain()
        for drop in cloud.raindrops:
            drop.move()
            drop.draw()
            if mike.hit_by(drop):
                mike.last_hit_time = time.time()
                cloud.raindrops.remove(drop)
            if alyssa.hit_by(drop):
                alyssa.last_hit_time = time.time()
                cloud.raindrops.remove(drop)
            if drop.off_screen():
                cloud.raindrops.remove(drop)




        #    For each Raindrop in the Cloud's list of raindrops:
            #       - move the Raindrop.
            #       - draw the Raindrop.
            #  if the Hero (Mike or Alyssa) is hit by a Raindrop, set the Hero's last_time_hit to the current time.
            # Optional  - if the Raindrop is off the screen or hitting a Hero, remove it from the Cloud's list of raindrops.



        #  Draw the Heroes (Mike and Alyssa)
        alyssa.draw()
        mike.draw()


        #  Update the display and remove the pass statement below
        pygame.display.update()



#  Call main.

main()
