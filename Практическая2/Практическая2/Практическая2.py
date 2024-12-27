import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Для работы с иконкой

class GuessTheNumberGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Угадай число")

        # Загрузка иконки из файла
        self.root.iconbitmap("icon.ico")  # Убедитесь, что файл `icon.ico` в папке с программой

        # Минимальное и максимальное значение
        self.min_number = 1
        self.max_number = 100
        self.secret_number = None
        self.attempts_left = 10

        # Главное окно
        self.frame = tk.Frame(root)
        self.frame.pack(pady=10, padx=10)

        # Панель с кнопками
        self.panel = tk.Frame(self.frame)
        self.panel.pack(fill=tk.X)

        self.new_game_button = tk.Button(self.panel, text="Новая игра", command=self.new_game)
        self.new_game_button.pack(side=tk.LEFT, padx=5)

        self.minimize_button = tk.Button(self.panel, text="Свернуть в трей", command=self.minimize_to_tray)
        self.minimize_button.pack(side=tk.RIGHT, padx=5)

        # Поле для вывода текста
        self.output = tk.Text(self.frame, width=40, height=10, state=tk.DISABLED)
        self.output.pack(pady=10)

        # Ввод числа
        self.input_label = tk.Label(self.frame, text="Введите число:")
        self.input_label.pack()
        self.input_field = tk.Entry(self.frame)
        self.input_field.pack()
        self.input_field.bind("<Return>", lambda event: self.check_guess())

        self.submit_button = tk.Button(self.frame, text="Отправить", command=self.check_guess)
        self.submit_button.pack(pady=5)

        self.new_game()

    def new_game(self):
        """Начинает новую игру."""
        self.min_number = 1
        self.max_number = 100
        self.secret_number = random.randint(self.min_number, self.max_number)
        self.attempts_left = 10
        self.clear_output()
        self.print_to_output("Началась новая игра! Угадайте число от 1 до 100.")

    def minimize_to_tray(self):
        """Сворачивает окно в трей."""
        self.root.iconify()

    def check_guess(self):
        """Проверяет ввод пользователя."""
        try:
            guess = int(self.input_field.get())
            self.input_field.delete(0, tk.END)
            if guess < self.secret_number:
                self.print_to_output("Ваше число меньше загаданного.")
            elif guess > self.secret_number:
                self.print_to_output("Ваше число больше загаданного.")
            else:
                messagebox.showinfo("Поздравляем!", "Вы угадали число!")
                self.new_game()
                return

            self.attempts_left -= 1
            if self.attempts_left == 0:
                messagebox.showinfo("Конец игры", f"Вы проиграли! Загаданное число было: {self.secret_number}")
                self.new_game()
            else:
                self.print_to_output(f"Осталось попыток: {self.attempts_left}")
        except ValueError:
            self.print_to_output("Ошибка: Введите корректное число.")

    def clear_output(self):
        """Очищает текстовое поле."""
        self.output.config(state=tk.NORMAL)
        self.output.delete(1.0, tk.END)
        self.output.config(state=tk.DISABLED)

    def print_to_output(self, text):
        """Выводит текст в текстовое поле."""
        self.output.config(state=tk.NORMAL)
        self.output.insert(tk.END, text + "\n")
        self.output.config(state=tk.DISABLED)

# Главная программа
if __name__ == "__main__":
    root = tk.Tk()
    app = GuessTheNumberGame(root)
    root.mainloop()
