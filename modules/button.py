"""Module to define the Button class, child of pygame.sprite.Sprite class"""
import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, screen: pygame.Surface, msg: str, active_button_color: tuple[int], inactive_button_color: tuple[int], text_color: tuple[int], width: int, height: int, center_pos: tuple[int]) -> None:
        """
        Initialize button's attributes
        Namely, Screen over which button is drawn, Active button color (active on hover), Inactive button color, Button's width, height, color, text color, text font, the text (message)
        Args:
            screen: Surface, over which button is to be drawn
            msg: str, The string to add in button
            ...
            center_pos: tuple[int], coordinates of center of rect of object
        Returns:
            None
        """
        super().__init__()

        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.active_button_color = active_button_color
        self.inactive_button_color = inactive_button_color

        # Set dimensions and properties of the button
        self.width, self.height = width, height
        self.button_color = inactive_button_color
        self.text_color = text_color
        self.font = pygame.font.Font('fonts/Blox2.ttf',40)

        # Build button
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = center_pos

        self.org_msg = msg
        self.prep_msg(msg)
    
    def prep_msg(self, msg):
        """
        Turn msg into a rendered image and center text on the button
        Args:
            msg: str, messag on button
        Returns:
            None
        """
        self.msg_image = self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self)->None:
        """
        Function to blit the button on screen
        """
        # Draw blank button and then draw message.
        self.screen.fill(self.button_color, self.rect)
        self.msg_image_rect.center = self.rect.center
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def update_button(self, mouse_x, mouse_y):
        """
        Function to check whether the button is being hovered or not
        """
        if self.rect.collidepoint(mouse_x,mouse_y):
            self.button_color = self.active_button_color
            self.prep_msg(self.org_msg)
        else:
            self.button_color = self.inactive_button_color
            self.prep_msg(self.org_msg)

    def update_animation(self):
        """
        Function to animate the button falling down
        """
        self.rect.move_ip(0,5)

        #kill the buttoon after it is not visible
        if self.rect.top > self.screen.get_height():
            self.kill()
    
    def hearts(self):
        """
        Draws Heart image depiciting lives of the player
        """
        self.screen.set_alpha(0)
        self.msg_image = pygame.image.load('images/heart.png')
        self.msg_image_rect.center = self.rect.center
        self.screen.blit(self.msg_image, self.msg_image_rect)