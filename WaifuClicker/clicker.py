import tkinter as tk
import pyautogui
from PIL import Image, ImageTk
import threading
import time
import keyboard  # Для отслеживания нажатия клавиши F6
import json  # Для сохранения данных в файл

# Переменные
clicking = False
click_count = 0  # Счетчик кликов

# Путь к файлу с данными
data_file = "click_data.json"

# Функция для загрузки кликов из файла
def load_clicks():
    global click_count
    try:
        with open(data_file, 'r') as file:
            data = json.load(file)
            click_count = data.get("click_count", 0)  # Если данных нет, то устанавливаем 0
    except (FileNotFoundError, json.JSONDecodeError):
        click_count = 0  # Если файл не существует или поврежден, начинаем с 0 кликов
        save_clicks()  # Создаём новый файл с 0 кликами

# Функция для сохранения кликов в файл
def save_clicks():
    with open(data_file, 'w') as file:
        json.dump({"click_count": click_count}, file)

# Функция для выполнения кликов
def start_clicking(interval):
    global click_count
    while clicking:
        pyautogui.click()  # Кликаем в текущем положении мыши
        click_count += 1  # Увеличиваем счетчик кликов
        label_click_rate.config(text=str(click_count))  # Обновляем текст с текущим счетом
        save_clicks()  # Сохраняем клики в файл
        time.sleep(interval)  # Интервал между кликами

# Функция для начала/остановки кликов
def toggle_clicking():
    global clicking
    if clicking:
        clicking = False
        start_button.config(text="Start Clicking")
    else:
        clicking = True
        start_button.config(text="Stop Clicking")
        threading.Thread(target=start_clicking, args=(0.0001,), daemon=True).start()

# Функция для запуска/остановки с клавиши F6
def check_f6_key():
    global clicking
    if keyboard.is_pressed("F6"):
        toggle_clicking()

# Функция для сброса кликов
def reset_clicks():
    global click_count
    click_count = 0  # Сбрасываем счетчик
    label_click_rate.config(text=str(click_count))  # Обновляем метку
    save_clicks()  # Сохраняем новые данные

# Инициализация интерфейса
root = tk.Tk()
root.title("Waifu Clicker")

# Загружаем GIF изображение
bg_image = Image.open(r"Waifu\Feixiao\feixiao3.gif")  # Используй путь к файлу

# Устанавливаем фон
canvas = tk.Canvas(root, width=400, height=800)
canvas.pack()

# Функция для анимации GIF
def animate_gif():
    while True:
        try:
            # Загружаем следующий кадр из GIF
            bg_image.seek(bg_image.tell() + 1)
        except EOFError:
            bg_image.seek(0)  # Если достигнут конец, начинаем сначала
        
        # Получаем размеры окна (включая канвас)
        window_width = root.winfo_width()
        window_height = root.winfo_height()

        # Изменяем размер изображения в зависимости от размеров окна
        resized_image = bg_image.resize((window_width, window_height), Image.Resampling.LANCZOS)

        # Создаём объект для обновлённого изображения
        bg_photo = ImageTk.PhotoImage(resized_image)

        # Обновляем изображение на канвасе
        canvas.create_image(0, 0, anchor=tk.NW, image=bg_photo)
        canvas.image = bg_photo  # Храним ссылку на изображение, чтобы оно не удалялось сборщиком мусора

        time.sleep(0.1)  # Задержка между кадрами

# Запускаем поток для анимации GIF
threading.Thread(target=animate_gif, daemon=True).start()

# Добавляем элементы управления
start_button = tk.Button(root, text="Start Clicking", command=toggle_clicking)
start_button.place(x=250, y=300)

# Счётчик кликов
label_click_rate = tk.Label(root, text="0", font=("Arial", 20), bg="white")
label_click_rate.place(x=250, y=250)

# Кнопка для сброса кликов
reset_button = tk.Button(root, text="Reset Clicks", command=reset_clicks)
reset_button.place(x=250, y=350)

# Запуск проверки клавиши F6 в фоновом потоке
def check_f6_thread():
    while True:
        check_f6_key()
        time.sleep(0.1)  # Проверяем клавишу каждые 100 миллисекунд

# Запускаем поток для отслеживания нажатия клавиши F6
threading.Thread(target=check_f6_thread, daemon=True).start()

# Загружаем количество кликов перед запуском
load_clicks()
label_click_rate.config(text=str(click_count))  # Отображаем начальное количество кликов

# Запуск интерфейса
root.mainloop()
