#!/usr/bin/python3


from Context import Context
from Strategy import *
from Windows import MainWindowFactory


def start():
    window = MainWindowFactory().create_window()
    context = Context(FileStrategy('log.txt'))
    window.run(context)


if __name__ == '__main__':
    start()
