#!/usr/bin/python3

import enum
import PySimpleGUI as sg
from abc import ABC, abstractmethod


class Keys(enum.Enum):
    RESET_KEY = '-RESET-'
    INPUT_KEY = '-INPUT-'
    OPTION_KEY = '-OPTION-'
    RESULT_KEY = '-RESULT-'


class Window:
    def run(self):
        pass


class MainWindow(Window):
    def __init__(self):
        self.layout = [
            [sg.Text('Input time:')],
            [sg.Input(key=Keys.INPUT_KEY.value)],
            [sg.Button('Convert')],
            [sg.Button('Reset', key=Keys.RESET_KEY.value)]
        ]

    def run(self, context):
        window = sg.Window('Time', self.layout)
        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                break
            elif event == 'Convert':
                try:
                    int(values[Keys.INPUT_KEY.value])
                except:
                    context.send_message(f'The user entered a non-number: "{values[Keys.INPUT_KEY.value]}"')
                    continue
                context.send_message(f"User input: {values[Keys.INPUT_KEY.value]}")
                options_window = OptionsWindowFactory().create_window()
                options_window.run(values[Keys.INPUT_KEY.value], context)
            elif event == Keys.RESET_KEY.value:
                context.send_message(f"User has reset entered value")
                window[Keys.INPUT_KEY.value].update(value='')


class OptionsWindow(Window):
    def __init__(self):
        self.layout = [
            [sg.Text('Choose convert to:')],
            [sg.Combo(['Seconds in minutes', 'Minutes in hours', 'Hours in days'], key=Keys.OPTION_KEY.value,
                      default_value='Seconds in minutes')],
            [sg.Button('Choose')]
        ]

    def run(self, text, context):
        window = sg.Window('Format', self.layout)

        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                break
            elif event == 'Choose':
                context.send_message(f"User option: {values[Keys.OPTION_KEY.value]}")
                result_window = ResultWindowFactory().create_window()
                result_window.run(text, values[Keys.OPTION_KEY.value], context)


class ResultWindow(Window):
    def __init__(self):

        self.layout = [
            [sg.Text('Result:', size=(15, 1), justification='center')],
            [sg.Text(size=(40, 1), key=Keys.RESULT_KEY.value)],
            [sg.Button('Calculate')]
        ]

    def run(self, text, option, context):
        window = sg.Window('Result', self.layout)
        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                break
            if event == 'Calculate':
                if option == 'Seconds in minutes':
                    result = int(text) // 60
                elif option == 'Minutes in hours':
                    result = int(text) // 60
                elif option == 'Hours in days':
                    result = int(text) // 24
                context.send_message(f"Calculated Result: {result}")
                window[Keys.RESULT_KEY.value].update(result)


class WindowFactory(ABC):
    @abstractmethod
    def create_window(self):
        pass


class MainWindowFactory(WindowFactory):
    def create_window(self):
        return MainWindow()


class OptionsWindowFactory(WindowFactory):
    def create_window(self):
        return OptionsWindow()


class ResultWindowFactory(WindowFactory):
    def create_window(self):
        return ResultWindow()
