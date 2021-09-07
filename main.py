import pygame
from pygame.locals import *

pygame.init()
pygame.display.set_caption('Chess Engine :)')

screen = pygame.display.set_mode((480,480))



def mainLoop():
    board = Board()

    running = True
    while running:
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        board.draw_board()

        # Draw a solid blue circle in the center
        #pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

        # Flip the display
        pygame.display.flip()


class Board():
    dark_color = (195,160,130)
    light_color = (242,225,195)

    #
    squares = [0] * 64

    def __init__(self):
        dark_color = (50,50,50)
        light_color = (200,200,200)

    def draw_board(self):
        screen.fill(self.light_color)
        
        for file in range(0,8):
            for rank in range(0,8):
                if (file+rank)%2 != 0:
                    pygame.draw.rect(screen, self.dark_color,  pygame.Rect(file*60, rank*60, 60, 60))

        pygame.display.flip()

    def peice_setup(fen):
        #Starts from top left, lowercase = black, uppercase = white, / = new line
        #rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1
        

        print("board setup")
    

class Peice(pygame.sprite.Sprite):
    
    #0 - nothing
    #1 - pawn
    #2 - bishop
    #3 - knight
    #4 - rook
    #5 - queen
    #6 - king
    #8 - white
    #16 - black

    nothing = 0
    pawn = 1
    bishop = 2
    knight = 3
    rook = 4
    queen = 5
    king = 6
    white = 8
    black = 16

    peice_number = 0
    
    def __init__(self, peice_number):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.peice_number = peice_number




"""
#This function takes the name of an image to load. It also optionally takes an argument it can use to set a colorkey for the image. A colorkey is used in graphics to represent a color of the image that is transparent.
def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

#Next is the function to load a sound file. The first thing this function does is check to see if the pygame.mixerpygame module for loading and playing sounds module was imported correctly. If not, it returns a small class instance that has a dummy play method. 
def load_sound(name):
    class NoneSound:
        def play(self): pass
    if not pygame.mixer:
        return NoneSound()
    fullname = os.path.join('data', name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error as message:
        print('Cannot load sound:', fullname)
        raise SystemExit(message)
    return sound
"""

def main():
    mainLoop()

main()


# Done! Time to quit.
pygame.quit()