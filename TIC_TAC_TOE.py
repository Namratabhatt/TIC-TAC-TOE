#board
board=['-','-','-',
       '-','-','-',
       '-','-','-']

player='X'
game_on=True
winner=None

#display board
def display_board():
    print(board[0],'|',board[1],'|',board[2],'\t','1 | 2 | 3')
    print(board[3],'|',board[4],'|',board[5],'\t','4 | 5 | 6')
    print(board[6],'|',board[7],'|',board[8],'\t','7 | 8 | 9')

#handle turn
def handle_turn(player):
    print(player+"'s turn")
    #ask for input
    position=input("Enter the position(1-9):")

    valid=False
    while not valid:
        while position not in ['1','2','3','4','5','6','7','8','9']:
            position=input("Enter the position(1-9):")
        position=int(position)-1

        if board[position]=="-":
            valid=True
        else:
            print("you cant go there!!")  
    board[position]=player
    display_board()

def check_row():
    global game_on
    row1=board[0]==board[1]==board[2]!='-'
    row2=board[3]==board[4]==board[5]!='-'
    row3=board[6]==board[7]==board[8]!='-'
    if row1 or row2 or row3:
        game_on=False
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    return

def check_column():
    global game_on
    col1=board[0]==board[3]==board[6]!='-'
    col2=board[1]==board[4]==board[7]!='-'
    col3=board[2]==board[5]==board[8]!='-'
    if col1 or col2 or col3:
        game_on=False
    if col1:
        return board[0]
    elif col2:
        return board[1]
    elif col3:
        return board[2]
    return

def check_diagonal():
    global game_on
    dia1=board[0]==board[4]==board[8]!='-'
    dia2=board[2]==board[4]==board[6]!='-'
    if dia1 or dia2:
        game_on=False
    if dia1:
        return board[0]
    elif dia2:
        return board[2]
    return

def check_for_winner():
    global winner
    rwinner=check_row()
    cwinner=check_column()
    dwinner=check_diagonal()

    if rwinner:
        winner=rwinner
    elif cwinner:
        winner=cwinner
    elif dwinner:
        winner=dwinner
    else:
        winner=None
    return

def check_if_tie():
    global game_on
    if '-' not in board:
        game_on=False
    return

def flip_turn():
    global player
    if player=='X':
        player='O'
    elif player=='O':
        player='X'



#play game
def playgame():
    print("WELCOME TO TIC TAC TOE GAME")
    display_board()

    while game_on:

        handle_turn(player)
        check_for_winner()
        check_if_tie()
        flip_turn()

    if winner=='X' or winner=='O':
        print(winner+' won.')
    else:
        print('Tie.')

playgame()