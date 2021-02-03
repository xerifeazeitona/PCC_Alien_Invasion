"""
GameStats class file.
"""
class GameStats:
    """Track statistics for Super Rocket!!!"""

    def __init__(self, sr_game):
        """Initialize statistics."""
        self.settings = sr_game.settings
        self.reset_stats()
        # Start Alien Invasion in an active state.
        self.game_active = True

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.rockets_left = self.settings.rocket_limit
