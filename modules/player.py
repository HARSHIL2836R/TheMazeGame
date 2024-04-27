'''Module to store the class Player, children of pygame.sprite.Sprite class containing all information of the player running in the maze (or say a pegion flying in the sky-top maze :) )'''
import pygame

#My Modules
from modules.maze_logic.maze import Maze

class Player(pygame.sprite.Sprite):

    def __init__(self, screen: pygame.Surface, the_maze: Maze):
        """
        Initialise the player
        The properties initialised are:
        Parent class (Sprite) properties, Surface on which player's rect is present, Images of the surface of player, Rect values of the player, Rect values of the Screen, Maze in which the player is present, (ndarray) Matrix of the Maze, Position of the player (Coordinates(x,y))
        """ 
        super().__init__()

        #Load the player image and get it's rectangular representation
        self.screen = screen
        self.right_face = pygame.image.load('images/player_right.png')
        self.left_face = pygame.image.load('images/player_left.png')
        self.image = self.right_face
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.the_maze = the_maze
        self.maze = the_maze.mazrix

        #Start player at center of left edge
        self.rect.topleft = self.screen_rect.topleft
        self.pos=(0,0)

        self.lives = 3
    
    def bltime(self)->None:
        """
        Draws the player at it's current position
        """
        self.screen.blit(pygame.transform.scale(self.image,(self.width,self.height)), self.rect)
    
    def set_dim(self, width:int,height:int)->None:
        """
        Sets the dimensions of the Rect of the player and adds width and height as property of the object
        """
        self.width = width
        self.height = height
        self.right_face = pygame.transform.scale(self.right_face,(self.width,self.height))
        self.left_face = pygame.transform.scale(self.left_face,(self.width,self.height))
        self.image = pygame.transform.scale(self.image,(self.width,self.height))

    def move(self, x: int =0,y: int =0)->bool:
        """
        Move player by x pixels right and y pixels up
        Args:
            x: int, pixels right
            y: int, pixels up
        Returns:
            bool: False is player was unable to move due to an Obstacle, True otherwise
        """
        new_rect = pygame.Rect(self.rect)
        new_rect.x = self.rect.x + x
        new_rect.y = self.rect.y + y
        #new_rect = (self.rect[0] + x,self.rect[1]+y,self.rect[2],self.rect[3])
        new_pos = (int(self.pos[0]+x/self.width),int(self.pos[1]+y//self.height))
        #if (0<=new_rect[0]<self.screen.get_width() and 0<=new_rect[1]<self.screen.get_height() and self.maze[new_pos[1],new_pos[0]] != -1):
        if (self.maze[new_pos[1],new_pos[0]] != -1):
            self.rect = new_rect
            self.pos = new_pos
            return True

        #If not moving, return False
        return False

class Enemy(Player):
    def __init__(self, player: Player, pos: tuple):
        super().__init__(player.screen, player.the_maze)
        self.image = pygame.image.load('images/player_old.png')
        self.right_face = self.image
        self.left_face = self.image
        self.set_dim(player.width,player.height)

        self.rect.topleft = (pos[0]*self.width,pos[1]*self.height)

        self.die = False