"""
Задание №2
📌 Создайте класс Архив, который хранит пару свойств.
Например, число и строку.
📌 При нового экземпляра класса, старые данные из ранее
созданных экземпляров сохраняются в пару списков-
архивов
📌 list-архивы также являются свойствами экземпляра
"""


class Archive:
    """
    Класс Архив, который хранит пару свойств.
    Например, число и строку.
    При нового экземпляра класса, старые данные из ранее
    созданных экземпляров сохраняются в пару списков-архивов
    """
    nums_archive = []
    strs_archive = []
    last_num = None
    last_str = None

    def __init__(self, num, new_str):
        self.num = num
        self.new_str = new_str

        if Archive.last_num is not None:
            Archive.nums_archive.append(Archive.last_num)
        if Archive.last_str is not None:
            Archive.strs_archive.append(Archive.last_str)

        Archive.last_num = num
        Archive.last_str = new_str

    def __str__(self):
        return f"{self.num}, {self.new_str}, {self.nums_archive}, {self.strs_archive}"


if __name__ == '__main__':
    arc1 = Archive(1, "Строка 1")
    print(arc1)

    arc2 = Archive(2, "Текст 2")
    print(arc2)

    arc3 = Archive(3, "Symbols 3")
    print(arc3)
