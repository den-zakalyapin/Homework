def add_everything_up(a, b):
    try:
        # Проверяем, являются ли a и b разными типами (число и строка)
        if (isinstance(a, (int, float)) and isinstance(b, str)) or (isinstance(a, str) and isinstance(b, (int, float))):
            # Если это так, возвращаем строковое представление a и b
            return str(a) + str(b)
        else:
            # В противном случае складываем значения
            return a + b
    except TypeError:
        # Обработка исключения TypeError
        return str(a) + str(b)

# Примеры использования
print(add_everything_up(123.456, 'строка'))  # Вывод: 123.456строка
print(add_everything_up('яблоко', 4215))     # Вывод: яблоко4215
print(add_everything_up(123.456, 7))          # Вывод: 130.456
