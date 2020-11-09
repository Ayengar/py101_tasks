"""
Программа оценивает сложность пароля.

Пользователь вводит пароль, в ответ получает оценку "сложный"/"простой"
Сложным считается пароль, состоящий как минимум из 8-ми символов,
включая цифры и алфавитные символы
"""
if __name__ == '__main__':
N = 1
L = 0
B = 0
temp ='0123456789'
print('Enter your password')
password = input()
for numbers in range(0, len(password)):
   if password[numbers] in temp:
       N=0
if password.isupper() or password.islower():
       B = 1
if len(password) < 8:
    L = 1
Safety_Condition = L+N+B
if Safety_Condition != 0:
    print('Your password is too weak!')
    if N == 1:
        print('Add numbers to your password')
    if L == 1:
        print('Enter password with 8 or more symbols')
    if B == 1:
        print('Use upper & lower cases in your password')
else:
    print('Your password is good')
