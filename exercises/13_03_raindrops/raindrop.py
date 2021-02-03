"""
13-3. Raindrops
Find an image of a raindrop and create a grid of raindrops.
Make the raindrops fall toward the bottom of the screen until they
disappear.
"""
import sys
from random import randint
import pygame
from pygame.sprite import Sprite

class Settings:
    """A class to store all settings."""

    def __init__(self):
        """Initialize the settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (10, 10, 30)

        # Raindrop settings
        self.drop_speed = 1


class ImageObject(Sprite):
    """A class to represent a single object."""

    def __init__(self, main_program):
        """Initialize the alen and set its starting position."""
        super().__init__()
        self.screen = main_program.screen
        self.settings = main_program.settings

        # Load the image and set its rect attribute.
        self.image = pygame.image.load('raindrop.bmp')
        self.rect = self.image.get_rect()

        # Start each new alen near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """Move the object."""
        lucky_number = randint(0, 800)
        while True:
            number = randint(0, 800)
            if number == lucky_number:
                self.y += self.settings.drop_speed
                self.rect.y += self.y
                break


class MainProgram:
    """Overall class to manage assets and behaviour."""

    def __init__(self):
        """Initialize the program, and create resources."""
        pygame.init()
        self.settings = Settings()

        # Create a display window and assign to self.screen
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("13-3 Raindrops")

        self.images = pygame.sprite.Group()

        self._create_image_grid()

    def run_program(self):
        """Start the main loop for the program."""
        while True:
            self._check_events()
            self._update_images()

            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and
                    event.key == pygame.K_q):
                sys.exit()

    def _create_image_grid(self):
        """Create a grid of image objects."""
        # Create an image and find the number of images in a row.
        # Spacing between each image is equal to one image width.
        image = ImageObject(self)
        image_width, image_height = image.rect.size
        available_space_x = self.settings.screen_width - image_width
        number_images_x = available_space_x // (2 * image_width)

        # Determine the number of rows of aliens that fit on the screen.
        available_space_y = (
            self.settings.screen_height - (3 * image_height))
        number_rows = (available_space_y // (2 * image_height)) + 2

        # Create the fleet of aliens.
        for row_number in range(number_rows):
            for image_number in range(number_images_x):
                self._create_image(image_number, row_number)

    def _create_image(self, image_number, row_number):
        """Create an image and place it in the row."""
        image = ImageObject(self)
        image_width, image_height = image.rect.size
        image.x = image_width + 2 * image_width * image_number
        image.rect.x = image.x
        image.rect.y = image.rect.height + 2 * image.rect.height * row_number
        self.images.add(image)

    def _update_images(self):
        """update the positions of all images in the grid."""
        self.images.update()


    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.images.draw(self.screen)

        pygame.display.flip()


if __name__ == "__main__":
    # Make a game instance, and run the game.
    mp = MainProgram()
    mp.run_program()
