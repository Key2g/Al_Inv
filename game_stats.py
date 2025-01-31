class GameStats():
    """Track Statistic for alien invasion"""
    
    def __init__(self, ai_settings) -> None:
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()
        
        # Start Alien Invasion in inactive state.
        self.game_active = False

        #High score should never be reset.
        self.high_score = 0
        
    
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0