import requests
import matplotlib.pyplot as plt
from datetime import datetime
from tkinter import messagebox
from plyer import notification

# API ключ OpenWeatherMap (замени на свой)
API_KEY = "8abaaec8ad619728f76a0ecfe4669b76"
CITY = "Yakutsk"
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&units=metric&cnt=7&appid={API_KEY}"

# Функция получения данных о погоде
def get_weather():
    response = requests.get(URL)
    print(f"Status Code: {response.status_code}")  # Добавим вывод кода статуса
    data = response.json()
    
    if data["cod"] != "200":
        print("Error response:", data)  # Напечатаем ошибку в ответе
        messagebox.showerror("Error", f"Не удалось получить данные о погоде: {data}")
        return None
    
    return data

# Функция для обработки и отображения данных
def process_data(data):
    dates = []
    temps = []
    descriptions = []
    
    for forecast in data["list"]:
        # Преобразование времени из UNIX в дату
        dates.append(datetime.utcfromtimestamp(forecast["dt"]).strftime('%Y-%m-%d %H:%M:%S'))
        temps.append(forecast["main"]["temp"])
        descriptions.append(forecast["weather"][0]["description"])
    
    return dates, temps, descriptions

# Функция отображения графика температур
def plot_temperature(dates, temps):
    plt.plot(dates, temps, marker='o', color='b', linestyle='-', label="Temperature")
    plt.xticks(rotation=45)
    plt.xlabel("Дата/Время")
    plt.ylabel("Температура (°C)")
    plt.title("Прогноз температуры")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Функция для отправки уведомлений
def send_notifications(temps, descriptions):
    for temp, desc in zip(temps, descriptions):
        if temp < 0:
            notification.notify(
                title="Погода: Ожидается мороз!",
                message="Ожидается мороз. Одевайтесь теплее!",
                timeout=10
            )
        elif "rain" in desc or "snow" in desc:
            notification.notify(
                title="Погода: Ожидаются осадки!",
                message="Возьмите зонт, ожидаются осадки.",
                timeout=10
            )

# Основная программа
def main():
    data = get_weather()
    if data:
        # Получаем прогноз
        dates, temps, descriptions = process_data(data)

        # Отображаем график
        plot_temperature(dates, temps)

        # Отправляем уведомления
        send_notifications(temps, descriptions)

        # Отображаем текущую погоду и описание
        current_temp = temps[0]
        current_desc = descriptions[0]
        messagebox.showinfo(
            "Текущая погода",
            f"Город: {CITY}\n"
            f"Температура: {current_temp}°C\n"
            f"Описание: {current_desc}\n"
            f"Прогноз на ближайшие дни отображён на графике."
        )

# Запуск программы
if __name__ == "__main__":
    main()

