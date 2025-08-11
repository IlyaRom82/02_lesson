import math  # подключаем модуль math для округления вверх


# Функция для вычисления площади квадрата
def square(side):
    area = side * side  # формула: сторона * сторона
    return math.ceil(area)  # округляем вверх


# Пример использования
side_length = 4.3  # можно поменять на любое значение
result = square(side_length)


print(f"Сторона квадрата: {side_length}, площадь: {result}")
