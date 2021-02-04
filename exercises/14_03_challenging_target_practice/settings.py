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
        self.rocket_limit = 3

        # Bullet settings
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (120, 120, 120)
        self.bullets_allowed = 3

        # Enemy settings
        self.fleet_advance_speed = 20

        # How quickly the game speeds up on level up
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.rocket_speed = 1.5
        self.bullet_speed = 1.5
        self.enemy_speed = 0.5
        # 1 for up, -1 for down
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase the game speed."""
        self.rocket_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.enemy_speed *= self.speedup_scale
        