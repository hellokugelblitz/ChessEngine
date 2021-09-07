import pygame
from pygame.locals import *

pygame.init()
pygame.display.set_caption('Chess Engine :)')

screen = pygame.display.set_mode((480,480))

def main_loop():
    board = Board()
    board.peice_setup("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
    running = True

    while running:
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        board.draw_board()
        handleMouse()

        count = 0
        for square in board.squares:
            draw_peice(square, count)
            count += 1

        # Draw a solid blue circle in the center
        #pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

        # Flip the display
        pygame.display.flip()

class Board():
    dark_color = (195,160,130)
    light_color = (242,225,195)

    #
    squares = [0] * 64

    file_letters = {
        1 : 'a',
        2 : 'b',
        3 : 'c',
        4 : 'd',
        5 : 'e',
        6 : 'f',
        7 : 'g',
        8 : 'h'
    }

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

    peice_dict = {
        20: 'images/bRook.png',
        19: 'images/bKnight.png',
        18: 'images/bBishop.png',
        21: 'images/bKing.png',
        22: 'images/bQueen.png',
        17: 'images/bPawn.png',
         9:  'images/wPawn.png',
        12: 'images/wRook.png',
        11: 'images/wKnight.png',
        10: 'images/wBishop.png',
        13: 'images/wKing.png',
        14: 'images/wQueen.png',
        0:  'none'
    }

def print_board(board,rowsize):
    print()
    print("Current game board: ")
    for file in range(0,rowsize):
        for rank in range(0,rowsize):
            print(board[(file*8)+rank], end=" ")
        print()

def draw_peice(peice_3bits,color_num, index):

    peice_num = peice_3bits | color_num

    file = int(index/8)
    rank = int(index%8)

    if peice_num != 0:
        peice = pygame.image.load(Peice.peice_dict[peice_num])
        peice = pygame.transform.scale(peice, (60, 60))
        screen.blit(peice, (60*rank,60*file,30,30))

def draw_peice(peice_num, index):

    file = int(index/8)
    rank = int(index%8)

    if peice_num != 0:
        peice = pygame.image.load(Peice.peice_dict[peice_num])
        peice = pygame.transform.scale(peice, (60, 60))
        screen.blit(peice, (60*rank,60*file,30,30))

def handleMouse():
    #Useful :)
    mouseX = pygame.mouse.get_pos()[0]
    mouseY = pygame.mouse.get_pos()[1]

    #Yellow mouseb box
    if(pygame.mouse.get_focused() != False): 
        transparent_rect(60*int(mouseX/60),60*int(mouseY/60),60,60,(255,255,0),128)

    if pygame.mouse.get_pressed() == (1, 0, 0):
        rank = int(mouseY/60) + 1
        file = int(mouseX/60) + 1
        index = (8*rank) + file - 9
        print("click info -> file: ", Board.file_letters[file]," rank: ", int(translate(rank,8,1,1,8))," index: ", index)
        
        if(Board.squares[index] != 0):
            print("square taken")
        else:
            print("square not taken")

#Method for revere mapping arrays of values.
def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)

#Pygame does not have a way to easily make transparent squares, this is my solution.
def transparent_rect(x,y,w,h,color,alpha):
    s = pygame.Surface((w,h))  # the size of your rect
    s.set_alpha(alpha)                # alpha level
    s.fill(color)           # this fills the entire surface
    screen.blit(s, (x,y))




#Call main loop
main_loop()

# Done! Time to quit.
pygame.quit()