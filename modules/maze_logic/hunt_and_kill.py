from matplotlib.pylab import rand
import numpy as np
import random
#My modules
from modules.maze_logic.maze import Maze

def hunt_n_kill(maze_: Maze, points: list, debug: bool=False)->Maze:
    """
    Args:
        maze: Maze, the maze over which Hunt and Kill algorithm is to be applied to complete it
        points: list, the list of points open in maze
        debug: bool, if true, turn on the print statements
    Returns:
        Maze: New instance of class Maze
    """

    the_maze = maze_.__copy__()
    maze = the_maze.mazrix
    dimx = the_maze.dim[0]
    dimy = the_maze.dim[1]
    coords = [(x,y) for x in np.arange(dimx) for y in np.arange(dimy)]
    
    while not (np.all([maze[2*x][2*y] == 0 for (x,y) in coords])):
        #Initialise
        new_coords = random.sample(coords,len(coords))
        for coord in new_coords:
            start_point = (coord[0]*2,coord[1]*2)
            curr_coord = start_point
            neighbors = [(curr_coord[0],curr_coord[1]+2),(curr_coord[0],curr_coord[1]-2),(curr_coord[0]+2,curr_coord[1]),(curr_coord[0]-2,curr_coord[1])]
            neighbors = [(x,y) for (x,y) in neighbors if ((x>=0) and (y>=0) and (x<dimx*2) and (y<dimy*2))]
            #check if all neighbors are visited
            if (np.all([maze[y][x] == 0 for (x,y) in neighbors])):
                #Single captured Cell
                if maze[curr_coord[1],curr_coord[0]] == -1:
                    maze[curr_coord[1],curr_coord[0]] = 0
                    #Open one random wall
                    wall1 = [curr_coord[1]+random.choice((-1,1)),curr_coord[0]+random.choice((-1,1))]
                    
                    if (0<=wall1[0]<dimx and 0<=wall1[1]<dimy):
                        maze[wall1] = 0
                    continue
                #Otherwise continue
                continue
            else:
                for neighbor in neighbors:
                    if (neighbor[0]/2,neighbor[1]/2) in maze_.solution_.walk:
                        #Make it less likely to interfere into solution path
                        toss = random.choice((0,1))
                        if toss:
                            continue
                #Otherwise continue
                break
        
        if debug:
            print("-"*100)
            print("start_point,points,neighbors",start_point,points,neighbors)
        
        count = 0
        while (not (np.all([maze[int(y/2),int(x/2)] == 0 for (x,y) in neighbors]))) and count < 100:
            if debug:
                print("TRYING TO MOVIE","\n", maze)
            possible_moves = [(0, 2), (0, -2), (2, 0), (-2, 0)]
            match_moves = {(0,2):'D',(0,-2):'U',(2,0):'R',(-2,0):'L'}
            match_wall = {'D':(0,-1),'U':(0,1),'R':(-1,0),'L':(1,0)}
            
            random.shuffle(possible_moves)
            for next_move in possible_moves:
                new_coord = (curr_coord[0] + next_move[0], curr_coord[1] + next_move[1])
                if not (0<=new_coord[0]<dimx*2 and 0<=new_coord[1]<dimy*2):
                    continue
                if maze[new_coord[1]][new_coord[0]] == 0:
                    continue
                else:
                    break
            
            if (0 <= new_coord[0] < dimx*2 and 0 <= new_coord[1] < dimy*2):
                    curr_coord = new_coord
                    neighbors = [(curr_coord[0],curr_coord[1]+2),(curr_coord[0],curr_coord[1]-2),(curr_coord[0]+2,curr_coord[1]),(curr_coord[0]-2,curr_coord[1])]
                    
                    maze[curr_coord[1]][curr_coord[0]]=0 # make the corresponding cell zero

                    direction = match_moves[next_move]
                    wall_coord = (curr_coord[0]+match_wall[direction][0],curr_coord[1]+match_wall[direction][1])
                    maze[wall_coord[1]][wall_coord[0]]=0 # make the corresponding wall zero
                    count += 1
            else:
                count += 1
                continue
        
        if debug:
            #print("coords:",coords)
            #print([maze[2*x][2*y] == 0 for (x,y) in coords])
            print(list(zip(coords,[maze[2*x][2*y] == 0 for (x,y) in coords])))
            print(np.all([maze[2*x][2*y] == 0 for (x,y) in coords]))
            input("Press to HUNT")
    
    if debug:
        print("Hunting Done")
        arr_all_odd=np.delete(maze, list(range(1, maze.shape[0], 2)), axis=1)
        arr_odd_odd=np.delete(arr_all_odd, list(range(1, maze.shape[1], 2)), axis=0)
        print(arr_odd_odd)
    
    return the_maze