# Входные данные
purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]

# Функция подсчета общей выручки
def total_revenue(pur: list):
    # Переменная для результата
    revenue = 0
    # Проход по каждому элементу списка
    for item in pur:
        # Увеличение общей выручки от каждой продажи
        revenue += item["quantity"]*item["price"]
    return f"Общая выручка: {revenue}"

# Функция формирования словаря с распределением товаров по категориям
def items_by_category(pur: list):
    # Создание словаря
    result = {}
    # Проход по каждому элементу списка
    for item in pur:
        # Переменная для категории текущего товара
        cur_category = item["category"]
        # Если такая категория уже есть в словаре, то добавить в список текущий элемент
        if cur_category in result:
            result[cur_category].append(item["item"])
        # Если категории нет, то добавить категорию и к нему элемент
        else:
            result[cur_category] = [item["item"]]
    return f"Товары по категориям: {result}"

# Функция определения покупок товаров дороже min_price
def expensive_purchases(pur: list, min_price: float):
    # Создание списка
    result = []
    # Проход по каждому элементу списка
    for item in pur:
        # Если цена выше или равна min_price, то добавить покупку в результат
        if item["price"] >= min_price:
            result.append(item)
    return f"Покупки дороже {min_price}: {result}"

# Функция определения средней цены товаров в каждой категории
def average_price_by_category(pur: list):
    # Создание словаря
    result = {}
    # Проход по каждому элементу списка
    for item in pur:
        # Переменная для категории текущего товара
        cur_category = item["category"]
        # Если такая категория уже есть в словаре, то посчитать среднюю цену с учетом текущего товара
        if cur_category in result:
            result[cur_category] = (result[cur_category] + item["price"]) / 2
        # Если категории нет, то добавить категорию и к нему цену текущего товара
        else:
            result[cur_category] = item["price"]
    return f"Средняя цена по категориям: {result}"

# Функция поиска категория с наибольшим количеством товаров
def most_frequent_category(pur: list):
    # Создание словаря
    result = {}
    # Проход по каждому элементу списка
    for item in pur:
        # Переменная для категории текущего товара
        cur_category = item["category"]
        # Если такая категория уже есть в словаре, то увеличить значение на 1
        if cur_category in result:
            result[cur_category] += 1
        # Если категории нет, то добавить категорию и значение указать 1
        else:
            result[cur_category] = 1

    # Создание переменных для определение самой частой категории
    most_fr_category = ''
    max_count = 0
    # Проход по каждому ключу и значению в словаре
    for key, value in result.items():
        # Если значение выше текущего максимума, то считать категорию самой популярной
        if value > max_count:
            most_fr_category = key
            max_count = value
    return f"Категория с наибольшим количеством проданных товаров: {most_fr_category}"

# Вывод результатов
print(total_revenue(purchases))
print(items_by_category(purchases))
print(expensive_purchases(purchases, 1.0))
print(average_price_by_category(purchases))
print(most_frequent_category(purchases))