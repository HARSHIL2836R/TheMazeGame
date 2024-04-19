import numpy as np

class Move_functions():
    def up(pointer,vmaze)->list:
        try:
            if vmaze[pointer[0],pointer[1]-1] == -1:
                #update pointer only if next cell is in the maze and is univisited
                pointer[1] -= 1
                return pointer
            else:
                return pointer
        except IndexError:
            return pointer
    def down(pointer,vmaze)->list:
        try:
            if vmaze[pointer[0],pointer[1]+1] == -1:
                #update pointer only if next cell is in the maze and is univisited
                pointer[1] += 1
                return pointer
            else:
                return pointer
        except IndexError:
            return pointer
    def left(pointer,vmaze)->list:
        try:
            if vmaze[pointer[0]-1,pointer[1]] == -1:
                #update pointer only if next cell is in the maze and is univisited
                pointer[0] -= 1
                return pointer
            else:
                return pointer
        except IndexError:
            return pointer
    def right(pointer,vmaze)->list:
        try:
            if vmaze[pointer[0]+1,pointer[1]] == -1:
                #update pointer only if next cell is in the maze and is univisited
                pointer[0] += 1
                return pointer
            else:
                return pointer
        except IndexError:
            return pointer


def dummy_random_walk(start,end,dimx=None,dimy=None)->tuple:
    """
    Args:
        start: tuple, representing the startpoint
        end: tuple, representing the endpoint
        dim: int, dimension of the maze
    Returns:
        tuple, sequence of U,D,L,R representing the walk
    """
    
    #If dimension is not provided, interpret the maze with dimension as the distance between start and end
    if dimx==None:
        dimx=end[0]-start[0]
    if dimy==None:
        dimy=end[1]-start[1]

    vmaze = -1*np.ones((dimx,dimy))

    pointer = [0,0] #Initiate pointer
    
    ops = []

    counter = 0
    max_count = (dimx*dimy)**2

    while ((np.any(vmaze==(-1)) == True) or (pointer == [end[0]-start[0],end[1]-start[1]])) and counter < max_count:
        vmaze[pointer[0]][pointer[1]] = 0
        print(vmaze)

        #up,right,down,left
        probabilities=(0.25,0.25,0.25,0.25)
        step = np.random.choice([1,2,3,4],p=probabilities)
        match step:
            case 1:
                pointer_new = Move_functions.up(pointer,vmaze)
                if pointer_new == pointer:
                    pass
                else:
                    pointer = pointer_new
                    ops.append('U')
            case 2:
                pointer_new = Move_functions.right(pointer,vmaze)
                if pointer_new == pointer:
                    pass
                else:
                    pointer = pointer_new
                    ops.append('R')
                
            case 3:
                pointer_new = Move_functions.down(pointer,vmaze)
                if pointer_new == pointer:
                    pass
                else:
                    pointer = pointer_new
                    ops.append('D')
            case 4:
                pointer_new = Move_functions.left(pointer,vmaze)
                if pointer_new == pointer:
                    pass
                else:
                    pointer = pointer_new
                    ops.append('L')
        counter += 1

    if counter == max_count:
        raise TimeoutError
    else:
        return ops

def random_walk(start,end,dimx=None,dimy=None):
    while True:
        try:
            ops = dummy_random_walk(start,end,dimx,dimy)
            break
        except TimeoutError:
            print("parsing")
            continue
    return ops

print(random_walk((0,0),(4,4)))