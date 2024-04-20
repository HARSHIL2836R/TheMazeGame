"""Module to Generate and Store Maze in the class Maze"""
import numpy as np

class Maze():
    def __init__(self,dim) -> None:
        """
        Params:
            dim: tuple, dimensions of maze
        """
        self.dim=dim
        self.mazrix = -1 * np.ones(dim)
        self.solution_=Solution(None,None)

    def restart(self):
        self.mazrix = -1 * np.ones(self.dim)
    
    def solution(self,directions,walk):
        self.solution_.directions = directions
        self.solution_.walk = walk

class Solution():
    def __init__(self,directions,walk) -> None:
        self.directions = directions
        self.walk = walk