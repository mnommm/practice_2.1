import json

FILE = 'resource/library.json'


def load_books():
    try:
        with open(FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_books(books):
    with open(FILE, 'w', encoding='utf-8') as f:
        json.dump(books, f, ensure_ascii=False, indent=2)
    print("Данные сохранены!")


def show_all(books):
    if not books:
        print("Библиотека пуста")
        return
    print("\n----ВСЕ КНИГИ----")
    for book in books:
        status = "Доступна" if book['available'] else "Выдана"
        print(f"ID:{book['id']} | {book['title']} | {book['author']} | {book['year']} | {status}")


def search(books):
    query = input("Введите автора или название: ").strip().lower()
    results = [b for b in books if query in b['title'].lower() or query in b['author'].lower()]

    if results:
        print(f"\nНайдено {len(results)} книг:")
        for book in results:
            status = "Доступна" if book['available'] else "Выдана"
            print(f"ID:{book['id']} | {book['title']} | {book['author']} | {book['year']} | {status}")
    else:
        print("Ничего не найдено")


def add_book(books):
    print("\n----ДОБАВЛЕНИЕ КНИГИ----")
    title = input("Название: ").strip()
    author = input("Автор: ").strip()
    try:
        year = int(input("Год издания: "))
    except ValueError:
        print("Ошибка: год должен быть числом")
        return

    new_id = max([b['id'] for b in books], default=0) + 1

    books.append({
        "id": new_id,
        "title": title,
        "author": author,
        "year": year,
        "available": True
    })
    print(f"Книга '{title}' добавлена с ID {new_id}")
    save_books(books)


def toggle_status(books):
    try:
        book_id = int(input("Введите ID книги: "))
    except ValueError:
        print("Ошибка: ID должен быть числом")
        return

    for book in books:
        if book['id'] == book_id:
            book['available'] = not book['available']
            status = "доступна" if book['available'] else "выдана"
            print(f"Статус книги '{book['title']}' изменен на {status}")
            save_books(books)
            return
    print("Книга с таким ID не найдена")


def delete_book(books):
    try:
        book_id = int(input("Введите ID книги для удаления: "))
    except ValueError:
        print("Ошибка: ID должен быть числом")
        return

    for i, book in enumerate(books):
        if book['id'] == book_id:
            confirm = input(f"Удалить книгу '{book['title']}'? (да/нет): ")
            if confirm.lower() == 'да':
                del books[i]
                print("Книга удалена")
                save_books(books)
            return
    print("Книга с таким ID не найдена")


def export_available(books):
    available = [b for b in books if b['available']]
    if not available:
        print("Нет доступных книг для экспорта")
        return

    with open('resource/available_books.txt', 'w', encoding='utf-8') as f:
        f.write("Список доступных книг:\n")
        f.write("-" * 40 + "\n")
        for book in available:
            f.write(f"{book['title']} - {book['author']} ({book['year']})\n")

    print(f"Экспортировано {len(available)} книг в resource/available_books.txt")


def main():
    books = load_books()

    while True:
        print("\n")
        print("БИБЛИОТЕЧНАЯ СИСТЕМА")
        print("\n")
        print("1 - Показать все книги")
        print("2 - Поиск по автору/названию")
        print("3 - Добавить книгу")
        print("4 - Изменить статус (взята/возвращена)")
        print("5 - Удалить книгу по ID")
        print("6 - Экспорт доступных книг")
        print("7 - Выход")

        choice = input("\nВыберите действие (1-7): ").strip()

        if choice == '1':
            show_all(books)
        elif choice == '2':
            search(books)
        elif choice == '3':
            add_book(books)
            books = load_books()
        elif choice == '4':
            toggle_status(books)
            books = load_books()
        elif choice == '5':
            delete_book(books)
            books = load_books()
        elif choice == '6':
            export_available(books)
        elif choice == '7':
            print("Программа завершена")
            break
        else:
            print("Ошибка: введите число от 1 до 7")


if __name__ == "__main__":
    main()