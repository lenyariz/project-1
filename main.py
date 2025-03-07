from datetime import datetime

product = ""
product_list = {}
total_cost = {}
while product.lower() != "стоп":
    product = input("Введите продукт: ")
    if len(product.split(":")) != 3 or not product.split(":")[1].isdigit() or product.split(":")[0].isdigit() or product.split(":")[2].isdigit():
        if product != "стоп":
            print("Ошибка, данные не подходят, пропускаю...")
        continue
    if product.split(":")[2] not in product_list:
        product_list[product.split(":")[2]] = []
    product_list[product.split(":")[2]].append((product.split(":")[0], int(product.split(":")[1])))

temp_cost = 0
for key, value in product_list.items():
    for price in value:
        temp_cost += price[1]
    total_cost[key] = (temp_cost, temp_cost / len(value))

print("\n--------------------ОБЩИЕ ДАННЫЕ-----------------------")
print(f"Общее количество покупок: {sum([len(product) for product in product_list.values()])}")
print(f"Общая сумма расходов: {sum([price[1] for product in product_list.values() for price in product])}")
print(f"Среднее значение по всем категориям: {sum([price[1] for product in product_list.values() for price in product]) / sum([len(product) for product in product_list.values()])}")
print("\n--------------------ДАННЫЕ ПО КАЖДОЙ КАТЕГОРИИ-----------------------")
for key, value in product_list.items():
    print(f"Категория: {key.capitalize()}")
    print(f"Список покупок: {value}")
    print(f"Суммарная стоимость: {total_cost[key][0]}")
    print(f"Среднее значение покупок: {total_cost[key][1]}")
    print("---------------------------------------------------")
print(f"Дата отчёта: {datetime.now().strftime("%d.%m.%Y %H:%M")}")