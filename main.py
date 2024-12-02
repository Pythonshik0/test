# coding=utf-8
from __future__ import division
from collections import deque
import time
import random


#  ------------1 Задание---(Работает Python 2.7)----------------------------------------------------- -*-
def isEven1(value):
    """
    Если разделенное число равно округленному разделенному числу, то функция вернёт True.
    Если нет - выведет False.

    ПЛЮСЫ: Работает для всех чисел
           Для случаев, где операции с остатками (%) недоступны (редко), этот метод может быть использован как альтернативный.
    МИНУС: Медленнее из-за дробной арифметики:
           Операция деления (/) с последующим сравнением с целым числом требует преобразования числа в float (даже если это целое число).
           Это делает функцию менее производительной, чем проверка через %.
    """
    dev_number = value / 2  # Деление
    int_number = int(dev_number)
    return int_number == dev_number


def isEven2(value):
    """
    ПЛЮС: Быстрее, так как операция битового AND — одна из самых быстрых.
    МИНУС: Требует целого числа, не работает с вещественными типами.
    """
    return (value & 1) == 0


print(isEven1(5)) # Выведет False
print(isEven2(4)) # Выведет True


#------------2 Задание--------------------------------------------------------

class CircularBufferList(object):
    def __init__(self, size):
        if size <= 0:
            raise ValueError("Размер буфера должен быть больше 0")
        self.buffer = [None] * size
        self.size = size
        self.head = 0
        self.tail = 0
        self.is_full = False

    def append(self, item):
        """Добавление элемента в буфер."""
        self.buffer[self.tail] = item
        self.tail = (self.tail + 1) % self.size
        if self.is_full:
            self.head = (self.head + 1) % self.size
        elif self.tail == self.head:
            self.is_full = True

    def pop(self):
        """Удаление элемента из буфера."""
        if self.is_empty():
            raise IndexError("Буфер пуст")
        item = self.buffer[self.head]
        self.buffer[self.head] = None  # Необязательно, для чистоты
        self.head = (self.head + 1) % self.size
        self.is_full = False
        return item

    def is_empty(self):
        return not self.is_full and self.head == self.tail

    def __repr__(self):
        return "CircularBufferList({})".format(self.buffer)



class CircularBufferDeque(object):
    def __init__(self, size):
        if size <= 0:
            raise ValueError("Размер буфера должен быть больше 0")
        self.buffer = deque(maxlen=size)

    def append(self, item):
        """Добавление элемента в буфер."""
        self.buffer.append(item)

    def pop(self):
        """Удаление элемента из буфера."""
        if self.is_empty():
            raise IndexError("Буфер пуст")
        return self.buffer.popleft()

    def is_empty(self):
        return len(self.buffer) == 0

    def __repr__(self):
        return "CircularBufferDeque({})".format(list(self.buffer))


buf1 = CircularBufferList(3)
buf1.append(1)
buf1.append(2)
buf1.append(3)
print(buf1)  # CircularBufferList([1, 2, 3])
buf1.append(4)
print(buf1)  # CircularBufferList([4, 2, 3])
print(buf1.pop())  # 2
print(buf1)  # CircularBufferList([4, None, 3])

buf2 = CircularBufferDeque(3)
buf2.append(1)
buf2.append(2)
buf2.append(3)
print(buf2)  # CircularBufferDeque([1, 2, 3])
buf2.append(4)
print(buf2)  # CircularBufferDeque([2, 3, 4])
print(buf2.pop())  # 2
print(buf2)  # CircularBufferDeque([3, 4])

"""
Выводы
CircularBufferList:

Плюсы: Подходит для работы с большими фиксированными буферами, где важна оптимизация памяти.
Минусы: Сложная реализация, требуется контроль индексов, возможны ошибки.
CircularBufferDeque:

Плюсы: Простота реализации, встроенная поддержка FIFO и ограниченного размера.
Минусы: Чуть больше overhead на управление памятью, менее производительно на больших буферах.
"""

# Для общего использования рекомендован deque,
# так как он проще в реализации и более универсален.


#----------Задание 3----------------------------------------------------------
def sort_array(arr_num):
    """
    Сортирует массив чисел с использованием встроенного метода .sort(),
    который реализует алгоритм Timsort.
    """
    arr_num.sort()
    return arr_num


arr = [random.randint(1, 100000) for _ in range(100000)] # Генерация случайного массива


start_time = time.time()
sort_array(arr)
print("Время выполнения:", time.time() - start_time)

"""
Вывод: Для сортировки массива чисел на Python 2.7 наиболее быстрым алгоритмом в среднем случае является Timsort, 
который используется в встроенной функции sorted() и методе .sort() списка. 
Этот алгоритм был разработан для обеспечения высокой производительности на реальных данных и сочетает в себе преимущества сортировки вставкой и слияния.
"""