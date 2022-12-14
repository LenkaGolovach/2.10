#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Напишите функцию, принимающую произвольное количество аргументов, и возвращающую требуемое значение.
Если функции передается пустой список аргументов, то она должна возвращать значение None.
В процессе решения не использовать преобразования конструкции *args в список или иную структу-ру данных.
Сумму аргументов, расположенных после последнего аргумента, равного нулю.
"""


def proiz(*args):
    if args:
        last_index = len(args) - 1 - args[::-1].index(0)
        return sum(args[last_index + 1:])
    else:
         return None


if __name__ == "__main__":
    print(proiz(10, 0, 3, 4, 0, 5, 6))
