# TIC-TAC-TOE V1 by Sreeharsha Raveendra

import random   # for random number generation
import sys      # for exit function
import os       # for clearing terminal screen
import time     # for time delay

class Player:
    def __init__(self, play_char):
        self.play_char = play_char
        self.turns = 0
        self.score = 0

    def get_play_char(self):
        # function to get the player character
        return self.play_char
    
    def add_score(self):
        # function to increment player score
        self.score += 1
        return

class GamePlay:
    def __init__(self):
        self.game_pos = {key: ' ' for key in range (1,10)}    # dictionary to hold player positions on game board
        self.draws = 0              # keep track of draws
        self.player1 = None         # player to play 1st
        self.player2 = None         # player to play 2nd
        self.winner = None          # winner of the game
        self.current_player = None  # which player is playing currently?
        self.game_running = True    # status of game running/not running
        self.print_intro()
        self.print_options()

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
        return
    
    def print_options(self):
        # function to print the introductory options
        print("                                                                                        ")
        print("                                      a> Play Game                                      ")
        print("                                      b> Quit Game                                      ")
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
        print("       ----------- \n")
        return

    def set_players(self, p1, p2):
        # function to set player instances
        self.player1 = Player(p1)
        self.player2 = Player(p2)
        return
    
    def set_current_player(self):
        # function to set current player
        self.current_player = self.player1
        return
    
    def display_score(self):
        # function to display score:
        if (self.player1.play_char == 'X'):
            print(f"\nSCORE:\n  Player X = {self.player1.score}\n  Player O = {self.player2.score}\n  Draws: {self.draws}\n\n")
        else:
            print(f"\nSCORE:\n  Player X = {self.player2.score}\n  Player O = {self.player1.score}\n  Draws: {self.draws}\n\n")
        return

    def game_board(self):
        # function to show tic tac toe board positions
        print("       --- --- --- ")
        print(f"      | {self.game_pos[1]} | {self.game_pos[2]} | {self.game_pos[3]} |")
        print("      |---|---|---|")
        print(f"      | {self.game_pos[4]} | {self.game_pos[5]} | {self.game_pos[6]} |")
        print("      |---|---|---|")
        print(f"      | {self.game_pos[7]} | {self.game_pos[8]} | {self.game_pos[9]} |")
        print("       ----------- ")
        return
    
    def player_input(self):
        # function to take player input
        print(f"\n  it's Player {self.current_player.get_play_char()}'s turn  ")
        inp_pos = int(input("Enter an empty position number 1-9: "))
        while (inp_pos not in range(1,10)) or (self.game_pos[inp_pos] != ' '):
            print("INVALID INPUT")
            inp_pos = int(input("Again, enter an empty position number 1-9: "))
        
        self.game_pos[inp_pos] = self.current_player.get_play_char()  # set player on game board
        return
    
    def check_row(self):
        # function to check if row of game board is matching
        if self.game_pos[1] == self.game_pos[2] == self.game_pos[3] and self.game_pos[2] != ' ':
            self.winner = self.game_pos[1]
            return True
        elif self.game_pos[4] == self.game_pos[5] == self.game_pos[6] and self.game_pos[5] != ' ':
            self.winner = self.game_pos[4]
            return True
        elif self.game_pos[7] == self.game_pos[8] == self.game_pos[9] and self.game_pos[8] != ' ':
            self.winner = self.game_pos[7]
            return True 
        else:
            return False
        
    def check_column(self):
        # function to check if column of game board is matching
        if self.game_pos[1] == self.game_pos[4] == self.game_pos[7] and self.game_pos[4] != ' ':
            self.winner = self.game_pos[1]
            return True
        elif self.game_pos[2] == self.game_pos[5] == self.game_pos[8] and self.game_pos[5] != ' ':
            self.winner = self.game_pos[2]
            return True
        elif self.game_pos[3] == self.game_pos[6] == self.game_pos[9] and self.game_pos[6] != ' ':
            self.winner = self.game_pos[3]
            return True
        else:
            return False
        
    def check_diagonal(self):
        # function to check if diagonal of game board is matching
        if self.game_pos[1] == self.game_pos[5] == self.game_pos[9] and self.game_pos[5] != ' ':
            self.winner = self.game_pos[1]
            return True
        elif self.game_pos[3] == self.game_pos[5] == self.game_pos[7] and self.game_pos[5] != ' ':
            self.winner = self.game_pos[3]
            return True
        else:
            return False
        
    def check_tie(self):
        # function to check if game board is tied
        if ' ' not in self.game_pos.values():
            print("\n IT'S A TIE! \n")
            self.draws += 1
            self.game_running = False
            return True
        else:
            return False
    
    def check_win(self):
        # function to check if game is won
        if self.check_row() or self.check_column() or self.check_diagonal():
            print(f"   Player {self.winner} has won!   ")
            if  self.winner == self.player1.get_play_char():
                self.player1.add_score()
            else:
                self.player2.add_score()
            self.game_running = False
        else:
            return
        
    def switch_player(self):
        # function to switch current player
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1
        return
    
    def rematch(self):
        # function to handle rematch
        query = input("Do you want a rematch Y/N? ").upper()
        while query not in ['Y', 'N']:
            print("INVALID INPUT")
            query = input("Do you want a rematch Y/N? ").upper()
        
        if query == 'N':
            self.quit_game()
        else:
            # reset game board
            self.game_pos.clear()
            self.game_pos = {key: ' ' for key in range (1,10)}
            self.game_running = True
    
    def play_game(self):
    # function to handle the logic of playing the game Tic Tac Toe
        os.system('cls' if os.name == 'nt' else 'clear')    # clear terminal screen
        self.print_intro()  # display intro board
        self.display_score()    # display initial score
        self.demo_board()   # demo board for reference of game board positions
        self.game_board()   # actual board
        self.player_input() # take player input
        self.game_board()
        self.check_win()
        self.check_tie()
        self.switch_player()

        if self.game_running == False:
            print("   GAME HAS ENDED   ")
            self.display_score()    # display score after game
            self.rematch()
        return

    def quit_game(self):
        # function to exit out of the game
        print("\n QUITTING GAME \n")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')    # clear terminal screen
        sys.exit()


if __name__ == '__main__':
    game1 = GamePlay()  # create game instance
    # input game option
    game_option = input("Choose option a or b: ").lower()
    while game_option not in ['a', 'b']:
        print("INVALID OPTION")
        print("")
        game_option = input("Choose option a or b: ").lower()

    # start and select play character
    if game_option == 'a':
        print("  Player O vs Player X")
        print("\n ...Random Coin Toss... \n")
        time.sleep(2)   # delay for 2 seconds
        if (random.randint(0,1) == 1):  # randomly decide who is going first
            game1.set_players('X', 'O') # set player instances in game
            print("    Player X goes first")
        else:
            game1.set_players('O', 'X') # set player instances in game
            print("    Player O goes first")
        game1.set_current_player()  # set current player
    else:
        game1.quit_game()
    time.sleep(1)   # delay for 1 second

    # start the game
    while True:
        game1.play_game()
