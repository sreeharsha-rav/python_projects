# TIC-TAC-TOE V1 by Sreeharsha Raveendra

import random   # for random number generation

game_pos = {key: '' for key in range (1,10)}    # dictionary to hold player positions on game board

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
    print("                                                                                        ")

def coin_toss():
    # function to decide who goes first in 2 player mode
    pass

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
    pass

class GameBoard:
    pass


if __name__ == '__main__':
    print_intro()
    game_mode = input("Choose option a or b: ")
    
    if game_mode == 'a':
        print("  Player vs Computer")
        choice = input("  Do you want to be 'O' or 'X'? ")    # valid values 'O' and 'X'
    elif game_mode =='b':
        print("  Player O vs Player X")
        print("    Player X goes first") if (random.randint(0,1) == 1) else print("    Player O goes first")
    demo_board()
    pos = input("    Enter postion: ")