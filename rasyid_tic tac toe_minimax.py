
from tkinter import *
from tkinter import messagebox



board = [" " for _ in range(9)]
player_turn = "O"
game_over = False

winning_combinations = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
    [0, 4, 8], [2, 4, 6]  # Diagonals
]




window = Tk()
window.title("Tic-Tac-Toe")
window.config(background="lightblue")
window.resizable(FALSE, FALSE)




def check_win(board, player):
    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False




def check_draw(board):
    return " " not in board




def make_move(button, index):
    global player_turn, game_over

    if board[index] == " " and not game_over:
        board[index] = player_turn
        button.config(text=player_turn, state=DISABLED)
        if check_win(board, player_turn):
            messagebox.showinfo("Game Over", f"Player {player_turn} wins!")
            game_over = True
        elif check_draw(board):
            messagebox.showinfo("Game Over", "It's a draw!")
            game_over = True
        else:
            player_turn = "O" if player_turn == "X" else "X"
            if player_turn == "X":
                computer_move()




def computer_move():
    best_move = -1
    best_score = -float('inf')
    for move in range(len(board)):
        if board[move] == " ":
            board[move] = "X"
            score = minimax(board, 0, False)
            board[move] = " "
            if score > best_score:
                best_score = score
                best_move = move

    buttons[best_move].config(text="X", state=DISABLED)
    board[best_move] = "X"
    global player_turn
    player_turn = "O"
    if check_win(board, "X"):
        messagebox.showinfo("Game Over", "Computer wins!")
    elif check_draw(board):
        messagebox.showinfo("Game Over", "It's a draw!")




def minimax(board, depth, is_maximizing):
    if check_win(board, "X"):
        return 1
    elif check_win(board, "O"):
        return -1
    elif check_draw(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for move in range(len(board)):
            if board[move] == " ":
                board[move] = "X"
                score = minimax(board, depth + 1, False)
                board[move] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for move in range(len(board)):
            if board[move] == " ":
                board[move] = "O"
                score = minimax(board, depth + 1, True)
                board[move] = " "
                best_score = min(score, best_score)
        return best_score




def reset_game():
    global board, game_over, player_turn
    board = [" " for _ in range(9)]
    game_over = False
    player_turn = "O"

    # Clear the button text and re-enable buttons
    for button in buttons:
        button.config(text=" ", state=NORMAL)




buttons = []
for i in range(9):
    row, col = i // 3, i % 3
    button = Button(window, text=" ", font="Normal 60", relief=RIDGE, bd=5, activebackground="blue", width=3,
                      command=lambda i=i: make_move(buttons[i], i))
    button.grid(row=row, column=col, padx=10, pady=10)
    buttons.append(button)

# Start the game
menubar = Menu(window, tearoff=False)
window.config(menu=menubar)
menubar.add_command(label="Reset", command=reset_game)


window.mainloop()
