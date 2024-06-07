import pygame
import sys
import random


# You will implement this module ENTIRELY ON YOUR OWN!

# TODO: Create a Ball class.
class Ball:
    def __init__(self, screen):
        self.screen = screen
        self.x = random.randint(0, screen.get_width())
        self.y = random.randint(0, screen.get_height())
        self.rad = random.randint(10, 35)
        self.speed_x = random.randint(-3, 3)
        self.speed_y = random.randint(-3, 3)
        self.r = random.randint(0, 255)
        self.g = random.randint(0, 255)
        self.b = random.randint(0, 255)


    def draw(self):
        pygame.draw.circle(self.screen, (self.r, self.g, self.b), (self.x, self.y), self.rad, 2)


    def OffScreen(self):
        if self.y > self.screen.get_height() or self.y < 0:
            return 1
        elif self.x > self.screen.get_width() or self.x < 0:
            return 2
        else:
            return 0


    def move(self):
        self.y += self.speed_y
        self.x += self.speed_x
        if self.OffScreen() == 1:
            self.speed_y = -self.speed_y
        elif self.OffScreen() == 2:
            self.speed_x = -self.speed_x
        else:
            self.speed_x = self.speed_x
            self.speed_y = self.speed_y






# : Possible member variables: screen, color, x, y, radius, speed_x, speed_y
# : Methods: __init__, draw, move


def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption('Bouncing Ball')
    screen.fill(pygame.Color('gray'))
    clock = pygame.time.Clock()
    ball = Ball(screen)







    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


        clock.tick(60)
        screen.fill(pygame.Color('gray'))

        ballList = []
        for i in range(100):
            ballList.append(Ball(screen))

        for ball in ballList:
            ball.draw()
            ball.move()




        pygame.display.update()


main()


# Optional challenges (if you finish and want do play a bit more):
#   After you get 1 ball working make a few balls (ball2, ball3, etc) that start in different places.
#   Make each ball a different color
#   Make the screen 1000 x 800 to allow your balls more space (what needs to change?)
#   Make the speed of each ball randomly chosen (1 to 5)
#   After you get that working try making a list of balls to have 100 balls (use a loop)!
#   Use random colors for each ball
