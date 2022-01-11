def main():

    board = [[None for _ in range(3)] for _ in range(3)]
    n = 1
    for i, row in enumerate(board):
        for j, _ in enumerate(row):
            board[i][j] = n
            n += 1

    print("Welcome to Tic-Tac-Toe. When you start playing, enter the position where you want to place your mark.")
    print()

    print_board(board)

    print()
    input("Press any key to start...")
    print()

    turn = 'x'

    # Game starts
    while True:
        
        position = int(input(f"{turn}'s turn to choose a square (1-9): "))
        x, y = get_coordinate(position)             # Get the coordinates of the board by the position

        # Check if the position claimed is free
        pos = board[y][x]
        if pos != 'x' and pos != 'o':
            board[y][x] = turn                      # Set the board

            result = check_game_condition(board)
            if result:
                print(f"{result} has won the game. Congratulations!")
                print()
                print_board(board)
                print()
                break
            
            if check_tie(board):
                print("The game ended in a tie. There are no more free spaces.")
                print()
                print_board(board)
                print()
                break

            turn = 'x' if turn == 'o' else 'o'      # Change the player's turn

        else:
            print("That position is claimed. Please select another one.")
        
        print()
        print_board(board)
        print()

def check_game_condition(board : list) -> str:
    '''
    Checks the game board and returns
    the winner of the game.
    '''
    
    # All possible winning combinations
    combinations = [
        board[0],
        board[1],
        board[2],
        [row[0] for row in board],
        [row[1] for row in board],
        [row[2] for row in board],
        [row[i] for i, row in enumerate(board)],
        [row[2 - i] for i, row in enumerate(board)]
    ]

    for combination in combinations:
        if combination.count('x') == 3:
            return 'x'
        elif combination.count('o') == 3:
            return 'o'
    
    return None


def get_coordinate(position : int) -> tuple:
    """
    Gets the x and y value of the position
    given by the player.
    """
    x = 0
    y = 0
    aux = position

    while True:
        aux = aux - 3
        if aux > 0:
            y += 1
        else:
            x = aux + 2
            break

    return (x, y)


def print_board(board : list) -> None:
    """
    Prints the full content of the board
    with the proper format.
    """

    for row in board:
        print(f" {row[0]} | {row[1]} | {row[2]}")
        print("---+---+---")


def check_tie(board : list) -> bool:
    """
    Check if the current board ended in a tie.
    """

    for row in (board):
        for col in (row):
            if col != 'x' and col != 'o':
                return False

    return True


if __name__ == '__main__':
    main()