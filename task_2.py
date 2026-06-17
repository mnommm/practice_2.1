try:
    print("Чтение файла 'resource/students.txt'")
    with open('resource/students.txt', 'r', encoding='utf-8') as file:
        students_data = file.readlines()

    results = []
    best_student = None
    best_score = -1

    for line in students_data:
        line = line.strip()

        if line:
            name, grades_str = line.split(':')

            grades_list = grades_str.split(',')
            grades = []
            for grade in grades_list:
                grades.append(int(grade))

            average = sum(grades) / len(grades)
            results.append((name, average))

            if average > best_score:
                best_score = average
                best_student = name

    print("Запись результатов в 'resource/result.txt'")
    with open('resource/result.txt', 'w', encoding='utf-8') as file:
        filtered_count = 0
        for name, avg in results:
            if avg > 4.0:
                file.write(f"{name}: {avg:.2f}\n")
                filtered_count += 1

        if filtered_count == 0:
            file.write("Нет студентов со средним баллом выше 4.0\n")

    print("\n")
    print("РЕЗУЛЬТАТЫ ПРОГРАММЫ:")
    print("\n")

    for name, avg in results:
        status = "Выше 4.0" if avg > 4.0 else "Ниже 4.0"
        print(f"{status}: {name} - {avg:.2f}")

    print(f"\nВ файл 'resource/result.txt' добавлено {filtered_count} студентов")

    if best_student:
        print(f"Студент с наивысшим средним баллом: {best_student} ({best_score:.2f})")
    else:
        print("Нет данных о студентах")

except FileNotFoundError:
    print("Ошибка: Файл 'resource/students.txt' не найден!")
    print("Убедитесь, что файл существует в папке resource")
except ValueError:
    print("Ошибка: Неверный формат данных в файле!")
    print("Проверьте, что оценки записаны числами через запятую")
except Exception as e:
    print(f"Непредвиденная ошибка: {e}")