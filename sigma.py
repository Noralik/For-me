import tkinter as tk
import threading
import pyautogui
import keyboard
import time

clicking = False
click_thread = None
click_interval = 0.01  # Начальный интервал между кликами

# Функция, которая будет выполняться в отдельном потоке для кликов
def click_loop():
    while True:
        if clicking:
            pyautogui.click()
            time.sleep(click_interval)  # Интервал между кликами
        else:
            time.sleep(0.1)

# Функция для включения/выключения кликов
def toggle_clicking():
    global clicking
    clicking = not clicking
    status_var.set("Статус: ВКЛ" if clicking else "Статус: ВЫКЛ")

# Функция для отслеживания нажатия F6
def monitor_key():
    while True:
        keyboard.wait('f6')
        toggle_clicking()

# Функция для изменения интервала между кликами
def update_interval(val):
    global click_interval
    click_interval = float(val) / 1000  # Ползунок дает значения от 0 до 1000, мы делим на 1000 для нужной точности
    interval_var.set(f"Интервал: {click_interval:.3f} сек")

# Запуск потоков
def start_key_monitoring():
    threading.Thread(target=monitor_key, daemon=True).start()

def start_click_thread():
    global click_thread
    click_thread = threading.Thread(target=click_loop, daemon=True)
    click_thread.start()

# GUI
root = tk.Tk()
root.title("Автокликер")

# Статус
status_var = tk.StringVar()
status_var.set("Статус: ВЫКЛ")

status_label = tk.Label(root, textvariable=status_var, font=("Arial", 14))
status_label.pack(padx=20, pady=10)

# Информация
info_label = tk.Label(root, text="Нажми F6 для включения/выключения", font=("Arial", 10))
info_label.pack(pady=5)

# Ползунок для изменения интервала
interval_var = tk.StringVar()
interval_var.set(f"Интервал: {click_interval:.3f} сек")

interval_label = tk.Label(root, textvariable=interval_var, font=("Arial", 10))
interval_label.pack(pady=5)

interval_slider = tk.Scale(root, from_=1, to=1000, orient="horizontal", command=update_interval)
interval_slider.set(10)  # Начальный интервал (0.01 секунды)
interval_slider.pack(padx=20, pady=10)

# Запуск потоков
start_click_thread()
start_key_monitoring()

root.mainloop()
