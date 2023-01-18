board = [1,2,3,4,5,6,7,8,9]
complex_board = [[1,2,3],[4,5,6],[7,8,9]]

play = True

def print_board(board):
    print(f'{board[0]} | {board[1]} | {board[2]}')
    print('-'*9)
    print(f'{board[3]} | {board[4]} | {board[5]}')
    print('-'*9)
    print(f'{board[6]} | {board[7]} | {board[8]}')

#def take_turn(player, spot, board):
    #work on this section to switch players and 

while play:
    print_board(board)
    
    #intiates a request from player
    update_brd = int(input('Player1 what position do you want to update?'))
    board[update_brd -1] = 'X'
    print_board(board)

    update_brd = int(input('Player2 what position do you want to update?'))
    board[update_brd -1] = 'O'
