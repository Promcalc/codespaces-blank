import random

# Список загадок и их ответов
riddles = [
    {"question": "Что за птица, что не летает?", "answer": "курица"},
    {"question": "Сколько ног у стула?", "answer": "четыре"},
    {"question": "Что растет, но не живет?", "answer": "камень"},
    {"question": "Что у человека всегда с собой, но никто не видит?", "answer": "имя"},
    {"question": "Что может быть в руках, но не может быть в кармане?", "answer": "птица"},
    {"question": "Что идет вверх, но никогда не движется?", "answer": "возраст"},
    {"question": "Какой месяц имеет 28 дней?", "answer": "февраль"},
    {"question": "Что легче перышка, но даже самый сильный человек не может удержать это в руках?", "answer": "дыхание"},
    {"question": "Что всегда впереди, но никогда не видно?", "answer": "будущее"},
    {"question": "Что можно увидеть один раз в минуту, два раза в моменте, но никогда в тысячу лет?", "answer": "буква 'м'"},
]

def play_game():
    # Выбираем 3 случайные загадки
    selected_riddles = random.sample(riddles, 3)
    score = 0

    for riddle in selected_riddles:
        print(riddle["question"])
        user_answer = input("Ваш ответ: ").strip().lower()
        
        if user_answer == riddle["answer"]:
            print("Правильно!")
            score += 1
        else:
            print(f"Неправильно. Правильный ответ: {riddle['answer']}")

    print(f"Вы отгадали {score} из 3 загадок.")

if __name__ == "__main__":
    print("Добро пожаловать в игру 'Угадай загадку'!")
    play_game()
