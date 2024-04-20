import random
from tabnanny import check
import matplotlib.pyplot as plt

def generate_random_walk(start_coord, end_coord):
    curr_coord = start_coord
    walk = [curr_coord]
    
    while curr_coord != end_coord:
        next_move = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        new_coord = (curr_coord[0] + next_move[0], curr_coord[1] + next_move[1])
        
        if (0 <= new_coord[0] <= end_coord[0] and
            0 <= new_coord[1] <= end_coord[1]):
            curr_coord = new_coord
            walk.append(new_coord)
    
    return walk

def check_working():
    start_coord = (0, 0)
    end_coord = (4, 4)
    random_walk = generate_random_walk(start_coord, end_coord)

    # Separate x and y coordinates for plotting
    x_data = [step[0] for step in random_walk]
    y_data = [step[1] for step in random_walk]

    for step in random_walk:
        print(step)

    plt.plot(x_data, y_data)  # Plot using x and y coordinates separately
    plt.show()

if __name__ == "random walk from replit":
    check_working()