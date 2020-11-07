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
                    if single_number.isdigit():
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
def sell_alcohol():
    print('Продаем алкоголь')
age = 17
sell_alcohol() if age >= 21 else print('Мы не продаём алкоголь несовершеннолетним.')


# напиши функцию, которая проверит, является ли строка ключевым словом в Питоне
# тебе понадобится модуль keyword, импортируй его и изучи с помощью dir()
def function_keyword():
    import keyword
    string = input()
    print('String is indeed a keyword in Python') if keyword.iskeyword(string) else print('String is not a keyword')

# напиши функцию, которая возвращает тип данных на русском языке:
# число, строка, булевый, None, список, кортеж, множество, словарь
# пример: get_type("что-то") возвращает "Это строка."
# пример2: get_type(42) возвращает "Это словарь."
checked_object = ('a', "B", "C")
def get_type(checked_object):
    p = type(checked_object)
    if p == str:
        print('это строка')
    if p == list:
        print('это список')
    if p == bool:
        print('это булевый')
    if p == dict:
        print('это словарь')
    if p == tuple:
        print('это кортеж')
    if p == int or p == float:
        print('это число')
    if p == set:
        print('это множество')
    if p == None:
        print('это None')

