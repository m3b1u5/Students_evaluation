# ДЗ: Практическое задание


def calculate_average(grades):
    return sum(grades) / len(grades)


def print_students(students):
    for student in students:
        print(f"""
Студент: {student["name"]}
Средний балл: {student["score_average"]}
Статус: {student["is_success"]}""")
    print(f"\nОбщий средний балл всех студентов: {total_average_score(students)}\n" + "_" * 50)


def total_average_score(students):
    average = 0
    for student in students:
        average += student["score_average"]
    return average / len(students)


def update_students(students):
    for student in students:
        average_score = calculate_average(student["grades"])
        student["score_average"] = average_score
        student["is_success"] = "Успешен" if average_score >= 75 else "Не успешен"
    print_students(students)


def remove_lowest_score(students):
    lowest_score = float('inf')
    index = None
    for i, val in enumerate(students):
        if val["score_average"] < lowest_score:
            lowest_score = val["score_average"]
            index = i
    if index is not None:
        print(f"\nСтудент {students[index]['name']} Отчисляется за наименьший средний балл.")
        students.pop(index)


def main():
    students = [
        {"name": "Harry", "grades": [80, 90, 78]},
        {"name": "Hermione", "grades": [95, 90, 97]},
        {"name": "Ron", "grades": [60, 70, 64]},
        {"name": "Draco", "grades": [60, 75, 70]},
    ]
    print("\nСписок студентов: ")
    update_students(students)

    students.append({"name": "Denys", "grades": [99, 99, 99]})
    print("\nПрибывает новый студент: ")
    update_students(students)

    remove_lowest_score(students)
    update_students(students)


main()
