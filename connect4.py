import os
import random
def clear_screen():
    os.system('clear')

def validate_input(prompt, valid_inputs):
    while True:
        user_input = input(prompt)
        if user_input in valid_inputs:
            return user_input
        else:
            print("Invalid input, please try again.")

def create_board():
    board = [[0 for _ in range(8)] for _ in range(7)]  
    return board

def print_board(board):
    print("========== Connect4 =========")
    print("Player 1: X            Player 2: O")
    for row in range(1, len(board)):  
        for col in range(1, len(board[row])): 
            cell = board[row][col]
            if cell == 0:
                print("|---", end=" ")
            elif cell == 1:
                print("| X ", end=" ")
            elif cell == 2:
                print("| O ", end=" ")
        print("|")
    print("=============================")

def drop_piece(board, player, col):
    row = len(board)-1
    while row >= 1:  
        if board[row][col] == 0:
            board[row][col] = player
            return True
        row -= 1
    return False

def execute_player_turn(player, board):
    while True:
        user_input = validate_input(f"Player {player}, please enter the column you would like to drop your piece into ",
                                    ["1", "2", "3", "4", "5", "6", "7"])
        bol = drop_piece(board, player, int(user_input))
        if bol == True:
            print("ok")
            break
        else:
            print("column is full")

def end_game(board):
    for row in range(1, len(board) - 3): 
        for col in range(1, len(board[row])):
            if all(board[row + i][col] == 1 for i in range(4)):
                return 1  
            elif all(board[row + i][col] == 2 for i in range(4)):
                return 2 

    for row in range(1, len(board)):
        for col in range(1, len(board[row]) - 3):  
            if all(board[row][col + i] == 1 for i in range(4)):
                return 1  
            elif all(board[row][col + i] == 2 for i in range(4)):
                return 2  

    for row in range(1, len(board) - 3): 
        for col in range(1, len(board[row]) - 3): 
            if all(board[row + i][col + i] == 1 for i in range(4)):
                return 1  
            elif all(board[row + i][col + i] == 2 for i in range(4)):
                return 2  

    for row in range(1, len(board) - 3):  
        for col in range(4, len(board[row])):
            if all(board[row + i][col - i] == 1 for i in range(4)):
                return 1  
            elif all(board[row + i][col - i] == 2 for i in range(4)):
                return 2  

    for row in board:
        if 0 not in row:
            return 3
    return 0  # No win found

def localgame():
    player = 1
    board = create_board()
    while True:
        clear_screen()
        print_board(board)
        execute_player_turn(player, board)

        result = end_game(board)

        if result == 1:
            print("Player 1 win ")
            input()
            break
        elif result == 2:
            print("Player 2 win ")
            input()
            break
        elif result == 3:
            print("Draw")
            input()
            break

        if player == 1:
            player = 2
        elif player == 2:
            player = 1

def view_rules():
    print('''Connect4 Game Rules:
1. Connect4 is a two-player board game played on a 6x7 grid.
2. Players take turns dropping their colored tokens into a column.
3. Tokens fall to the lowest available empty cell in the chosen column.
4. The objective is to connect four of your tokens in a row, column, or diagonal.
5. The first player to achieve four in a row wins the game.
6. If the board is filled without a winner, the game is a draw.''')
    input("\nPress Enter to return to the main menu.")

def cpu_player_easy():
    player=1
    board=create_board()
    while True:
        print_board(board)
        execute_player_turn(player,board)
        drop_piece(board,2,random.randint(1, 7))
        result=end_game(board)
        if result == 1:
            print("Player 1 win ")
            print_board(board)
            input()
            break
        elif result == 2:
            print("cpu win ")
            print_board(board)
            input()
            break
        elif result == 3:
            print("Draw")
            input()
            break
        clear_screen()


def cpu_player_medium():
    player = 1
    board = create_board()

    while True:
        result = end_game(board)
        if result == 1:
            print("Player 1 wins!")
            print_board(board)
            input()
            break
        elif result == 2:
            print("CPU wins!")
            print_board(board)
            input()
            break
        elif result == 3:
            print("Draw")
            print_board(board)
            input()
            break
        print_board(board)
        execute_player_turn(player, board)
        cpu_move = None
        for col in range(1, 8):
            temp_board = [row[:] for row in board]
            if drop_piece(temp_board, 2, col):
                if end_game(temp_board) == 2:
                    cpu_move = col
                    break
                temp_board_copy = [row[:] for row in temp_board]
                if drop_piece(temp_board_copy, player, col) and end_game(temp_board_copy) == 1:
                    cpu_move = col
                    break
        if cpu_move is None:
            for col in range(1, 8):
                temp_board = [row[:] for row in board]
                if drop_piece(temp_board, player, col) and end_game(temp_board) == 1:
                    cpu_move = col
                    break
        if cpu_move is None:
            cpu_move = random.randint(1, 7)
        drop_piece(board, 2, cpu_move)








def main():
    while True:
        clear_screen()
        print("Welcome to the Connect4 Game!")
        print("1. View Rules")
        print("2. Play a Local 2-Player Game")
        print("3. Play easy against Computer")
        print("4. play medium against computer" )
        print("5. Exit")

        choice = validate_input("Select an option: ", ["1", "2", "3", "4"])

        if choice == "1":
            view_rules()
        elif choice == "2":
            localgame()
        elif choice == "3":
            cpu_player_easy()
        elif choice == "4":
            cpu_player_medium()
        elif choice == "5":
            clear_screen()
            print("Exiting the program.")
            break
        else:
            input("Invalid choice! Press Enter to continue.")


main()
