per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input("Введите сумму:"))
values_bank = list( per_cent.values())
deposit = [i * money / 100 for i in values_bank]
deposit = list(map(int,deposit))
max_deposit = max(deposit)
print(deposit)
print("Максимальная сумма, которую вы можете заработать —", max_deposit)

# print(values_bank)
