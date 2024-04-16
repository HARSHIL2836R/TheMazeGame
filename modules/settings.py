'''Module to store the Settings class'''
class Settings():
    """A class to store all settings for Maze Game"""

    def __init__(self):
        """Initialise the game's settings."""
        #Screen settings
        self.screen_width = 800
        self.screen_height = 800
        self.bg_color = (144,43,245)

    class Menu():
        def __init__(self) -> None:
            """Menu Settings"""
            Settings.__init__(self)
            self.screen_color = (145,63,146)
            self.screen_text_color = (255,255,255)
            self.lvl_button_width = self.screen_width/5
            self.lvl_button_height = 60
            self.active_bt_color = 	(0,0,255)
            self.inactive_bt_color = (35,58,119)
            self.bt_text_color = (255,255,255)