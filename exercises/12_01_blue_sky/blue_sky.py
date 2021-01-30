"""
12-1. Blue Sky: Make a Pygame window with a blue background.
"""
import sys
import pygame

# initialize pygame
pygame.init()
# create surface
surface = pygame.display.set_mode((1200, 800))
# set title bar caption
pygame.display.set_caption("12-1 Blue Sky")
# blue sky
bg_color = (135, 206, 235)
# set background color to sky blue
surface.fill(bg_color)

while True:
    # loops until window is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Make the most recently drawn screen visible
    pygame.display.flip()
