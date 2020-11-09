"""
Программа генерирует число от 0 до 1_000_000 и предлагает угадать его.

Программа должна приветствовать пользователя и считывать число с клавиатуры
Если число меньше загаданного, то программа выводит сообщение о том, что число
меньше
Если больше загаданного, то программа выводит сообщение о том, что больше

Программа должна выводить сообщения-предупреждения, если:
* пользователь ввёл не число
* число не входит в обозначенный в условии диапазон
Если пользователь ничего не ввёл/ввёл "exit", то происходит выход из программы.

Тебе может понадобится модуль random, цикл while и ветвления
"""
import random

if __name__ == '__main__':
    random_number = random.randint(1, 1000_000)
    users_number = int(input('Try to guess the number: '))
    while users_number != random_number:
        if str(users_number).isdigit():
            if not 0 < int(users_number) < 1000_001:
                print('Your number is out of diapason')
            if int(users_number) > random_number:
                print('Hidden number is lower than Your number')
            else:
                print('Hidden number is higher than Your number')
            users_number = input('Try again: ')
        else:
            print('You entered not a number')
            users_number = input('Try again: ')
        if users_number == 'exit':
            break
        if int(users_number) == random_number:
            break
    if int(users_number) == random_number:
        print('You guessed the number right!')
