"""
This class will control all rocket related stuff
"""
import pygame

class Rocket:
    """A class to manage the rocket."""

    def __init__(self, sr_game):
        """Initialize the ship and set its starting position."""
        self.screen = sr_game.screen
        self.settings = sr_game.settings
        self.screen_rect = sr_game.screen.get_rect()

        # Load the rocket image and get its rect.
        self.image = pygame.image.load('images/rocket.bmp')
        self.rect = self.image.get_rect()

        # Start each new rocket at the center of the screen
        self.rect.midleft = self.screen_rect.midleft

        # Store decimal values for the rocket's y position
        self.y = float(self.rect.y)

        # Movement flags
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the rocket's position based on the movement flags."""
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.rocket_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.rocket_speed

        # Update rect object from self
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
