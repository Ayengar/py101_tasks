"""Задания по ветвлениям, итерациям и вводу данных."""

# напиши функцию, которая принимает на вход любое
# количество чисел и сообщает, есть ли среди них чётное
def even_numbers():
            even_number_condition = 0
            single_number = ''
            numbers = input()
            for i in range(0, len(numbers)):
                if numbers[i] != ' ' :
                    single_number = single_number + numbers[i]
                else:
                    if single_number != '':
                        if int(single_number) % 2 == 0:
                            even_number_condition = 1
                    single_number = ''
            if even_number_condition == 1 or int(single_number) % 2 == 0:
                print('There are even number(s)')
            else:
                print('There are only odd numbers')
            
# используй тернарный оператор, чтобы вызвать функцию
# если возраст больше 21 года, в противном случае верни
# сообщение "Мы не продаём алкоголь несовершеннолетним."
# age = 17
# sell_alcohol()


# напиши функцию, которая проверит, является ли строка ключевым словом в Питоне
# тебе понадобится модуль keyword, импортируй его и изучи с помощью dir()


# напиши функцию, которая возвращает тип данных на русском языке:
# число, строка, булевый, None, список, кортеж, множество, словарь
# пример: get_type("что-то") возвращает "Это строка."
# пример2: get_type(42) возвращает "Это словарь."
