"""
GameStats class file.
"""
import json

class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        # Start Alien Invasion in an inactive state.
        self.game_active = False
        self.choosing_difficulty = False
        # High score should never be reset.
        self.high_score = 0
        self.get_high_score()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 0

    def get_high_score(self):
        """
        Read the high score from file
        """
        try:
            with open('high_score.hgs') as file_obj:
                hgs = json.load(file_obj)
        except FileNotFoundError:
            hgs = 0
        else:
            self.high_score = int(hgs)

    def set_high_score(self):
        """
        Write the high score to file
        """
        with open('high_score.hgs', 'w') as file_obj:
            json.dump(self.high_score, file_obj)
