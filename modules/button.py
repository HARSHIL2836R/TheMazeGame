"""Module to define the Button class"""
import pygame.font

class Button():
    def __init__(self, screen, msg, button_color, text_color, width, height, center_pos) -> None:
        """Initialize button attributes
        Args:
            screen: Surface
            msg: str, The string to add in button
        Returns:
            None
        """
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Set dimensions and properties of the button
        self.width, self.height = width, height
        self.button_color = button_color
        self.text_color = text_color
        self.font = pygame.font.SysFont(None, 48)

        # Build button
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = center_pos

        self.prep_msg(msg)
    
    def prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button
        Args:
            msg: str, messag on button
        Returns:
            None
        """
        self.msg_image = self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Draw blank button and then draw message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)