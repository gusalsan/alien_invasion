import json
class GameStats:
    """Track statistics for Alien Invasion"""

    def __init__(self, ai_game):
        """Initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()

        # Load high score from file, if it exists
        self.high_score = self._load_high_score()
       

    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def _load_high_score(self):
        """Load high score from file, return 0 if file doesn't exist"""
        try:
            with open('high_score.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return 0
        
    def save_high_score(self):
        """Save high score to file"""
        with open('high_score.json', 'w') as file:
            json.dump(self.high_score, file)
