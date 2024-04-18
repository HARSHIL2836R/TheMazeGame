import numpy as np

DIM = 50

maze = -1*np.ones((DIM,DIM), dtype=int)
cordi = [0,0]

#while cordi != [DIM-1,DIM-1]:
for i in range(5): #DEBUGGING
    """
    a:right
    b:down
    c:left
    d:up
    """
    a,b,c,d = [0,1],[1,0],[0,-1],[-1,0]
    step = np.random.choice(np.array([a,b,c,d],dtype=object),p=[0.1,0.4,0.1,0.4])

    if list(cordi + list(step))[0] in np.arange(10) and list(cordi + list(step))[1] in np.arange(10):
        cordi += list(step)

    maze[cordi[0]][cordi[1]] = 0 
print(maze)