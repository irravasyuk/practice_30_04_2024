# Завдання 1
# Користувач вводить з клавіатури значення у список.
# Після чого запускаються два потоки. Перший потік знаходить
# максимум у списку. Другий потік знаходить мінімум
# у списку. Результати обчислень виведіть на екран.
# import threading
#
# def max_num(numbers):
#     max_number = max(numbers)
#     print(f'Максимум в списку: {max_number}')
#
# def min_num(numbers):
#     min_number = min(numbers)
#     print(f'Мінімум в списку: {min_number}')
#
# if __name__ == "__main__":
#     numbers = input("Введіть значення через пробіл у список: ").split()
#
#     numbers = [int(num) for num in numbers]
#
#     max_thread = threading.Thread(target=max_num, args=(numbers,))
#     min_thread = threading.Thread(target=min_num, args=(numbers,))
#
#     max_thread.start()
#     min_thread.start()
#
#     max_thread.join()
#     min_thread.join()


# Завдання 2
# Користувач вводить з клавіатури значення у список.
# Після чого запускаються два потоки. Перший потік знаходить суму
# елементів у списку. Другий потік знаходить
# середнє арифметичне у списку. Результати обчислень
# виведіть на екран.
# import threading
#
# def summa_num(numbers):
#     summa = sum(numbers)
#     print(f'Сума чисел: {summa}')
#
# def mean(numbers):
#     mean_num = sum(numbers) / len(numbers)
#     print(f"Середнє арифметичне чисел {mean_num}")
#
# if __name__ == "__main__":
#     numbers = input("Введіть значення через пробіл у список: ").split()
#
#     numbers = [int(num) for num in numbers]
#
#     summa_thread = threading.Thread(target=summa_num, args=(numbers,))
#     mean_thread = threading.Thread(target=mean, args=(numbers,))
#
#     summa_thread.start()
#     mean_thread.start()
#
#     summa_thread.join()
#     mean_thread.join()



# Завдання 3
# Користувач вводить з клавіатури шлях до файлу, що
# містить набір чисел. Після чого запускаються два потоки.
# Перший потік створює новий файл, в який запише лише
# парні елементи списку. Другий потік створює новий файл,
# в який запише лише непарні елементи списку. Кількість
# парних і непарних елементів виводиться на екран.
import threading
import json

def even_num(numbers, filename):
    even_list = [num for num in numbers if num % 2 == 0]
    with open(filename, 'w') as f:
        json.dump(even_list, f)
    print(f"Кількість записаних парних елементів: {len(even_list)}")

def odd_num(numbers, filename):
    odd_list = [num for num in numbers if num % 2 != 0]
    with open(filename, 'w') as f:
        json.dump(odd_list, f)
    print(f"Кількість записаних непарних елементів: {len(odd_list)}")

def read_numbers(filename):
    with open(filename, 'r') as f:
        numbers = json.load(f)
    return numbers

filename = input('Введіть шлях до файлу: ')
even_file = input('Введіть шлях до файлу з парними числами:')
odd_file = input('Введіть шлях до файлу з непарними числами:')

numbers = read_numbers(filename)

even_file = open(even_file, 'w')
odd_file = open(odd_file, 'w')

t1 = threading.Thread(target=even_num, args=(numbers, even_file))
t2 = threading.Thread(target=odd_num, args=(numbers, odd_file))

t1.start()
t2.start()

t1.join()
t2.join()
















