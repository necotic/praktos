import random

def is_valid_input(value):
    """Проверяет, является ли ввод корректным числом."""
    return value.isdigit()

def get_number_input(prompt):
    """Запрашивает ввод пользователя и возвращает число."""
    while True:
        user_input = input(prompt)
        if is_valid_input(user_input):
            return int(user_input)
        else:
            print("Ошибка: введите корректное число.")

def main():
    print("Добро пожаловать в игру 'Угадай число'!")
    
    # Установление границ для случайного числа
    print("Введите минимальное и максимальное значения для случайного числа.")
    min_number = get_number_input("Минимальное значение: ")
    max_number = get_number_input("Максимальное значение: ")
    
    # Проверка корректности границ
    if min_number >= max_number:
        print("Ошибка: Минимальное значение должно быть меньше максимального.")
        return
    
    # Генерация случайного числа
    secret_number = random.randint(min_number, max_number)
    print("Число сгенерировано! Попробуйте угадать его за 10 попыток.")
    
    attempts_left = 10

    while attempts_left > 0:
        print(f"Осталось попыток: {attempts_left}")
        guess = get_number_input("Введите ваше предположение: ")

        if guess < secret_number:
            print("Ваше число меньше загаданного.")
        elif guess > secret_number:
            print("Ваше число больше загаданного.")
        else:
            print("Поздравляем! Вы угадали число!")
            break

        attempts_left -= 1

    if attempts_left == 0:
        print(f"К сожалению, попытки закончились. Загаданное число было: {secret_number}")

if __name__ == "__main__":
    main()

