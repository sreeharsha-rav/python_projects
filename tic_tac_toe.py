# TIC-TAC-TOE V1 by Sreeharsha Raveendra

import random   # for random number generation
import sys      # for exit function

# positions that win the game
game_win = [(1, 2, 3),
            (4, 5, 6),
            (7, 8, 9),
            (1, 4, 7),
            (2, 5, 8),
            (3, 6, 9),
            (1, 5, 9),
            (3, 5, 7)]

def print_intro():
    # function to print the introductory terminal display
    print("########################################################################################")
    print("                                                                                        ")
    print(" TTTTTTT  IIIIIII  CCCCCCC     TTTTTTT     A      CCCCCCC     TTTTTTT  OOOOOOO  EEEEEEE ")
    print("    T        I     C              T       A A     C              T     O     O  E       ")
    print("    T        I     C              T      AAAAA    C              T     O     O  EEEEE   ")
    print("    T        I     C              T     A     A   C              T     O     O  E       ")
    print("    T     IIIIIII  CCCCCCC        T    A       A  CCCCCCC        T     OOOOOOO  EEEEEEE ")
    print("                                                                                        ")
    print("########################################################################################")
    print("                                                                                        ")
    print("                                      a> 1 Player                                       ")
    print("                                      b> 2 Player                                       ")
    print("                                      c> Exit                                           ")
    print("                                                                                        ")
    print("________________________________________________________________________________________")

def demo_board():
    # function to show tic tac toe board positions
    print("       --- --- --- ")
    print("      | 1 | 2 | 3 |")
    print("      |---|---|---|")
    print("      | 4 | 5 | 6 |")
    print("      |---|---|---|")
    print("      | 7 | 8 | 9 |")
    print("       ----------- ")

class Player:
    def __init__(self, play_char):
        self.play_char = play_char
        self.turns = 0
        self.g_pos = []

class GamePlay:
    def __init__(self):
        self.game_pos = {key: '' for key in range (1,10)}    # dictionary to hold player positions on game board
        self.game_mode = None
        self.print_intro()


    def print_intro(self):
        # function to print the introductory terminal display
        print("########################################################################################")
        print("                                                                                        ")
        print(" TTTTTTT  IIIIIII  CCCCCCC     TTTTTTT     A      CCCCCCC     TTTTTTT  OOOOOOO  EEEEEEE ")
        print("    T        I     C              T       A A     C              T     O     O  E       ")
        print("    T        I     C              T      AAAAA    C              T     O     O  EEEEE   ")
        print("    T        I     C              T     A     A   C              T     O     O  E       ")
        print("    T     IIIIIII  CCCCCCC        T    A       A  CCCCCCC        T     OOOOOOO  EEEEEEE ")
        print("                                                                                        ")
        print("########################################################################################")
        print("                                                                                        ")
        print("                                      a> 1 Player                                       ")
        print("                                      b> 2 Player                                       ")
        print("                                      c> Quit                                           ")
        print("                                                                                        ")
        print("________________________________________________________________________________________")
        return

    def demo_board(self):
        # function to show tic tac toe board positions
        print("       --- --- --- ")
        print("      | 1 | 2 | 3 |")
        print("      |---|---|---|")
        print("      | 4 | 5 | 6 |")
        print("      |---|---|---|")
        print("      | 7 | 8 | 9 |")
        print("       ----------- ")
        return

    def game_input(self):
        # function to take input for game option
        self.game_mode = input("Choose option a, b or c: ")
        while self.game_mode not in ['a', 'b', 'c']:
            print("INVALID OPTION")
            print("")
            self.game_mode = input("Choose option a, b or c: ")       
        return
    
    def game_option(self):
        # function to handle game option
        if self.game_mode == 'a':
            print("  Player vs Computer")
            play_char = input("  Do you want to be 'O' or 'X'? ")    # valid values 'O' and 'X'
            while play_char not in ['O', 'X']:
                print("  INVALID INPUT")
                play_char = input("  Do you want to be 'O' or 'X'? ")
            self.player = Player(play_char)
        
        elif self.game_mode == 'b':
            print("  Player O vs Player X")
            print("    Player X goes first") if (random.randint(0,1) == 1) else print("    Player O goes first")
        else:
            print(" QUITTING GAME ")
            sys.exit()
        return


game1 = GamePlay()
game1.game_input()
