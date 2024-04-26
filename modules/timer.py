"""Module for customised timer"""
from time import sleep
import pygame

class Timer():
    def __init__(self, time) -> None:
        self.start_time = pygame.time.get_ticks()
        self.end_time = time
        self.current_time = self.start_time
        self.time_elapsed = 0
        self.time_remaining = 0
        self.pause = False
    
    def update(self):
        self.current_time = pygame.time.get_ticks()
        self.time_elapsed = self.current_time - self.start_time
        self.time_remaining = self.end_time - self.current_time
    
    def check(self)->bool:
        if self.time_remaining < 0:
            return True

if __name__ == "__main__":
    pygame.init()
    timer = Timer(10)
    print(timer.start_time,timer.end_time,timer.current_time)
    sleep(2)
    timer.update()
    print(pygame.time.get_ticks())
    print(timer.start_time,timer.end_time,timer.current_time)