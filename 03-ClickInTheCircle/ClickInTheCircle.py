import pygame, sys
import math


def distance(point1, point2):
    point1_x = point1[0]
    point2_x = point2[0]
    point1_y = point1[1]
    point2_y = point2[1]

    deltaX = point2_x - point1_x
    deltaY = point2_y - point1_y

    dist = math.sqrt(deltaX ** 2 + deltaY ** 2)

    return dist

    # TODO 4: Return the actual distance between point 1 and point 2.
    #  Hint: you will need the math library for the sqrt function.
    #       distance = sqrt(   (delta x) ** 2 + (delta y) ** 2  )



def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption("Mouse click positions")
    font = pygame.font.Font(None, 25)


    # TODO 8: Load the "drums.wav" file into the pygame music mixer
    pygame.mixer_music.load("drums.wav")

    instruction_text = 'Click in the circle'
    text_color = (222, 222, 0)
    instructions_image = font.render(instruction_text, True, text_color)


    circle_color = (154, 58, 212)
    circle_center = (screen.get_width() // 2, screen.get_height() // 2)
    circle_radius = 50
    circle_border_width = 3

    message_text = ''



    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                clickPos = event.pos

                if distance(circle_center, clickPos) <= circle_radius:
                    message_text = "Bullseye!"
                    pygame.mixer.music.play(-1)

                else:
                    message_text = "You missed!"
                    pygame.mixer.music.stop()

            # Done: For a MOUSEBUTTONDOWN event get the click position.
                # Done: Determine the distance between the click position and the circle_center using the distance
                # Done:   function and save the result into a variable called distance_from_circle
                # Done: If distance_from_circle is less than or equal to circle_radius, set message_text to 'Bullseye!'
                # If distance_from_circle is greater than the circle_radius, set the message_text to 'You missed!'
                # TODO 9: Start playing the music mixer looping forever if the click is within the circle

                # TODO 10: Stop playing the music if the click is outside the circle

        screen.fill(pygame.Color("Black"))

        # TODO 1: Draw the circle using the screen, circle_color, circle_center, circle_radius, and circle_border_width
        pygame.draw.circle(screen, circle_color, circle_center, circle_radius, circle_border_width)

        # TODO 6: Create a text image (render the text) based on the message_text with the color (122, 237, 201)
        text = font.render(message_text, True, (122, 237, 201))
        screen.blit(text, (25, 200) )

        screen.blit(instructions_image, (25, 25))

        # TODO 7: Draw (blit) the message to the user that says 'Bullseye!' or 'You missed!'

        pygame.display.update()




main()
