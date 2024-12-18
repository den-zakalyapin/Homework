import os
import time

directory = "."  # переменная директория

for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file)  # путь
        filetime = os.path.getmtime(filepath)  # Время последнего изменения
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime)) #Отформатированная строка времени
        filesize = os.path.getsize(filepath)  # размер файла
        parent_dir = os.path.dirname(filepath)  # родительский каталог
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')