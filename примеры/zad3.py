#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Дано время сна студентов в ночь с пятницы на субботу в виде ключ-значения.
Определить лучшее время сна и среднее время сна среди всех студентов группы.
"""


def son(**keywords):
    summa = 0
    n = len(keywords)
    max = keywords["Вова"]
    for kw in keywords:
        summa = summa + keywords[kw]
        if keywords[kw] > max:
            max = keywords[kw]
    print("Лучшее время сна:", max)
    print("Среднее время сна среди всех студентов - ", summa / n)


if __name__ == "__main__":
    son(
        Вова=0.5,
        Вася=5.6,
        Максим=1.2,
        Саша=5.3,
        Дина=7.8,
        Коля=3.7,
    )