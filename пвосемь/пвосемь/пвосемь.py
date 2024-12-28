import tkinter as tk
import random

# Определение игры
class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]  # Пустое поле
        self.game_over = False
        self.winner = None

    def print_board(self):
        for i in range(3):
            print("|".join(self.board[i*3:(i+1)*3]))
            if i < 2:
                print("-" * 5)

    def is_winner(self, player):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Горизонтальные
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Вертикальные
            [0, 4, 8], [2, 4, 6]  # Диагонали
        ]
        for condition in win_conditions:
            if all(self.board[i] == player for i in condition):
                return True
        return False

    def is_full(self):
        return " " not in self.board

    def make_move(self, position, player):
        if self.board[position] == " ":
            self.board[position] = player
            return True
        return False

    def reset(self):
        self.board = [" " for _ in range(9)]
        self.game_over = False
        self.winner = None


class TicTacToeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Крестики-Нолики")

        self.game = TicTacToe()
        self.player = "X"
        self.bot = "O"
        self.difficulty = "Easy"  # Легкий по умолчанию

        self.buttons = []
        self.create_widgets()

    def create_widgets(self):
        for i in range(9):
            button = tk.Button(self.root, text=" ", width=10, height=3, font=("Arial", 24), command=lambda i=i: self.player_move(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

        self.reset_button = tk.Button(self.root, text="Сбросить", width=10, height=3, command=self.reset_game)
        self.reset_button.grid(row=3, column=1)

        self.difficulty_button = tk.Button(self.root, text=f"Уровень: {self.difficulty}", width=10, height=3, command=self.toggle_difficulty)
        self.difficulty_button.grid(row=3, column=0)

    def toggle_difficulty(self):
        self.difficulty = "Hard" if self.difficulty == "Easy" else "Easy"
        self.difficulty_button.config(text=f"Уровень: {self.difficulty}")

    def player_move(self, position):
        if self.game.game_over or self.game.board[position] != " ":
            return
        self.game.make_move(position, self.player)
        self.update_board()
        if self.check_game_over():
            return
        self.bot_move()

    def bot_move(self):
        if self.game.game_over:
            return
        if self.difficulty == "Easy":
            self.easy_bot_move()
        else:
            self.hard_bot_move()

        self.update_board()
        self.check_game_over()

    def easy_bot_move(self):
        empty_positions = [i for i, x in enumerate(self.game.board) if x == " "]
        position = random.choice(empty_positions)
        self.game.make_move(position, self.bot)

    def hard_bot_move(self):
        best_move = self.minimax(self.game, self.bot)
        self.game.make_move(best_move, self.bot)

    def minimax(self, game, player):
        available_moves = [i for i, x in enumerate(game.board) if x == " "]
        if player == self.bot:
            best_score = -float('inf')
            best_move = None
            for move in available_moves:
                game.board[move] = self.bot
                score = self.minimax_score(game, False)
                game.board[move] = " "
                if score > best_score:
                    best_score = score
                    best_move = move
            return best_move
        else:
            best_score = float('inf')
            best_move = None
            for move in available_moves:
                game.board[move] = self.player
                score = self.minimax_score(game, True)
                game.board[move] = " "
                if score < best_score:
                    best_score = score
                    best_move = move
            return best_move

    def minimax_score(self, game, is_maximizing):
        if game.is_winner(self.bot):
            return 1
        elif game.is_winner(self.player):
            return -1
        elif game.is_full():
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for i in range(9):
                if game.board[i] == " ":
                    game.board[i] = self.bot
                    score = self.minimax_score(game, False)
                    game.board[i] = " "
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(9):
                if game.board[i] == " ":
                    game.board[i] = self.player
                    score = self.minimax_score(game, True)
                    game.board[i] = " "
                    best_score = min(score, best_score)
            return best_score

    def update_board(self):
        for i in range(9):
            self.buttons[i].config(text=self.game.board[i])

    def check_game_over(self):
        if self.game.is_winner(self.player):
            self.display_winner(self.player)
            return True
        elif self.game.is_winner(self.bot):
            self.display_winner(self.bot)
            return True
        elif self.game.is_full():
            self.display_winner("Draw")
            return True
        return False

    def display_winner(self, winner):
        if winner == "Draw":
            result = "Ничья!"
        else:
            result = f"Победитель: {winner}"
        result_label = tk.Label(self.root, text=result, font=("Arial", 16))
        result_label.grid(row=4, column=0, columnspan=3)

    def reset_game(self):
        self.game.reset()
        self.update_board()


# Запуск приложения
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGame(root)
    root.mainloop()

