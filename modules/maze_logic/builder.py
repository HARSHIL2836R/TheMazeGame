#My modules
import random
from modules.maze_logic.maze import Maze
from modules.maze_logic.hunt_and_kill import hunt_n_kill
from modules.maze_logic.random_walk import generate_random_walk

def build_maze(maze: Maze, difficulty: int, start_point: tuple,end_point: tuple)->Maze:
    dimx = maze.dim[0]
    dimy = maze.dim[1]
    if difficulty == 1:
        #Make the Solution Path
        new_maze = generate_random_walk(start_point,end_point,maze_=maze,lower_bound=0,upper_bound=dimx*dimy/2)
        points = [(int(x[0]),int(x[1])) for x in new_maze.solution_.walk]

        #Completing the maze
        new_maze = hunt_n_kill(new_maze, points, debug=False)
        return new_maze
    
    if difficulty == 2:
        #Make the Solution Path
        new_maze = generate_random_walk(start_point,end_point,maze_=maze,lower_bound=0,upper_bound=dimx*dimy/2,debug=False)
        points = [(int(x[0]),int(x[1])) for x in new_maze.solution_.walk]

        #Modify the solution path
        rand_pt = random.randint(0,len(points)-2)
        new_maze = generate_random_walk(points[rand_pt],points[rand_pt+1],maze_=new_maze,lower_bound=2,upper_bound=dimx*dimy/2,debug=False,update_solution=True)
        
        middle_wall = (int((points[rand_pt][0]+points[rand_pt+1][0])),int((points[rand_pt][1]+points[rand_pt+1][1])))
        print(middle_wall)
        new_maze.mazrix[middle_wall[1],middle_wall[0]] = -1
        
        #Completing the maze
        new_maze = hunt_n_kill(new_maze, points, debug=False)
        return new_maze
    
    if difficulty == 3:
        #Make the Solution Path
        new_maze = generate_random_walk(start_point,end_point,maze_=maze,lower_bound=0,upper_bound=dimx*dimy/2,debug=False)
        points = [(int(x[0]),int(x[1])) for x in new_maze.solution_.walk]

        #Modify the solution path
        rand_pt = random.randint(0,len(points)-2)
        new_maze = generate_random_walk(points[rand_pt],points[rand_pt+1],maze_=new_maze,lower_bound=2,upper_bound=dimx*dimy/2,debug=False,update_solution=True)
        
        middle_wall = (int((points[rand_pt][0]+points[rand_pt+1][0])),int((points[rand_pt][1]+points[rand_pt+1][1])))
        print(middle_wall)
        new_maze.mazrix[middle_wall[1],middle_wall[0]] = -1
        
        #Completing the maze
        new_maze = hunt_n_kill(new_maze, points, debug=False)
        return new_maze

if __name__ == "__main__":
    #Checking working
    my_maze = Maze((5,5))
    build_maze(my_maze,2)