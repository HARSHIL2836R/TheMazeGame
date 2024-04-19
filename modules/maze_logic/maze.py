"""Module to Generate and Store Maze in the class Maze"""
import numpy as np

class Maze():
    def __init__(self,dim) -> None:
        """
        Params:
            dim: dimension of maze
        """
        self.dim=dim
        self.mazrix = -1 * np.ones(dim,dim)

    

