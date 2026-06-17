import datetime
import os

LOG_FILE = 'resource/calculator.log'


def show_last_operations():
    try:
        with open(LOG_FILE, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            if lines:
                print("\n----ПОСЛЕДНИЕ 5 ОПЕРАЦИЙ----")
                for line in lines[-5:]:
                    print(line.strip())
            else:
                print("Лог-файл пуст")
    except FileNotFoundError:
        print("Лог-файл еще не создан")


def write_to_log(operation):
    os.makedirs('resource', exist_ok=True)
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(operation + '\n')


def clear_log():
    open(LOG_FILE, 'w', encoding='utf-8').close()
    print("Лог-файл очищен!")


def calculate(num1, num2, op):
    if op == '+': return num1 + num2
    if op == '-': return num1 - num2
    if op == '*': return num1 * num2
    if op == '/':
        if num2 == 0: raise ValueError("Деление на ноль!")
        return num1 / num2
    raise ValueError("Неверная операция!")


def main():
    print("\n")
    print("КАЛЬКУЛЯТОР С ЛОГИРОВАНИЕМ")
    print("\n")

    show_last_operations()

    while True:
        print("\n1 - Вычислить | 2 - Очистить лог | 3 - Выйти")
        choice = input("Выбор: ").strip()

        if choice == '1':
            try:
                num1 = float(input("Первое число: "))
                num2 = float(input("Второе число: "))
                op = input("Операция (+, -, *, /): ").strip()

                result = calculate(num1, num2, op)
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                log_entry = f"[{timestamp}] {num1} {op} {num2} = {result}"

                write_to_log(log_entry)
                print(f"\nРезультат: {num1} {op} {num2} = {result}")

            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == '2':
            if input("Очистить лог? (да/нет): ").lower() == 'да':
                clear_log()
                show_last_operations()

        elif choice == '3':
            print("Программа завершена")
            break

        else:
            print("Ошибка: введите 1, 2 или 3")


if __name__ == "__main__":
    main()