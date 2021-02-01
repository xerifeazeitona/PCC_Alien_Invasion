"""
Settings class for Super Rocket
"""
class Settings:
    "A class to store all settings for Super Rocket."

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (10, 50, 100)

        # Rocket settings
        self.rocket_speed = 1.5
