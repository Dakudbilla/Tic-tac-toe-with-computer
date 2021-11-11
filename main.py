from player import HumanPlayer,RandomComputerPlayer
from game import TicTacToe,play

if __name__=='__main__':
    o_player=RandomComputerPlayer('O')
    x_player=HumanPlayer('X')
    tic_tac_toe=TicTacToe()
    play(tic_tac_toe,x_player,o_player)