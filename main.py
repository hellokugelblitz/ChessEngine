import pygame
from pygame.locals import *

pygame.init()
pygame.display.set_caption('Chess Engine :)')

screen = pygame.display.set_mode((480,480))



def mainLoop():
    board = Board()
    board.peice_setup("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
    running = True


    while running:
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        board.draw_board()

        draw_peice(Peice.knight,Peice.black, 0)



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
        

        
        
        

    def peice_setup(self, fen):
        #Starts from top left, lowercase = black, uppercase = white, / = new line
        #rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1
        
        fen_board = fen.split(' ', 1)
        fen = fen_board[0]

        peice_dict = {
            'p': Peice.pawn,
            'b': Peice.bishop,
            'n': Peice.knight,
            'r': Peice.rook,
            'q': Peice.queen,
            'k': Peice.king,
        }

        char_fen = list(fen)
        print(char_fen)


        for character in range(0,len(char_fen)):
            crnt_char = char_fen[character]
            
            if crnt_char == '/':
                character

        file = 0
        rank = 0

        for character in fen:
            if character == '/':
                file = 0
                rank += 1
                continue
            
            if character.isnumeric():
                spaces = int(character)
                file += spaces
                continue

            peice = peice_dict[character.lower()]
            peice_color = 8 if str. isupper(character) else 16
            self.squares[rank*8+file] = peice | peice_color
            file += 1
        

        #self.squares[63] = Peice.pawn | Peice.black

        #print(self.squares)
        print_board(self.squares,8)
    
class Peice():
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


def print_board(board,rowsize):
    print()
    print("Current game board: ")
    for file in range(0,rowsize):
        for rank in range(0,rowsize):
            print(board[(file*8)+rank], end=" ")
        print()

def draw_peice(peice_3bits,color_num, index):

    peice_num = peice_3bits | color_num

    peice_dict = {
            20: 'images/bRook.png',
            19: 'images/bKnight.png',
            18: 'images/bBishop.png',
            21: 'images/bQueen.png',
            22: 'images/bKing.png',
            17: 'images/bPawn.png',
             9:  'images/wPawn.png',
            12: 'images/wRook.png',
            11: 'images/wKnight.png',
            10: 'images/wBishop.png',
            13: 'images/wKing.png',
            14: 'images/wQueen.png',
    }

    peice = pygame.image.load(peice_dict[peice_num])
    peice = pygame.transform.scale(peice, (60, 60))
    screen.blit(peice, (0,0,30,30))

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