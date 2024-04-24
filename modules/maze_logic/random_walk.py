import time
import random
import matplotlib.pyplot as plt
import numpy as np
#My Modules
from modules.maze_logic.maze import Maze, Solution

def generate_random_walk(start_coord: tuple, end_coord: tuple, dimx: int =None, dimy:int =None,maze_: Maze =None,lower_bound: int=0,upper_bound: int=None, debug: bool = False,update_solution: bool=False)->Maze:
    """
    Args:
        start_coord: tuple, representing the startpoint
        end_coord: tuple, representing the endpoint
        dimx: int, X dimension of the maze
        dimy: int, Y dimension of the maze
        maze_: Maze, build upon the given maze or make a new maze if not provided
        lower_bound: int, minimum number of steps the walk should run
        upper_bound: int, maximum number of steps the walk should run
        debug: bool, if true, print the matrix, directions and walk at each run otherwise suppress printing
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
        dimx=maze_.mazrix.shape[0]
    if dimy==None:
        dimy=maze_.mazrix.shape[1]

    #use default upper bound if not provided
    if upper_bound == None:
        upper_bound = dimx*dimy/2
    
    global the_maze
    the_maze = None

    update_walks=[]
    update_directions=[]

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

        while (curr_coord != end_coord) and (total_steps < upper_bound):
            possible_moves = [(0, 2), (0, -2), (2, 0), (-2, 0)]
            match_moves = {(0,2):'D',(0,-2):'U',(2,0):'R',(-2,0):'L'}
            match_wall = {'D':(0,-1),'U':(0,1),'R':(-1,0),'L':(1,0)}
            
            if prev_move:
                possible_moves.remove((-prev_move[0], -prev_move[1]))  # Remove the reverse move

            next_move = random.choice(possible_moves)
            new_coord = (curr_coord[0] + next_move[0], curr_coord[1] + next_move[1])
            
            if (0 <= new_coord[0] < dimx and
                0 <= new_coord[1] < dimy):
                curr_coord = new_coord
                walk.append(new_coord) # add coord to walk

                maze[curr_coord[1]][curr_coord[0]]=0 # make the corresponding cell zero

                direction = match_moves[next_move]
                wall_coord = (curr_coord[0]+match_wall[direction][0],curr_coord[1]+match_wall[direction][1])
                maze[wall_coord[1]][wall_coord[0]]=0 # make the corresponding wall zero

                directions.append(direction)

                if debug: 
                    print(maze, walk, directions)
                total_steps += 1
                prev_move = next_move #update iterable
            else:
                continue

        if not update_solution:       
            the_maze.solution(directions,[(x[0]/2,x[1]/2) for x in walk])
        else:
            update_directions.append(directions)
            update_walks.append([(x[0]/2,x[1]/2) for x in walk])

        return total_steps

    
    runs = run()
    while (runs > upper_bound) or (runs < lower_bound):
        runs = run()

    if update_solution:
        the_maze.update_solution(update_directions[-1],update_walks[-1])

    if debug:
        print("original_maze",maze_.mazrix)
    return the_maze

def check_working()->None:
    maze=Maze((3,3))
    mazrix = np.array([[ 0,  0,  0, -1, -1, -1],
    [-1, -1,  0, -1, -1, -1],
    [-1, -1,  0, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1]])
    maze.mazrix = mazrix
    start_coord = (0, 0)
    end_coord = (30, 30)
    start_time = time.time()
    random_walk = generate_random_walk(start_coord, end_coord,maze_=None,debug=True).solution_.walk
    end_time = time.time()
    print("Time taken:", end_time-start_time)

    # Separate x and y coordinates for plotting
    x_data = [step[0] for step in random_walk]
    y_data = [-step[1] for step in random_walk]


    plt.plot(x_data, y_data)  # Plot using x and y coordinates separately
    plt.show()

if __name__=="__main__":
    check_working()