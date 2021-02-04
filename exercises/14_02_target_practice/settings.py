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
        self.rocket_limit = 3

        # Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (120, 120, 120)
        self.bullets_allowed = 3

        # Enemy settings
        self.enemy_speed = 0.5
        self.fleet_advance_speed = 20
        # 1 for up, -1 for down
        self.fleet_direction = 1
