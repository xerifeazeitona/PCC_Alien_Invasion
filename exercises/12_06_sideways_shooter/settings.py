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
        self.bg_color = (10, 20, 50)

        # Rocket settings
        self.rocket_speed = 1.5

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (120, 120, 120)
        self.bullets_allowed = 3
