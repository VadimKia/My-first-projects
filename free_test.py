# Только учусь, мало что знаю, мой первій раз:
# кратенькое описание:
print("Вы, клиент, который пришел в кафе и заказал стандартную пиццу. Теперь с помощью диалогового окна Вам необходимо выбрать добавки (начинку) для пиццы.")

# Составляем словарь ингредиентов для пиццы:
pizza = {
	'crust': 'тонким',
	'toppings': ['Грибы', 'Бекон', 'Супер сыр'],
}

# Составляем список заказа:
order_pizza = []


# Создаем наборы подсказок для древа выбора:

choices_order = f"\nВы заказали пиццу с {pizza['crust'].title()} тестом."
choices_order += "\nВыберите добавки для своей пиццы из списка:"
choices_order += f"\t{pizza['toppings']}"
choices_order += "\n(Если вы закончили: введите 'quit'\nЧтобы просмотреть весь заказ: введите 'мой заказ') "

next_adding_topping = "\nЧто вы хотите добавить в пиццу еще?"
next_adding_topping += "\nВведите добавку из списка:"
next_adding_topping += "\n(Если вы закончили: введите 'quit'\nЧтобы просмотреть весь заказ: введите 'мой заказ') "

already_added_to_pizza = "\nЭта добавка уже в заказе!"
already_added_to_pizza += "\nВыберите еще желанные добавки из списка:"
already_added_to_pizza += f"\n\t{pizza['toppings']}\n "

empty_order = "Ваш заказ пуст! \nВыберите добаку: "

wrong_order = "\nКакую добавку вы хотите? "

# Прописываем основной функционал:
while True:

# Начальный текст:
	order = input(choices_order)
#	order = order.lower()

# Проверка на повторность ввода ингридиентов
	if order in order_pizza:
		order = input(already_added_to_pizza)
		continue

# Проверка на завершение работы:
	elif order == 'quit':
		break 

# Проверка на соответствие ингридиентов и добавление их в список заказа
	elif order in pizza['toppings']:
		order_pizza.append(order)
		print(f"{order.title()} добавленна к вашей пицце")
		choices_order = next_adding_topping
		continue

# Проверка состояние текущего заказа
	elif order == 'мой заказ':
		for value in order_pizza:
			print(value)
		order = input(next_adding_topping)
		if order_pizza == []:
			order = input(empty_order)
		continue

# Проверка, если при введении команди допущена ошибка
	else:
		print(f"Твоя моя не понимать, сделайте выбор из следующего списка:")
		for value in pizza['toppings']:
			print(f"\t{value.title()}")
			choices_order = wrong_order
		continue 
