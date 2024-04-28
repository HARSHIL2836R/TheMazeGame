from matplotlib.pylab import rand
import numpy as np
import pygame
import random
#In Pygame, the origin (0, 0) is at the top-left corner of the screen, and coordinates increase as you go down and to the right

#import user defined modules
from modules.settings import Settings
from modules.player import Enemy, Player
from modules.game_screen import play_game
import modules.game_functions as gf
import modules.menu as menu
import modules.end_screen as the_end

def set_display(mg_settings: Settings):
    """
    Function to set up a dispaly screen and a map(Surface type) for the game
    Args:
        mg_settings: Settings, class instance containing all game settings
    Returns:
        (Surface, Surface): (map_,screen); in camera mode, the screen gets displayed and map is used to store rects of all the Sprites
    """
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
    """
    Function to run an instance of the Maze Game
    Args:
        None
    Returns:
        str: String indicating whether to rerun the game or not
    """
    # Initialize game and create a screen object.
    pygame.init()
    pygame.mixer.init()
    mg_settings = Settings()

    #set screen dimensions and title
    map_,screen = set_display(mg_settings)
    if mg_settings.MODE == "map":
        menu_out, menu_settings = menu.show(map_)
    else:
        menu_out, menu_settings = menu.show(screen)

    if menu_out == "exit":
        quit()
    
    if menu_settings.is_muted: 
        mg_settings.is_muted = True

    if not mg_settings.is_muted:
        pygame.mixer.Sound('audio/counter-strike-jingle-cs-radio-ok-lets-go.mp3').play()
    difficulty = menu_out
    difficulty = int(difficulty)
    mg_settings.difficulty = difficulty

    #Set dimensions based on difficulty
    if difficulty == 1:
        mg_settings.dim =(5,5)
        mg_settings.start_point =(0,0)
        mg_settings.end_point =(4,4)
        mg_settings.timeout = 10000 
        mg_settings.no_of_enemies = 5
    if difficulty == 2:
        mg_settings.dim =(10,10)
        mg_settings.start_point =(0,0)
        mg_settings.end_point =random.choice([(9,9),(0,9),(9,0)])
        mg_settings.timeout = 20000
        mg_settings.no_of_enemies = 10
    if difficulty == 3:
        mg_settings.dim = (20,20)
        mg_settings.start_point =(0,0)
        mg_settings.end_point = (random.randint(9,20),random.randint(9,20))
        mg_settings.timeout = 30000
        mg_settings.no_of_enemies = 15
        map_ = pygame.surface.Surface((mg_settings.screen_width*4,mg_settings.screen_height*4))

    #Quite display because it's not needed, so that pygame doesn't freeze out when no input is provided from python while building the maze
    pygame.display.quit()

    ####BUILD MAZE
    print("Building Maze...")
    curr_maze=gf.build_maze(mg_settings.dim,int(difficulty),mg_settings.start_point,mg_settings.end_point)
    #Create a list of randomised images to be used in wall sprites
    mg_settings.create_wall_images_list(np.sum(np.where(curr_maze.mazrix == -1))+2*np.shape(curr_maze.mazrix)[0]-1)
    print("white",np.sum(np.where(curr_maze.mazrix == 0)))
    
    print("Building done")
    ####BUILD COMPLETE
    
    #Remake the display screen
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
    enemies = []
    if mg_settings.enable_enemies:
        for i in range(mg_settings.no_of_enemies):
            x = np.random.randint(0,mg_settings.dim[0])
            y = np.random.randint(0,mg_settings.dim[1])
            while (curr_maze.mazrix[y][x] == -1):
                x = np.random.randint(0,mg_settings.dim[0])
                y = np.random.randint(0,mg_settings.dim[1])
            enemies.append(Enemy(player,(x,y)))

    #Instanciate the scoreboard and Play the Game!
    scoreboard = mg_settings.ScoreBoard()
    play_game_out = play_game(screen,map_,mg_settings,player,curr_maze,scoreboard,enemies)
    
    if play_game_out == "game_over":
        print("Game completed")
        if not mg_settings.is_muted:
            scoreboard = Settings.ScoreBoard()
            data = scoreboard.iterable_data()
            if data[-1][-1].strip('\n') == "2": 
                pygame.mixer.Sound('audio/gta-v-death-sound-effect-102.mp3').play()
            else:
                pygame.mixer.Sound('audio/happy-happy-happy-song.mp3').play()
        if mg_settings.MODE == "map":
            var = map_
        else:
            var = screen
        
        #Show the end-screen
        if the_end.show(var) == "rerun":
            return "rerun"
        elif the_end.show(var) == "exit":
            print("exit")
            return False

    elif play_game_out == "timeout":
        print("Game Timeout")
        if not mg_settings.is_muted:
            pygame.mixer.Sound('audio/super-mario-beedoo_F3cwLoe.mp3').play()
        if mg_settings.MODE == "map":
            var = map_
        else:
            var = screen

        #Show the end-screen
        if the_end.show(var) == "rerun":
            return "rerun"
        elif the_end.show(var) == "exit":
            print("exit")
            return False

def check_game():
    """
    Just a dummy function to check whether the game runs nice without need to show menu or end-screen
    """
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

out = "rerun"
while out == "rerun":
    out = run_game()
    print(out)

#Uncomment if you want to run only the game, if so comment out the previous while loop also
#check_game()