"""
Программа выводит на экран числа от 1 до 100 включительно, с новой строки.

Если число кратно трём, то вместо этого числа программа выводит слово "zip"
Если чисто кратно пяти, то вместо этого числа выводится слово "zap"
Если число кратно пятнадцати, то вместо этого числа выводится слово "zip-zap"

Тебе может понадобиться цикл for и ветвления
"""
number = 1
while number !=101:
    if number % 15 == 0:
        print('zip-zap')
    elif number % 5 == 0:
        print('zap')
    elif number % 3 == 0:
        print('zip')
    else:
        print(number)
    number = number + 1
if __name__ == '__main__':
    pass
