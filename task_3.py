import csv

FILE = 'resource/products.csv'

data = [
    ['Название', 'Цена', 'Количество'],
    ['Яблоки', 100, 50],
    ['Бананы', 80, 30],
    ['Молоко', 120, 20],
    ['Хлеб', 40, 100]
]

with open(FILE, 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)

print("Файл создан!")


def load():
    products = []
    try:
        with open(FILE, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                products.append({
                    'Название': row['Название'],
                    'Цена': int(row['Цена']),
                    'Количество': int(row['Количество'])
                })
        print(f"Загружено {len(products)} товаров")
    except FileNotFoundError:
        print("Файл не найден, создается новый")
    return products


def save(products):
    with open(FILE, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['Название', 'Цена', 'Количество'])
        writer.writeheader()
        writer.writerows(products)
    print("Сохранено!")


def add(products):
    print("\n----ДОБАВЛЕНИЕ----")
    name = input("Название: ").strip()
    for p in products:
        if p['Название'].lower() == name.lower():
            print("Ошибка: товар уже есть!")
            return

    try:
        price = int(input("Цена: "))
        qty = int(input("Количество: "))
        if price < 0 or qty < 0:
            print("Ошибка: цена и количество не могут быть отрицательными")
            return
        products.append({'Название': name, 'Цена': price, 'Количество': qty})
        print(f"Товар '{name}' добавлен!")
    except ValueError:
        print("Ошибка: введите числа!")


def search(products):
    print("\n----ПОИСК----")
    name = input("Название: ").strip()
    for p in products:
        if p['Название'].lower() == name.lower():
            print(f"\n{p['Название']}")
            print(f"Цена: {p['Цена']} руб.")
            print(f"Количество: {p['Количество']} шт.")
            return
    print("Товар не найден")


def total(products):
    print("\n----ОБЩАЯ СТОИМОСТЬ----")
    if not products:
        print("Нет товаров")
        return
    summ = sum(p['Цена'] * p['Количество'] for p in products)
    print(f"Всего на складе: {summ} руб.")
    print("\nДетализация:")
    for p in products:
        cost = p['Цена'] * p['Количество']
        print(f"{p['Название']}: {p['Цена']} x {p['Количество']} = {cost} руб.")


def show(products):
    print("\n----ВСЕ ТОВАРЫ----")
    if not products:
        print("Список пуст")
        return
    print(f"{'Название':<12} {'Цена':<6} {'Кол-во':<6} Стоимость")
    print("-" * 40)
    for p in products:
        cost = p['Цена'] * p['Количество']
        print(f"{p['Название']:<12} {p['Цена']:<6} {p['Количество']:<6} {cost}")


def main():
    print("\n")
    print("УПРАВЛЕНИЕ СКЛАДОМ")
    print("\n")

    products = load()

    while True:
        print("\n1 - Показать все")
        print("2 - Добавить товар")
        print("3 - Поиск товара")
        print("4 - Общая стоимость")
        print("5 - Сохранить и выйти")

        choice = input("\nВыберите действие (1-5): ")

        if choice == '1':
            show(products)
        elif choice == '2':
            add(products)
        elif choice == '3':
            search(products)
        elif choice == '4':
            total(products)
        elif choice == '5':
            save(products)
            print("Программа завершена")
            break
        else:
            print("Ошибка: введите 1-5")


if __name__ == "__main__":
    main()