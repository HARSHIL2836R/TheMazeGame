import numpy as np
import pygame
#In Pygame, the origin (0, 0) is at the top-left corner of the screen, and coordinates increase as you go down and to the right

#import user defined modules
from modules.settings import Settings
from modules.player import Player
import modules.game_functions as gf
import modules.menu as menu
from modules.game_screen import play_game
import modules.end_screen as the_end

def set_display(mg_settings: Settings):
    #DISPLAY THE COMPLETE MAP
    if mg_settings.MODE == "map":
        #display map_
        map_ = pygame.display.set_mode((mg_settings.screen_width,mg_settings.screen_height))
        #not needed indeed here
        screen = pygame.surface.Surface((mg_settings.screen_width, mg_settings.screen_height))
        pygame.display.set_caption("The Maze Game")
            
    #DISPLAY HALF OF MAP
    else:
        #surface for map_ (do I need this?)
        map_ = pygame.surface.Surface((mg_settings.screen_width*2,mg_settings.screen_height*2))
        #the screen to be displayed
        screen = pygame.display.set_mode((mg_settings.screen_width, mg_settings.screen_height))
        pygame.display.set_caption("The Maze Game")
    return map_,screen    
    
def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    mg_settings = Settings()

    #set screen dimensions and title
    map_,screen = set_display(mg_settings)
    if mg_settings.MODE == "map":
        menu_out = menu.show(map_)
    else:
        menu_out = menu.show(screen)

    if menu_out == "exit":
        quit()
    difficulty = menu_out
    difficulty = int(difficulty)
    mg_settings.difficulty = difficulty

    #Set dimensions based on difficulty
    if difficulty == 1:
        mg_settings.dim =(5,5)
        mg_settings.start_point =(0,0)
        mg_settings.end_point =(4,4)
    if difficulty == 2:
        mg_settings.dim =(10,10)
        mg_settings.start_point =(0,0)
        mg_settings.end_point =(9,9)
    if difficulty == 3:
        mg_settings.dim = (20,20)
        mg_settings.start_point =(0,0)
        mg_settings.end_point =(9,9)
        map_ = pygame.surface.Surface((mg_settings.screen_width*4,mg_settings.screen_height*4))

    pygame.display.quit()

    #BUILD MAZE
    print("Building Maze...")
    curr_maze=gf.build_maze(mg_settings.dim,int(difficulty),mg_settings.start_point,mg_settings.end_point)
    
    mg_settings.create_wall_images_list(np.sum(np.where(curr_maze.mazrix == -1))+2*np.shape(curr_maze.mazrix)[0]-1)
    print("white",np.sum(np.where(curr_maze.mazrix == 0)))
    
    print("Building done")
    map_,screen = set_display(mg_settings)
    
    #write solution in file
    file = open('path.txt','w')
    for i in range(len(curr_maze.solution_.directions)):
        file.write(curr_maze.solution_.directions[i])
    file.close()
    mg_settings.set_dim(map_, curr_maze)

    #Intanciate the player
    player = Player(map_,curr_maze)
    player.set_dim(mg_settings.box_width,mg_settings.box_height)

    #Instanciate the scoreboard and Play the Game!
    scoreboard = mg_settings.ScoreBoard()
    play_game_out = play_game(screen,map_,mg_settings,player,curr_maze,scoreboard)
    
    if play_game_out == "game_over":
        print("Game completed")
        if mg_settings.MODE == "map":
            print(the_end.show(map_))
        else:
            print(the_end.show(screen))

    elif play_game_out == "timeout":
        print("Game Timeout")

        if mg_settings.MODE == "map":
            print(the_end.show(map_))
        else:
            print(the_end.show(screen))

def check_game():
    pygame.init()
    mg_settings = Settings()
    map_,screen = set_display(mg_settings)
    difficulty = 1
    #BUILD MAZE
    print("Building Maze...")
    curr_maze=gf.build_maze(mg_settings.dim,int(difficulty))
    print("white",np.sum(np.where(curr_maze.mazrix == 0)))
    
    print("Building done")
    map_,screen = set_display(mg_settings)
    
    #write solution in file
    file = open('path.txt','w')
    for i in range(len(curr_maze.solution_.directions)):
        file.write(curr_maze.solution_.directions[i])
    file.close()
    mg_settings.set_dim(map_, curr_maze)

    #Intanciate the player
    player = Player(map_,curr_maze)
    player.set_dim(mg_settings.box_width,mg_settings.box_height)

    scoreboard = mg_settings.ScoreBoard()
    play_game_out = play_game(screen,map_,mg_settings,player,curr_maze,scoreboard)
    if play_game_out == "game_over":
        print("Game completed")
    elif play_game_out == "timeout":
        print("Game Timeout")

run_game()
#check_game()