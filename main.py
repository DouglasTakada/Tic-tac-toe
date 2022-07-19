from random import randrange


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print("+-------+-------+-------+\n|       |       |       |\n|   "+str(board[0][0])+"   |   "+str(board[0][1])+"   |   "+str(board[0][2])+"   |\n|       |       |       |\n+-------+-------+-------+\n|       |       |       |\n|   "+str(board[1][0])+"   |   "+str(board[1][1])+"   |   "+str(board[1][2])+"   |\n|       |       |       |\n+-------+-------+-------+\n|       |       |       |\n|   "+str(board[2][0])+"   |   "+str(board[2][1])+"   |   "+str(board[2][2])+"   |\n|       |       |       |\n+-------+-------+-------+")


def enter_move(board, dictionary):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.
    while True:
        user = int(input("Enter your move: "))
        if user >=10 or user<1:
            print("Choose a number between 1 and 9\n")
            continue
        elif user not in dictionary:
            print("That slot is already occupied. Try again")
            continue

        return user


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True  # checks diagonal
    if board[0][2] == sign and board[1][1] == sign and board[0][2] == sign:
        return True  # checks other diagonal
    for row in range(3):
        if board[row][0] == sign and board[row][1] == sign and board[row][2] == sign:
            return True  # checks rows
        if board[0][row] == sign and board[1][row] == sign and board[2][row] == sign:
            return True  # checks columns

    return False


def draw_move(board,dictionary):
    # The function draws the computer's move and updates the board.
    while True:
        comp = randrange(10)
        if comp in dictionary:
            break

    return comp


victory = False
turn = 1
board = [[1,2,3],[4,'X',6],[7,8,9]]
dictionary = {1:(0,0), 2:(0,1), 3:(0,2), 4:(1,0), 6:(1,2), 7:(2,0), 8:(2,1), 9:(2,2)}

print("The computer went first")

while turn != 9 or victory != True:
    turn += 1
    display_board(board)
    user = enter_move(board,dictionary)
    board[dictionary[user][0]][dictionary[user][1]] = 'O'
    del dictionary[user]
    victory = victory_for(board, 'O')
    if victory:
        display_board(board)
        print("Congrats you won!")
        break
    comp = draw_move(board, dictionary)
    board[dictionary[comp][0]][dictionary[comp][1]] = 'X'
    victory = victory_for(board, 'X')
    if victory:
        display_board(board)
        print("You lost!")
        break

    del dictionary[comp]

wait = input("Press Enter to Exit")