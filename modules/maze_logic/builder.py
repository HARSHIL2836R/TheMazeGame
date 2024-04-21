#My modules
from modules.maze_logic.maze import Maze
from modules.maze_logic.hunt_and_kill import hunt_n_kill
from modules.maze_logic.random_walk import generate_random_walk

def build_maze(maze: Maze, difficulty: int)->Maze:
    dimx = maze.dim[0]
    dimy = maze.dim[1]
    if difficulty == 1:
        new_maze = generate_random_walk((0,0),(dimx-1,dimy-1),maze_=maze,lower_bound=0,upper_bound=dimx*dimy/2)
        points = [(int(x[0]),int(x[1])) for x in new_maze.solution_.walk]

        #Completing the maze
        new_maze = hunt_n_kill(new_maze, points, debug=False)
        return new_maze

if __name__ == "__main__":
    #Checking working
    my_maze = Maze((5,5))
    build_maze(my_maze,1)