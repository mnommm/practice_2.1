try:
    with open('resource/text.txt', 'w', encoding='utf-8') as file:
        lines = [
            "Это первая строка в файле",
            "Это вторая строка в файле",
            "Это треться строка в файле",
            "Это четвертая строка в этом файле",
            "Это пятая строка финальная"
        ]
        for line in lines:
            file.write(line + '\n')
    print("Файл 'resource/text.txt' успешно создан и заполнен 5 строками")

    with open('resource/text.txt', 'r', encoding='utf-8') as file:
        content = file.readlines()

    clean_content = [line.strip() for line in content]

    line_count = len(content)

    word_count = sum(len(line.split()) for line in clean_content)

    longest_line = max(clean_content, key=len) if clean_content else ""
    longest_length = len(longest_line)

    print("\nРЕЗУЛЬТАТЫ ПРОГРАММЫ")
    print("\n")
    print(f"1. Количество строк в файле: {line_count}")
    print(f"2. Количество слов в файле: {word_count}")
    print(f"3. Самая длинная строка ({longest_length} символов):")
    print(f"   \"{longest_line}\"")

except FileNotFoundError:
    print("Ошибка: Не удалось создать или прочитать файл!")
except PermissionError:
    print("Ошибка: Нет прав доступа к файлу!")
except Exception as e:
    print(f"Непредвиденная ошибка: {e}")