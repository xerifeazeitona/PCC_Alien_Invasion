"""
Placing one enemy on the screen is like placing a rocket on the screen.
Each enemy’s behavior is controlled by a class called Enemy, which we’ll
structure like the Rocket class.
"""
import pygame
from pygame.sprite import Sprite

class Enemy(Sprite):
    """A class to represent a single enemy in the fleet."""

    def __init__(self, sr_game):
        """Initialize the enemy and set its starting position."""
        super().__init__()
        self.screen = sr_game.screen
        self.settings = sr_game.settings

        # Load the enemy image and set its rect attribute.
        self.image = pygame.image.load('images/enemy.bmp')
        self.rect = self.image.get_rect()

        # Start each new enemy near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the enemy's exact vertical position.
        self.y = float(self.rect.y)

    def check_edges(self):
        """Return true if enemy is at the edge of the screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom or self.rect.top <= 0:
            return True
        return False

    def update(self):
        """Move the enemy."""
        self.y += (self.settings.enemy_speed * self.settings.fleet_direction)
        self.rect.y = self.y
