''' Пользоваьель вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала для каждого предприятия.
программа должна определить среднюю прибыль и отдельно вывести наименования предприятий,
чья прибыль выше среднего и ниже среднего'''
from collections import namedtuple
enterprise_number = int(input('Введите количество предприятий '))


Enterprise = namedtuple('Enterprise', ['name', 'profit_1', 'profit_2', 'profit_3', 'profit_4', 'total_profit', 'avg_profit'])

list_enterprise = []

for i in range(enterprise_number):
    name = input('Введите имя организации ')
    profit_1 = float(input(f'Введите прибыль {name} за 1 квартал '))
    profit_2 = float(input(f'Введите прибыль {name} за 2 квартал '))
    profit_3 = float(input(f'Введите прибыль {name} за 3 квартал '))
    profit_4 = float(input(f'Введите прибыль {name} за 4 квартал '))
    total_profit = profit_1 + profit_2 + profit_3 + profit_4
    avg_profit = total_profit / 4
    list_enterprise.append(Enterprise(name, profit_1, profit_2, profit_3, profit_4, total_profit, avg_profit))





total = 0  # посчитаем общую сумму дохода по всем предприятиям

for i in range(enterprise_number):
    total += list_enterprise[i].total_profit


# определим средний доход
avg = total / 4 / enterprise_number

print(f'Средняя прибыль предприятий = {avg}')

sub_avg = []
over_avg = []
for i in range(enterprise_number):
    if list_enterprise[i].avg_profit > avg:
        over_avg.append(list_enterprise[i].name)
    else:
        sub_avg.append(list_enterprise[i].name)

print(f'Предприятия, чья прибыль выше среднего {", ".join(over_avg)}')
print(f'Предприятия, чья прибыль ниже или равна среднему {", ".join(sub_avg)}')







