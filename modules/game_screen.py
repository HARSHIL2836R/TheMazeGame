"""
Module to store methods to update the game_screen UI
"""
import pygame
import datetime
import random

#My Modules
from modules.button import Button
import modules.game_functions as gf
from modules.maze_logic.maze import Maze
from modules.player import Enemy, Player
from modules.settings import Settings
from modules.timer import Timer

FRAME = 1

def play_game(screen: pygame.Surface, map_: pygame.Surface, mg_settings: Settings, player: Player, curr_maze: Maze, scoreboard: Settings.ScoreBoard, enemies: list[Enemy])->str:
    """
    Exceutes tasks required to play the game
    Namely, control the audio play based on events, call the update_screen method in game_functions, check status of the game, whether player's reached end point or there's timeout, draw score and timer on the screen and limit the game's FPS (not necessarily needed though) 
    """

    #Play background music
    the_wind_rises_theme = pygame.mixer.Sound('audio/caproni.mp3')  
    the_wind_rises_theme.play(loops=-1,fade_ms=1000)  

    #initiate clock and Timer
    clock = pygame.time.Clock()
    timer = Timer(mg_settings.timeout)

    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        event_check_out = gf.check_events(player, mg_settings, enemies)
        if event_check_out == "game_over":
            scoreboard.update_score(player,curr_maze,mg_settings.end_point, timer)
            score = str(datetime.datetime.now())+","+str(scoreboard.curr_score)+","+"{0:.5}".format(str(timer.time_elapsed/1000))+"s,"+str(0)
            scoreboard.add_score(score)
            scoreboard.write_to_file()
            the_wind_rises_theme.fadeout(1000)
            return "game_over"
        elif event_check_out == "player_died":
            scoreboard.update_score(player,curr_maze,mg_settings.end_point, timer)
            score = str(datetime.datetime.now())+","+str(scoreboard.curr_score)+","+"{0:.5}".format(str(timer.time_elapsed/1000))+"s,"+str(2)
            scoreboard.add_score(score)
            scoreboard.write_to_file()
            the_wind_rises_theme.fadeout(1000)
            return "game_over"
        gf.update_screen(mg_settings, map_, screen, player,curr_maze,enemies)

        global FRAME
        print(FRAME)
        if FRAME%4 == 0:        
            #Move the enemies around
            keymap = {'U': (player.width*0,player.height*-1),
                'D': (player.width*0,player.height*1),
                'R': (player.width*1,player.height*0),
                'L': (player.width*-1,player.height*0)}
            for enemy in enemies:
                next_move = random.choice(['U','D','R','L'])
                enemy.move(keymap[next_move][0],keymap[next_move][1])
        FRAME +=1

        #Blit Counter
        if not timer.pause:
            timer.update()
        width = 200
        height = 50
        timer_image = Button(screen, "{0:^4.5}".format(str(timer.time_remaining/1000)),'white','white','black',width,height,(screen.get_rect().topleft[0]+width/2,screen.get_rect().topleft[1]+height/2))
        timer_image.draw_button()

        #Show score
        scoreboard.update_score(player,curr_maze, mg_settings.end_point, timer)
        score = scoreboard.curr_score
        score_image = Button(screen, str(score),'white','white','black',width,height,(screen.get_rect().topleft[0]+width/2,screen.get_rect().topleft[1]+height*3/2))
        score_image.draw_button()

        pygame.display.update()
        # Make the most recently drawn screen visible.
        pygame.display.flip()
        
        #Check whether game is timed out
        if timer.check():
            score = str(datetime.datetime.now())+","+str(scoreboard.curr_score)+","+"{0:.5}".format(str(timer.time_elapsed/1000))+"s,"+str(1)
            scoreboard.add_score(score)
            scoreboard.write_to_file()
            the_wind_rises_theme.fadeout(1000)
            pygame.mixer.Sound('audio/punch-gaming-sound-effect-hd_RzlG1GE.mp3').play()
            return "timeout"
        
        clock.tick(20)