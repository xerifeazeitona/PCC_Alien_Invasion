"""
The Bullet class inherits from Sprite, which we import from the
pygame.sprite module. When you use sprites, you can group related
elements in your game and act on all the grouped elements at once.
"""
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, sr_game):
        """Create a bullet object at the rocket's current position."""
        super().__init__()
        self.screen = sr_game.screen
        self.settings = sr_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midleft = sr_game.rocket.rect.midright

        # Store the bullet's position as a decimal value.
        self.x = float(self.rect.x)

    def update(self):
        """Move the bullet through the screen."""
        # Update the decimal positon of the bullet.
        self.x += self.settings.bullet_speed
        # Update the rect position
        self.rect.x = self.x

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
        