import tkinter as tk
import pyautogui
from PIL import Image, ImageTk
import threading
import time
import keyboard  # Для отслеживания нажатия клавиши F6

# Переменные
clicking = False
click_count = 0  # Счетчик кликов

# Функция для выполнения кликов
def start_clicking(interval):
    global click_count
    while clicking:
        pyautogui.click()  # Кликаем в текущем положении мыши
        click_count += 1  # Увеличиваем счетчик кликов
        label_click_rate.config(text=str(click_count))  # Обновляем текст с текущим счетом
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

# Инициализация интерфейса
root = tk.Tk()
root.title("Auto Clicker")

# Загружаем фоновое изображение
bg_image = Image.open("C:/Users/opilane/Desktop/clicker/feixiao.png")  # Используйте правильный путь к файлу
bg_image = bg_image.resize((600, 400))  # Изменить размер изображения по необходимости
bg_photo = ImageTk.PhotoImage(bg_image)

# Устанавливаем фон
canvas = tk.Canvas(root, width=600, height=400)
canvas.pack()
canvas.create_image(0, 0, anchor=tk.NW, image=bg_photo)

# Добавляем элементы управления
start_button = tk.Button(root, text="Start Clicking", command=toggle_clicking)
start_button.place(x=250, y=300)

# Счётчик кликов
label_click_rate = tk.Label(root, text="0", font=("Arial", 20), bg="white")
label_click_rate.place(x=250, y=250)

# Запуск проверки клавиши F6 в фоновом потоке
def check_f6_thread():
    while True:
        check_f6_key()
        time.sleep(0.1)  # Проверяем клавишу каждые 100 миллисекунд

# Запускаем поток для отслеживания нажатия клавиши F6
threading.Thread(target=check_f6_thread, daemon=True).start()

# Запуск интерфейса
root.mainloop()
