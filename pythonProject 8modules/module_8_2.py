def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    for item in numbers:
        try:
            result += item  # Попытка сложить элемент
        except TypeError:
            print(f'Некорректный тип данных для подсчёта суммы - {item}')
            incorrect_data += 1  # Увеличиваем счетчик некорректных данных

    return result, incorrect_data


def calculate_average(numbers):
    try:
        # Проверка, является ли numbers коллекцией
        if not isinstance(numbers, (list, tuple, set)):
            raise TypeError  # Генерируем исключение, если это не коллекция

        total, incorrect_count = personal_sum(numbers)  # Получаем сумму и количество некорректных данных

        # Возвращаем 0, если нет корректных данных
        if len(numbers) - incorrect_count == 0:
            return 0

        return total / (len(numbers) - incorrect_count)  # Среднее арифметическое
    except ZeroDivisionError:
        return 0  # Возвращаем 0 при делении на 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None  # Возвращаем None в случае некорректного типа данных



print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Смешанная коллекция
print(f'Результат 3: {calculate_average(567)}')  # Не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Корректная коллекция