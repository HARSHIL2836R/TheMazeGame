"""
Module to store methods to update the game_screen UI
"""
import pygame
import datetime

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
    if not mg_settings.is_muted:
        pygame.mixer.music.load('audio/caproni.mp3')  
        pygame.mixer.music.play(loops=-1,fade_ms=1000)  

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
            if not mg_settings.is_muted:
                pygame.mixer.music.fadeout(1000)
            return "game_over"
        elif event_check_out == "player_died":
            scoreboard.update_score(player,curr_maze,mg_settings.end_point, timer)
            score = str(datetime.datetime.now())+","+str(scoreboard.curr_score)+","+"{0:.5}".format(str(timer.time_elapsed/1000))+"s,"+str(2)
            scoreboard.add_score(score)
            scoreboard.write_to_file()
            if not mg_settings.is_muted:
                pygame.mixer.music.fadeout(1000)
            return "game_over"
        gf.update_screen(mg_settings, map_, screen, player,curr_maze,enemies)

        global FRAME
        for enemy in enemies:
            if FRAME%3 == 0:
                enemy.move()
        FRAME+=1
        
        gs_settings = mg_settings.GameScreen()
        bt_color = gs_settings.bt_color
        text_color = gs_settings.text_color
        #Blit Counter
        if not timer.pause:
            timer.update()
        width = 200
        height = 55
        timer_image = Button(screen, "{0:^4.5}".format(str(timer.time_remaining/1000)),bt_color,bt_color,text_color,width,height,(screen.get_rect().topleft[0]+width/2,screen.get_rect().topleft[1]+height/2))
        timer_image.draw_button()

        #Show score
        scoreboard.update_score(player,curr_maze, mg_settings.end_point, timer)
        score = scoreboard.curr_score
        score_image = Button(screen, str(score),bt_color,bt_color,text_color,width,height,(screen.get_rect().topleft[0]+width/2,screen.get_rect().topleft[1]+height*3/2))
        score_image.draw_button()

        #Show Lives
        heart_width = 50
        def draw_hearts_at(x,y):
            lives_image = Button(screen, str(player.lives),mg_settings.bg_color,mg_settings.bg_color,text_color,width,height,(x,y))
            lives_image.hearts()
        if player.lives == 1:
            draw_hearts_at(screen.get_rect().topright[0]-heart_width,screen.get_rect().topright[1]+5)
        if player.lives == 2:
            draw_hearts_at(screen.get_rect().topright[0]-heart_width,screen.get_rect().topright[1]+5)
            draw_hearts_at(screen.get_rect().topright[0]-2*heart_width,screen.get_rect().topright[1]+5)
        if player.lives == 3:
            draw_hearts_at(screen.get_rect().topright[0]-heart_width,screen.get_rect().topright[1]+5)
            draw_hearts_at(screen.get_rect().topright[0]-2*heart_width,screen.get_rect().topright[1]+5)
            draw_hearts_at(screen.get_rect().topright[0]-3*heart_width,screen.get_rect().topright[1]+5)

        pygame.display.update()
        # Make the most recently drawn screen visible.
        pygame.display.flip()
        
        #Check whether game is timed out
        if timer.check():
            score = str(datetime.datetime.now())+","+str(scoreboard.curr_score)+","+"{0:.5}".format(str(timer.time_elapsed/1000))+"s,"+str(1)
            scoreboard.add_score(score)
            scoreboard.write_to_file()
            if not mg_settings.is_muted:
                pygame.mixer.music.fadeout(1000)
                pygame.mixer.Sound('audio/punch-gaming-sound-effect-hd_RzlG1GE.mp3').play()
            return "timeout"
        
        clock.tick(20)