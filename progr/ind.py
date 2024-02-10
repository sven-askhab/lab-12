#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def reverse_print():
    """
    Принимает последовательность чисел и выводит их в обратном порядке
    """
    number = int(input("Введите число: "))
    if number != 0:
        reverse_print()
        print(number, end=' ')


if __name__ == "__main__":
    reverse_print()
