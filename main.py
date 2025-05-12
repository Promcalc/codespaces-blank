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

def calc05():
    # Запрашиваем у пользователя ввод целого числа
    number = int(input("Введите целое число: "))
    
    # Проверяем, делится ли число на 5 без остатка
    if number % 5 == 0:
        print(f"{number} делится на 5 без остатка.")
    else:
        print(f"{number} не делится на 5 без остатка.")


def kilometers_to_miles(km):
    return km * 0.621371

def miles_to_kilometers(miles):
    return miles / 0.621371

def calc06():
    print("Выберите действие:")
    print("1. Перевести километры в мили")
    print("2. Перевести мили в километры")

    choice = input("Введите номер действия (1 или 2): ")

    if choice == '1':
        km = float(input("Введите расстояние в километрах: "))
        miles = kilometers_to_miles(km)
        print(f"{km} километров равно {miles:.2f} миль.")
    elif choice == '2':
        miles = float(input("Введите расстояние в милях: "))
        km = miles_to_kilometers(miles)
        print(f"{miles} миль равно {km:.2f} километров.")
    else:
        print("Некорректный выбор. Пожалуйста, попробуйте еще раз.")

if __name__ == "__main__":
    calc06()