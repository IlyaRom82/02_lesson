def month_to_season(month):
    """
    Функция принимает номер месяца (1-12) и возвращает название сезона.
    Зима: 12, 1, 2
    Весна: 3, 4, 5
    Лето: 6, 7, 8
    Осень: 9, 10, 11
    """
    if month in (12, 1, 2):
        return "Зима"
    elif month in (3, 4, 5):
        return "Весна"
    elif month in (6, 7, 8):
        return "Лето"
    elif month in (9, 10, 11):
        return "Осень"
    else:
        return "Некорректный номер месяца"


# Пример использования функции
if __name__ == "__main__":
    for test_month in range(1, 13):
        print(month_to_season(int(input('4'))))
