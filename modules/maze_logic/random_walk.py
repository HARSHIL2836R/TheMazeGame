import random
import matplotlib.pyplot as plt
import numpy as np
from maze import Maze

def generate_random_walk(start_coord, end_coord, dimx=None, dimy=None)->Maze:
    """
    Args:
        start_coord: tuple, representing the startpoint
        end_coord: tuple, representing the endpoint
        dimx: int, X dimension of the maze
        dimy: int, Y dimension of the maze
    Returns:
        Set: {maze ,sequence of U,D,L,R representing the walk}
    """
    #If dimension is not provided, interpret the maze with dimension as the distance between start and end
    if dimx==None:
        dimx=end_coord[0]-start_coord[0]+1
    if dimy==None:
        dimy=end_coord[1]-start_coord[1]+1

    the_maze = Maze((dimx,dimy))
    
    def run()->int:
        the_maze.restart()
        maze = the_maze.mazrix

        curr_coord = start_coord
        maze[curr_coord[1]][curr_coord[0]] = 0
        walk = [curr_coord]
        prev_move=None
        total_steps=0
        directions = []

        while curr_coord != end_coord:
            possible_moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            match_moves = {(0,1):'D',(0,-1):'U',(1,0):'R',(-1,0):'L'}
            
            if prev_move:
                possible_moves.remove((-prev_move[0], -prev_move[1]))  # Remove the reverse move

            next_move = random.choice(possible_moves)
            new_coord = (curr_coord[0] + next_move[0], curr_coord[1] + next_move[1])
            
            if (0 <= new_coord[0] < dimx and
                0 <= new_coord[1] < dimy):
                curr_coord = new_coord
                walk.append(new_coord) # add coord to walk
                maze[curr_coord[1]][curr_coord[0]]=0 # make the corresponding cell zero
                directions.append(match_moves[next_move])
                prev_move = next_move
                print(maze, walk, directions)
                total_steps += 1
            else:
                continue

        the_maze.solution(directions,walk)
        return total_steps

    threshold = dimx*dimy/3
    
    runs = run()
    while runs > threshold:
        runs = run()

    return the_maze

def check_working():
    start_coord = (0, 0)
    end_coord = (4, 4)
    random_walk = generate_random_walk(start_coord, end_coord,10,10).solution_.walk

    # Separate x and y coordinates for plotting
    x_data = [step[0] for step in random_walk]
    y_data = [-step[1] for step in random_walk]

    for step in random_walk:
        print(step)

    plt.plot(x_data, y_data)  # Plot using x and y coordinates separately
    plt.show()

if __name__=="__main__":
    check_working()