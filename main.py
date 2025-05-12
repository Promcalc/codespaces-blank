from fractions import Fraction


def calc01():
    # Запрашиваем у пользователя ввод числа n
    n = float(input("Введите число n: "))
    
    # Вычисляем выражение n^2 + n^3 + n^4
    result = n**2 + n**3 + n**4
    
    # Выводим результат
    print(f"Результат выражения n^2 + n^3 + n^4 для n = {n} равен {result}")

def calc02():
    # Запрашиваем у пользователя ввод списка чисел, разделенных пробелами
    numbers = input("Введите список чисел, разделенных пробелами: ").split()

    # Проходим по каждому числу в списке
    for num_str in numbers:
        try:
            # Преобразуем строку в число
            num = float(num_str)
            # Проверяем, является ли число положительным
            if num < 0:
                print("Найдено первое отрицательное число. Завершение программы.")
                break
            else:
                print(num)  # Выводим положительное число
        except ValueError:
            print(f"'{num_str}' не является числом. Пропускаем.")

def calc03():
    # Запрашиваем у пользователя ввод вещественного числа
    number = float(input("Введите вещественное число: "))
    
    # Находим наименьшую обыкновенную дробь, приближенную к введенному числу
    fraction = Fraction(number).limit_denominator()  # Округляем до ближайшей дроби
    
    # Форматируем число с округлением до двух знаков после запятой
    formatted_number = f"{number:.2f}"
    
    # Выводим результат
    print(f"{formatted_number} ≈ {fraction.numerator}/{fraction.denominator}")

def calc04():
    # Запрашиваем у пользователя ввод количества минут
    total_minutes = int(input("Введите количество минут: "))

    # Вычисляем количество дней, часов и оставшихся минут
    days = total_minutes // (60 * 24)  # 1 день = 1440 минут
    hours = (total_minutes % (60 * 24)) // 60  # 1 час = 60 минут
    minutes = total_minutes % 60  # Оставшиеся минуты

    # Форматируем результат
    result = f"{days:02}:{hours:02}:{minutes:02}"

    # Выводим результат
    print(f"Результат: {result}")

if __name__ == "__main__":
    calc04()