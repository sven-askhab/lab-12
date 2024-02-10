#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import timeit
import functools


def factorial_iterative(n):
    """
    Итеративное вычисление факториала
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial_recursive(n):
    """
    Вычисление факториала с помощью рекурсии
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)


def fib_iterative(n):
    """
    Итеративное вычисление чисел фибоначи 
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fib_recursive(n):
    """
    Вычисление чисел фибоначи с помощью рекурсии
    """
    if n <= 1:
        return n
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)


@functools.lru_cache(maxsize=None)
def fib_recursive_cached(n):
    """
    Вычисление чисел фибоначи с использованием декоратора
    """
    if n <= 1:
        return n
    else:
        return fib_recursive_cached(n - 1) + fib_recursive_cached(n - 2)


@functools.lru_cache(maxsize=None)
def factorial_recursive_cached(n):
    """
    Вычисление факториала с использованием декоратора
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)


def main():
    """
    Основная функция программы
    """
    func_time = timeit.timeit(
        "factorial_iterative(20)", 
        globals=globals(), 
        number = 1000
    )
    print("Время выполнения итеративной функции factorial:", func_time)

    func_time = timeit.timeit(
        "factorial_recursive(20)", 
        globals=globals(), 
        number = 1000
    )
    print("Время выполнения рекурсивной функции factorial:", func_time)

    func_time = timeit.timeit(
        "fib_iterative(20)", 
        globals=globals(), 
        number = 1000
    )
    print("Время выполнения итеративной функции fib:", func_time)

    func_time = timeit.timeit(
        "fib_recursive(20)", 
        globals=globals(), 
        number = 1000
    )
    print("Время выполнения рекурсивной функции fib:", func_time)

    func_time = timeit.timeit(
        "fib_recursive_cached(20)", 
        globals=globals(), 
        number = 1000
    )
    print("Время работы рекурсивной функции fib с декоратором:", func_time)

    func_time = timeit.timeit(
        "factorial_recursive_cached(20)", 
        globals=globals(), 
        number = 1000
    )
    print("Время работы рекурсивной функции factorial с декор.:", func_time)


if __name__ == "__main__":
    main()