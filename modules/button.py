"""Module to define the Button class"""
import pygame.font

class Button():
    def __init__(self, screen, msg, active_button_color, inactive_button_color, text_color, width, height, center_pos) -> None:
        """Initialize button attributes
        Args:
            screen: Surface
            msg: str, The string to add in button
        Returns:
            None
        """
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.active_button_color = active_button_color
        self.inactive_button_color = inactive_button_color

        # Set dimensions and properties of the button
        self.width, self.height = width, height
        self.button_color = inactive_button_color
        self.text_color = text_color
        self.font = pygame.font.SysFont("monospace", 48)

        # Build button
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = center_pos

        self.org_msg = msg
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

    def update_button(self, mouse_x, mouse_y):
        if self.rect.collidepoint(mouse_x,mouse_y):
            self.button_color = self.active_button_color
            self.prep_msg(self.org_msg)
        else:
            self.button_color = self.inactive_button_color
            self.prep_msg(self.org_msg)