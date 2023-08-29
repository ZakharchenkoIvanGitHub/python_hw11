"""
Задание №1
📌 Создайте класс Моя Строка, где:
📌 будут доступны все возможности str
📌 дополнительно хранятся имя автора строки и время создания
(time.time)
"""

import time
from datetime import datetime


class MyStr(str):
    """
    класс Моя Строка, где:
    доступны все возможности str
    дополнительно хранятся имя автора строки и время создания
    """
    def __new__(cls, value, author_name):
        my_srt = super().__new__(cls, value)
        my_srt.author_name = author_name
        my_srt.value = value
        my_srt.creation_time = datetime.now()
        return my_srt

    def __str__(self):
        return f'автор: {self.author_name}, время создания: {self.creation_time} \n{self.value}'


if __name__ == '__main__':
    s = MyStr('Новая Строка Теста', 'Sergey')
    l = MyStr('Новая ', 'Leonid')

    print(s)
    print(l)
