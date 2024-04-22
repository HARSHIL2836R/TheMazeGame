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
        if self.solution_.directions == None:
            self.solution_.directions = directions
            self.solution_.walk = walk
        else:
            start_coord = walk[0]
            end_coord = walk[-1]
            if start_coord == end_coord:
                return None
            print(self.solution_.walk)
            print(len(self.solution_.walk))
            for i in range(len(self.solution_.walk)-1):
                if (self.solution_.walk[i] == start_coord) and (self.solution_.walk[i+1] == end_coord):
                    #CHANGE WALK
                    new_walk = self.solution_.walk[:i+1]
                    new_walk.append(walk[1:-1])
                    new_walk.append(self.solution_.walk[i+1:])
                    #CHANGE DIRECTIONS
                    new_directions = self.solution_.directions[:i]
                    new_directions.append(directions[1:-1])
                    new_directions.append(self.solution_.directions[i+1:])

                    self.solution_.walk = new_walk
                    self.solution_.directions = new_directions

class Solution():
    def __init__(self,directions: list,walk: list) -> None:
        self.directions = directions
        self.walk = walk