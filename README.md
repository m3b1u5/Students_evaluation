# ДЗ: Практическое задание

Задача: Создание программы для анализа и обработки списка студентов и их оценок

Вам предстоит создать программу, которая будет анализировать список студентов и их оценок. Программа должна уметь вычислять средний балл каждого студента, определять успешных и отстающих, а также выводить информацию в удобном формате. 

Требования:

1. Создайте список студентов. Каждый студент представлен словарём, содержащим имя и список его оценок.


2. Напишите цикл, который пройдётся по каждому студенту и рассчитает его средний балл.

Создайте функцию `calculate_average(grades)`, которая принимает список оценок и возвращает среднее значение.
 Используйте эту функцию внутри цикла для вычисления среднего балла каждого студента.
3. Определите, является ли студент успешным или отстающим. Считайте, что студент успешен, если его средний балл выше или равен 75. Добавьте логическое выражение, которое проверяет это условие, и выводит соответствующее сообщение.

4. Выведите для каждого студента сообщение следующего формата:

    Студент: Harry
    Средний балл: 84.33
    Статус: Успешен

   - Используйте f-строки для форматирования вывода.

5. Рассчитайте общий средний балл по всем студентам и выведите его.

6. Добавьте нового студента в список, используя метод `append`. Удалите студента с самым низким средним баллом из списка.
 7. Список всех студентов должен пересчитываться каждый раз, когда обновляется список. Можно вынести код для этого в отдельную функцию. 