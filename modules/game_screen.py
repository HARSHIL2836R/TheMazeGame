"""
Module to store methods to update the game_screen UI
"""
import pygame
import datetime

#My Modules
from modules.button import Button
import modules.game_functions as gf
from modules.maze_logic.maze import Maze
from modules.player import Player
from modules.settings import Settings
from modules.timer import Timer

def play_game(screen: pygame.Surface, map_: pygame.Surface, mg_settings: Settings, player: Player, curr_maze: Maze, scoreboard: Settings.ScoreBoard)->str:
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
        if gf.check_events(player, mg_settings) == "game_over":
            scoreboard.update_score(player,curr_maze,mg_settings.end_point)
            score = str(datetime.datetime.now())+","+str(scoreboard.curr_score)+","+str(timer.time_elapsed/1000)+"s,"+str(0)
            scoreboard.add_score(score)
            scoreboard.write_to_file()
            the_wind_rises_theme.fadeout(1000)
            return "game_over"
        gf.update_screen(mg_settings, map_, screen, player,curr_maze)

        #Blit Counter
        if not timer.pause:
            timer.update()
        width = 200
        height = 50
        timer_image = Button(screen, str(timer.time_remaining/1000),'white','white','black',width,height,(screen.get_rect().topleft[0]+width/2,screen.get_rect().topleft[1]+height/2))
        timer_image.draw_button()

        #Show score
        scoreboard.update_score(player,curr_maze, mg_settings.end_point)
        score = scoreboard.curr_score
        score_image = Button(screen, str(score),'white','white','black',width,height,(screen.get_rect().topleft[0]+width/2,screen.get_rect().topleft[1]+height*3/2))
        score_image.draw_button()


        pygame.display.update()
        # Make the most recently drawn screen visible.
        pygame.display.flip()
        
        #Check whether game is timed out
        if timer.check():
            score = str(datetime.datetime.now())+","+str(scoreboard.curr_score)+","+str(timer.time_elapsed/1000)+"s,"+str(1)
            scoreboard.add_score(score)
            scoreboard.write_to_file()
            the_wind_rises_theme.fadeout(1000)
            pygame.mixer.Sound('audio/punch-gaming-sound-effect-hd_RzlG1GE.mp3').play()
            return "timeout"
        
        clock.tick(120)