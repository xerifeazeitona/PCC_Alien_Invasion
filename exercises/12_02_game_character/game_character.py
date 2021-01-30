"""
12-2. Game Character
Find a bitmap image of a game character you like or convert an image to
a bitmap. Make a class that draws the character at the center of the 
screen and match the background color of the image to the background
color of the screen, or vice versa.
"""
import pygame
import sys

class Hero:
    """A class to manage the hero."""

    def __init__(self, surface):
        """Initialize the hero and set its starting position."""
        self.screen = surface
        self.screen_rect = surface.get_rect()

        # Load the hero image and get its rect.
        self.image = pygame.image.load('hero.bmp')
        self.rect = self.image.get_rect()

        # Start hero at the center of the screen.
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the hero at its current location."""
        self.screen.blit(self.image, self.rect)
        
# initialize pygame
pygame.init()
# create surface
surface = pygame.display.set_mode((1200, 800))
# set title bar caption
pygame.display.set_caption("12-2 Game Character")
# creates a hero
hero = Hero(surface)
# set background color to sky blue
bg_color = (135, 206, 235)
surface.fill(bg_color)

while True:
    # loops until window is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Make the most recently drawn screen visible
    hero.blitme()
    pygame.display.flip()
