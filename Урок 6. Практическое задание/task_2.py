"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""

from pympler import asizeof


def convert(*args):
    table = '0123456789ABCDEF'
    if args[0] < 16:
        return table[args[0]]
    x, y = divmod(args[0], 16)
    return f'{convert(x)}{table[y] if x else table[y]}'


if __name__ == '__main__':
    print(asizeof.asizeof(convert(113**113)))

    """
    Основная проблема при замере через модуль memory_profiler
    в том, что чем больше происходит рекурсивных вызовов, тем 
    больше выводится информации. Функция asizeof модуля asizeof
    библиотеки pympler оценивает занимаемую память как самой получаемой 
    на вход структуры данных, но и все входящие в нее. А так как в питоне
    все есть объект, то она отлично подходит
    """
