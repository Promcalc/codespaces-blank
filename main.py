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


import random

import random

def display_sticks(count):
    print(f"На столе {count} палочек.")

def player_move(player_name, sticks):
    while True:
        try:
            taken = int(input(f"{player_name}, сколько палочек вы хотите взять (1, 2 или 3)? "))
            if taken in [1, 2, 3] and taken <= sticks:
                return taken
            else:
                print("Неверный ввод. Попробуйте взять 1, 2 или 3 палочки, но не больше оставшихся.")
        except ValueError:
            print("Пожалуйста, введите число.")

def computer_move(sticks):
    # Стратегия: оставить количество палочек кратным 4 (если это возможно)
    if sticks > 4:
        taken = (sticks - 1) % 4
        if taken == 0:
            taken = random.randint(1, 3)  # Если не удалось, берем случайное количество
    else:
        taken = min(3, sticks)  # Берем максимум 3 палочки
    print(f"Компьютер берет {taken} палочек.")
    return taken

def game01():
    # Начальное количество палочек
    total_sticks = random.randint(17, 29)
    display_sticks(total_sticks)

    # Выбор режима игры
    game_mode = input("Выберите режим игры: 1 - Два игрока, 2 - Игрок против компьютера: ")
    if game_mode not in ['1', '2']:
        print("Некорректный выбор. Игра завершена.")
        return

    # Определяем, кто ходит первым
    if random.choice([True, False]):
        player1_name = "Игрок 1"
        player2_name = "Игрок 2" if game_mode == '1' else "Компьютер"
        first_player = player1_name
    else:
        player1_name = "Компьютер" if game_mode == '2' else "Игрок 2"
        player2_name = "Игрок 1"
        first_player = player1_name

    print(f"{first_player} начинает первым!")

    current_player = 1 if first_player == player1_name else 2

    while total_sticks > 0:
        if current_player == 1:
            if player2_name == "Компьютер":
                taken = computer_move(total_sticks)
            else:
                taken = player_move(player1_name, total_sticks)
        else:
            taken = player_move(player2_name, total_sticks)

        total_sticks -= taken

        display_sticks(total_sticks)

        # Проверка на проигрыш
        if total_sticks == 0:
            if current_player == 1:
                print(f"{player1_name} взял последнюю палочку и проиграл!")
            else:
                print(f"{player2_name} взял последнюю палочку и проиграл!")
            break

        # Смена игрока
        current_player = 2 if current_player == 1 else 1

if __name__ == "__main__":
    game01()