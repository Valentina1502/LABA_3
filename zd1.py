#!/urs/bin/env python3
# -*- coding^utf-8 -*-


def test():
    ch = int(input("Введите число: "))
    if ch < 0:
        negative(ch)
    elif ch > 0:
        positive(ch)
    else:
        print(f"Число {ch} = 0")


def positive(ch):
    print(f"Число положительное ({ch})")


def negative(ch):
    print(f"Число отрицательное ({ch})")


if __name__ == '__main__':
    test()
