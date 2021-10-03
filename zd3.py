#!/usr/bin/env python3\
# -*- coding: utf-8 -*-

def f():
    proizv = 1
    while True:
        mnogitel = int(input("Введите множитель: "))
        proizv *= mnogitel
        if mnogitel == 0:
            print("Произведение = 0")
            break
        else:
            print(f"Произведение = {proizv}")


if __name__ == '__main__':
    f()
