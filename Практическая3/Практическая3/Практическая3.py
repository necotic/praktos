import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import string

# Генерация пароля
def generate_password():
    length = int(password_length_entry.get())
    include_digits = digits_var.get()
    include_symbols = symbols_var.get()
    
    characters = string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    password_output.config(text=password)

# Конвертер температуры
def convert_temperature():
    temp = float(temperature_entry.get())
    unit = temperature_unit.get()
    
    if unit == "C":
        converted_temp = (temp * 9/5) + 32
        result_label.config(text=f"{temp}°C = {converted_temp:.2f}°F")
    elif unit == "F":
        converted_temp = (temp - 32) * 5/9
        result_label.config(text=f"{temp}°F = {converted_temp:.2f}°C")

# Открытие изображения
def open_image():
    global image
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp")])
    if file_path:
        image = Image.open(file_path)
        image.thumbnail((400, 400))  # Ограничиваем размер
        img = ImageTk.PhotoImage(image)
        
        # Сохраняем изображение для отображения
        panel.config(image=img)
        panel.image = img
        image_label.config(text=f"Открыто: {file_path.split('/')[-1]}")

# Изменение размера изображения
def resize_image():
    if image:
        try:
            width = int(width_entry.get())
            height = int(height_entry.get())
            resized_image = image.resize((width, height))
            img = ImageTk.PhotoImage(resized_image)
            
            # Обновляем изображение на панели
            panel.config(image=img)
            panel.image = img
        except ValueError:
            messagebox.showerror("Ошибка", "Пожалуйста, введите правильные значения для ширины и высоты.")

# Закрытие окна
def close_window():
    window.quit()

# Основное окно
window = tk.Tk()
window.title("Простой блокнот и конвертер")

# Кнопка для генерации пароля
password_frame = tk.Frame(window)
password_frame.pack(pady=10)

password_label = tk.Label(password_frame, text="Длина пароля:")
password_label.pack(side=tk.LEFT)

password_length_entry = tk.Entry(password_frame)
password_length_entry.insert(0, "12")
password_length_entry.pack(side=tk.LEFT, padx=10)

digits_var = tk.BooleanVar(value=True)
digits_checkbox = tk.Checkbutton(password_frame, text="Включать цифры", variable=digits_var)
digits_checkbox.pack(side=tk.LEFT)

symbols_var = tk.BooleanVar(value=True)
symbols_checkbox = tk.Checkbutton(password_frame, text="Включать символы", variable=symbols_var)
symbols_checkbox.pack(side=tk.LEFT)

generate_button = tk.Button(password_frame, text="Сгенерировать пароль", command=generate_password)
generate_button.pack(side=tk.LEFT, padx=10)

password_output = tk.Label(window, text="")
password_output.pack(pady=10)

# Кнопки для конвертации температуры
temp_frame = tk.Frame(window)
temp_frame.pack(pady=10)

temperature_label = tk.Label(temp_frame, text="Введите температуру:")
temperature_label.pack(side=tk.LEFT)

temperature_entry = tk.Entry(temp_frame)
temperature_entry.pack(side=tk.LEFT, padx=10)

temperature_unit = tk.StringVar(value="C")
celsius_radio = tk.Radiobutton(temp_frame, text="Цельсий", variable=temperature_unit, value="C")
celsius_radio.pack(side=tk.LEFT)

fahrenheit_radio = tk.Radiobutton(temp_frame, text="Фаренгейт", variable=temperature_unit, value="F")
fahrenheit_radio.pack(side=tk.LEFT)

convert_button = tk.Button(temp_frame, text="Конвертировать", command=convert_temperature)
convert_button.pack(side=tk.LEFT, padx=10)

result_label = tk.Label(window, text="")
result_label.pack(pady=10)

# Кнопка для открытия изображения
image_frame = tk.Frame(window)
image_frame.pack(pady=10)

open_image_button = tk.Button(image_frame, text="Открыть изображение", command=open_image)
open_image_button.pack()

image_label = tk.Label(image_frame, text="Изображение не открыто")
image_label.pack()

# Место для отображения изображения
panel = tk.Label(window)
panel.pack(pady=10)

# Поля для изменения размера изображения
resize_frame = tk.Frame(window)
resize_frame.pack(pady=10)

width_label = tk.Label(resize_frame, text="Ширина:")
width_label.pack(side=tk.LEFT)

width_entry = tk.Entry(resize_frame)
width_entry.pack(side=tk.LEFT)

height_label = tk.Label(resize_frame, text="Высота:")
height_label.pack(side=tk.LEFT)

height_entry = tk.Entry(resize_frame)
height_entry.pack(side=tk.LEFT)

resize_button = tk.Button(resize_frame, text="Изменить размер", command=resize_image)
resize_button.pack(side=tk.LEFT, padx=10)

# Кнопка для выхода
exit_button = tk.Button(window, text="Закрыть", command=close_window)
exit_button.pack(pady=10)

# Запуск приложения
window.mainloop()