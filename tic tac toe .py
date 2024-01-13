def draw_board(board):
    print('-------------')
    for i in range(3):
        print('|', end=' ')
        for j in range(3):
            print(board[i][j], '|', end=' ')
        print('\n-------------')

# Example usage
board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]
def moving(row,col,symbol):
    board[row][col]=symbol
# Assigning variables to empty spaces
top_left = board[0][0]
top_center = board[0][1]
top_right = board[0][2]
middle_left = board[1][0]
middle_center = board[1][1]
middle_right = board[1][2]
bottom_left = board[2][0]
bottom_center = board[2][1]
bottom_right = board[2][2]

def check_win():
    for row in board:#row
        if row[0]==row[1]==row[2]!=' ':
            return  won
    for col in range(3):#column
        if board[0][col]==board[1][col]==board[2][col]!=" ":
            return won
            #diagonal
    if board[0][0]==board[1][1]==board[2][2]!=" ":
        return won
    if board[0][2]==board[1][1]==board[2][0]!=" ":
        return won
    else:
        return False
def draw():
    if row in board:
        if " "in board:
            return False
    return True
current_player="X"
while True:
    draw_board(board)
row=int(input("enter a row"))
column=int(input("enter a column"))
if board[row][col]!=" ":
    print("invalid")
    continue
moving(row,column,current_player)
if check_win():
    draw_board(board)
    print("player wins")
    break
elif draw():
    draw_board(board)
    print("draw")
    break
if current_player == 'X':
        current_player = 'O'
else:
        current_player = 'X'
