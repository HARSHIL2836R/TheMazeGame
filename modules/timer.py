"""Module for creating customised timer"""

import pygame

class Timer():
    def __init__(self, time) -> None:
        """
        Initialise a timer objeect with attributes:
        start time, end time, current time, time elapsed, time reamaining, pause (boolean)
        """
        self.start_time = pygame.time.get_ticks()
        self.end_time = time
        self.current_time = self.start_time
        self.time_elapsed = 0
        self.time_remaining = 0
        self.pause = False
    
    def update(self):
        """
        Method to update the object's using the pygame's time class
        """
        self.current_time = pygame.time.get_ticks()
        self.time_elapsed = self.current_time - self.start_time
        self.time_remaining = self.end_time - self.current_time
    
    def check(self)->bool:
        """
        Method to check whether the timer has ended (True) or not
        """
        if self.time_remaining < 0:
            return True