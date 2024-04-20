"""Module to Generate and Store Maze in the class Maze"""
import numpy as np

class Maze():
    def __init__(self,dim) -> None:
        """
        Params:
            dim: tuple(x,y), dimensions of maze
        """
        self.dim=dim
        self.mazrix = -1 * np.ones((dim[0]*2,dim[1]*2))
        self.solution_=Solution(None,None)
    
    def __copy__(self):
        new = Maze(self.dim)
        new.mazrix = self.mazrix.copy()
        new.solution_=Solution(None, None)
        new.solution(self.solution_.directions,self.solution_.walk)
        return new

    def restart(self):
        self.mazrix = -1 * np.ones(self.dim)
    
    def solution(self,directions,walk):
        self.solution_.directions = directions
        self.solution_.walk = walk

class Solution():
    def __init__(self,directions,walk) -> None:
        self.directions = directions
        self.walk = walk