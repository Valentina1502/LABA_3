#!/usr/bin/env python3\
# -*- coding: utf-8 -*-

def test_input(mes):
    try:
        str_to_int(mes)
    except ValueError:
        print("Строку не преобразовать в число")


def str_to_int(mes):
    i = int(mes)
    print_int(i)


def print_int(i):
    print(i)


def get_input():
    mes = input("Введите строку: ")
    test_input(mes)


if __name__ == '__main__':
    get_input()
