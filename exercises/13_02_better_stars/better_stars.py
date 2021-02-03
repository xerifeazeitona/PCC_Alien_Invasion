"""
13-2. Better Stars
You can make a more realistic star pattern by introducing randomness
when you place each star.
Recall that you can get a random number like this:
    from random import randint
    random_number = randint(-10, 10)
This code returns a random integer between −10 and 10.

Using your code in Exercise 13-1, adjust each star’s position by a
random amount.
"""
import sys
from random import randint
import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """A class to represent a single star."""

    def __init__(self, screen):
        """Initialize the star and set its starting position."""
        super().__init__()
        self.screen = screen

        # Load the star image and set its rect attribute.
        self.image = pygame.image.load('star.bmp')
        self.rect = self.image.get_rect()

        # Create each new star near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the star's exact horizontal position.
        self.x = float(self.rect.x)

# Initialize attributes
pygame.init()
bg_color = (10, 10, 20)
screen_width = 1375
screen_height = 750
surface = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("13-2 - Better Stars")
surface.fill(bg_color)
stars = pygame.sprite.Group()

# Create a star and find the number of stars in a row.
# Spacing between each star is equal to one star width.
star = Star(surface)
star_width, star_height = star.rect.size
available_space_x = screen_width - (2 * star_width)
number_stars_x = (available_space_x // (2 * star_width)) + 1

# Determine the number of rows of stars that fit on the screen.
available_space_y = (screen_height - (2 * star_height))
number_rows = (available_space_y // (2 * star_height)) + 1

# Create the fleet of stars.
for row_number in range(number_rows):
    for star_number in range(number_stars_x):
        star = Star(surface)
        star_width, star_height = star.rect.size
        star.x = star_width + 2 * star_width * star_number
        star.rect.x = star.x + randint(-15, 15)
        star.rect.y = (
            (star.rect.height + 2 * star.rect.height * row_number) +
            randint(-15, 15))
        stars.add(star)


while True:
    #Respond to keypresses and mouse events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and
                event.key == pygame.K_q):
            sys.exit()

    stars.draw(surface)

    pygame.display.flip()
    