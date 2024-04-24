"""Module to Generate and Store Maze in the class Maze"""
from hmac import new
import re
from tkinter import NO
import numpy as np

class Maze():
    def __init__(self,dim: tuple) -> None:
        """
        Params:
            dim: tuple(x,y), dimensions of maze
        """
        self.dim=dim
        self.mazrix = -1 * np.ones((dim[0]*2,dim[1]*2), dtype=int)
        self.solution_=Solution(None,None)
    
    def __copy__(self):
        new = Maze(self.dim)
        new.mazrix = self.mazrix.copy()
        new.solution_=Solution(None, None)
        new.solution(self.solution_.directions,self.solution_.walk)
        return new

    def restart(self):
        self.mazrix = -1 * np.ones(self.dim)
    
    def solution(self,directions: list,walk: list):
        self.solution_.directions = directions
        self.solution_.walk = walk
        
    def update_solution(self,directions: list,walk: list):
            start_coord = walk[0]
            end_coord = walk[-1]
            if start_coord == end_coord:
                return None
            for i in range(len(self.solution_.walk)-1):
                if (self.solution_.walk[i] == start_coord) and (self.solution_.walk[i+1] == end_coord):
                    #CHANGE WALK
                    new_walk = self.solution_.walk[:i+1]
                    new_walk.extend(walk[1:-1])
                    new_walk.extend(self.solution_.walk[i+1:])
                    #CHANGE DIRECTIONS
                    new_directions = self.solution_.directions[:i]
                    new_directions.extend(directions)
                    new_directions.extend(self.solution_.directions[i+1:])

                    self.solution_.walk = new_walk
                    self.solution_.directions = new_directions

class Solution():
    def __init__(self,directions: list,walk: list) -> None:
        self.directions = directions
        self.walk = walk