import copy
import random
import matplotlib.pyplot as plt
import numpy as np
from maze import Maze

def generate_random_walk(start_coord, end_coord, dimx=None, dimy=None,maze_=None)->Maze:
    """
    Args:
        start_coord: tuple, representing the startpoint
        end_coord: tuple, representing the endpoint
        dimx: int, X dimension of the maze
        dimy: int, Y dimension of the maze
        maze_: Maze, build upon the given maze or make a new maze if not provided
    Returns:
        Maze: New instance of class Maze
    """
    #Scale start and end coordinates to match our walled maze
    start_coord = (start_coord[0]*2,start_coord[1]*2)
    end_coord = (end_coord[0]*2,end_coord[1]*2)

    #If dimension is not provided, interpret the maze with dimension as the distance between start and end
    try:
        if maze_ == None:
            if dimx==None:
                dimx=end_coord[0]-start_coord[0]+1
            if dimy==None:
                dimy=end_coord[1]-start_coord[1]+1
            maze_ = Maze((dimx,dimy))
    except ValueError:
        pass

    if dimx == None:
        dimx=maze_.mazrix.shape[0]/2
    if dimy==None:
        dimy=maze_.mazrix.shape[1]/2
    
    global the_maze
    the_maze = None

    def run()->int:
        global the_maze
        the_maze = maze_.__copy__()
        maze = the_maze.mazrix

        curr_coord = start_coord
        maze[curr_coord[1]][curr_coord[0]] = 0
        walk = [curr_coord]
        prev_move=None
        total_steps=0
        directions = []

        while curr_coord != end_coord:
            possible_moves = [(0, 2), (0, -2), (2, 0), (-2, 0)]
            match_moves = {(0,2):'D',(0,-2):'U',(2,0):'R',(-2,0):'L'}
            match_wall = {'D':(0,-1),'U':(0,1),'R':(-1,0),'L':(1,0)}
            
            if prev_move:
                possible_moves.remove((-prev_move[0], -prev_move[1]))  # Remove the reverse move

            next_move = random.choice(possible_moves)
            new_coord = (curr_coord[0] + next_move[0], curr_coord[1] + next_move[1])
            
            if (0 <= new_coord[0] < dimx*2 and
                0 <= new_coord[1] < dimy*2):
                curr_coord = new_coord
                walk.append(new_coord) # add coord to walk

                maze[curr_coord[1]][curr_coord[0]]=0 # make the corresponding cell zero

                direction = match_moves[next_move]
                wall_coord = (curr_coord[0]+match_wall[direction][0],curr_coord[1]+match_wall[direction][1])
                maze[wall_coord[1]][wall_coord[0]]=0 # make the corresponding wall zero

                directions.append(direction)

                print(maze, walk, directions)
                total_steps += 1
                prev_move = next_move #update iterable
            else:
                continue

        the_maze.solution(directions,[(x[0]/2,x[1]/2) for x in walk])
        return total_steps

    threshold = dimx*dimy/2
    
    runs = run()
    while runs > threshold:
        runs = run()

    print("maze_",maze_.mazrix)
    return the_maze

def check_working()->None:
    maze=Maze((3,3))
    mazrix = np.array([[ 0.,  0.,  0., -1., -1., -1.],
    [-1., -1.,  0., -1., -1., -1.],
    [-1., -1.,  0., -1., -1., -1.],
    [-1., -1., -1., -1., -1., -1.],
    [-1., -1., -1., -1., -1., -1.],
    [-1., -1., -1., -1., -1., -1.]])
    maze.mazrix = mazrix
    start_coord = (2, 0)
    end_coord = (0, 2)
    random_walk = generate_random_walk(start_coord, end_coord,maze_=maze).solution_.walk

    # Separate x and y coordinates for plotting
    x_data = [step[0] for step in random_walk]
    y_data = [-step[1] for step in random_walk]

    for step in random_walk:
        print(step)

    plt.plot(x_data, y_data)  # Plot using x and y coordinates separately
    plt.show()

if __name__=="__main__":
    check_working()