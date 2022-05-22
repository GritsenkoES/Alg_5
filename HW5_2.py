'''Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел.
При этом каждое число представляется как коллекция, элементы которой - цифры числа.
'''
from collections import deque
from functools import reduce
a = input('Введите число в шестнадцатеричной системе: ').upper()
b = input('Введите число в шестнадцатеричной системе: ').upper()

dict_hex = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
           'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'J': 16}

def find_key(value, dictionary):
    '''определим функцию для поиска ключа по значению'''
    for key in dictionary:
        if dictionary[key] == value:
            return key

def sum_hex(a, b):
    ''' определим функцию сложения чисел в 16 СC
    за алгоритм возьмем сложение чисел в столбик, где каждые цифры соот-й разрядности слагаемых
    складываются между собой, в случае если сумма цифр больше 16 введем переменную spam, которую прибавим
    к сумме цифр следующей разрядности'''
    spam = 0  # в случае когда сумма чисел > 16, тогда будем прибавлять к следующей разрядности "буфер"
    a = deque(a)
    b = deque(b)
    total = deque()
    while len(a) != len(b):  # выравниваем числа по длине
        if len(a) > len(b):
            b.appendleft('0')
        else:
            a.appendleft('0')
    for i in range(len(a)):
        numb_a = dict_hex[deque(a)[-1-i]]
        numb_b = dict_hex[deque(b)[-1-i]]
        total.appendleft(find_key(((numb_a + numb_b) + spam) % 16, dict_hex))
        spam = ((numb_a + numb_b) + spam) // 16
    if spam != 0:  # чтобы не потерять spam
        total.appendleft(find_key(spam, dict_hex))
    return total


def mult_hex(a, b):
    ''' определим функцию умножения чисел в 16 СC
    алгоритм функции заключается в умножении каждой цифры числа 'а' на число 'b'
    последующим сложением получившихся результатов
    т.е. 15*12 = 15*10 + 15*2 '''

    a = deque(a)
    b = deque(b)
    fact = []  # список в котором будем хранить результаты умножений каждой цифры "а" на число "b"
    for i in range(len(a)):
        spam = 0  # в случае когда произведение чисел > 16, тогда будем прибавлять к следующей разрядности "буфер"
        total = deque()
        numb_a = dict_hex[deque(a)[-1 - i]]
        for j in range(len(b)):
            numb_b = dict_hex[deque(b)[-1 - j]]
            total.appendleft(find_key(((numb_a * numb_b) + spam) % 16, dict_hex))
            spam = (numb_a * numb_b + spam) // 16
        if spam != 0:  # чтобы не потерять переменную spam при умножении с последней цифрой 'b'
            total.appendleft(find_key(spam, dict_hex))
        fact.append(total)
    # учтем разрядность при умножении, т.е. добавим справа "0"  в соот-и с разрядностью множителя

    for i in range(len(fact)):
        for j in range(i):
            fact[i].append('0')
    # print(fact)
    mult_total = reduce(sum_hex, fact)

    return mult_total

print('Сумма введенных чисел:')
print(sum_hex(a, b))  # deque(['C', 'F', '1'])
print("для проверки:")
print(deque(hex(int(a, 16) + int(b, 16)).split('0x')[-1].upper()))

print('Произведение введенных чисел:')
print(mult_hex(a, b))
print("для проверки:")

print(deque(hex(int(a, 16) * int(b, 16)).split('0x')[-1].upper()))

f = sum_hex(a, b)
s = deque(hex(int(a, 16) * int(b, 16)).split('0x')[-1].upper())

