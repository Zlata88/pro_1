accumulations = []
 print('введите ваши месячные расходы за последние 6 месяцев')
 for 1 in range(6):
 income = int(input('введите ЗП: '))
 accumulations.append(income*0.3)
print('accumulations')
 print('ваши накопления составят', sum(accumulations))

