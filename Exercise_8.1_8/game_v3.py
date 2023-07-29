"""Игра угадай число.
Компьютер сам загадывает и угадывает число
"""
import numpy as np
def sistem_predict(number: int = 1) -> int:
    """Систематически вычисляю число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0  
    half_range = 50 # Число, которое будет уменьшаться в два раза при каждой этерации. Равно среднему значению диапазона загадываемых чисел. 
    predict_number = half_range
    
    while True:
        count += 1 # Считаем попытки
        
        half_range = int(half_range/2+0.5) # Целое число. Округляю в большую сторону, если десятичная дробь больше или равна 0.5
        
        if number == predict_number:
            break # Выход из цикла, если угадали
        elif number > predict_number:
            predict_number += half_range # Увеличиваем наш ответ на половину диапазона 
        elif number < predict_number:
            predict_number -= half_range # Уменшаем наш ответ на половину диапазона

    return(count)

def score_game(random_predict) -> int:
    """За какое колличество попыток в среднем из 1000 подходов 
    угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее колличество попыток
    """
    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
if __name__ == '__main__':
    score_game(sistem_predict)