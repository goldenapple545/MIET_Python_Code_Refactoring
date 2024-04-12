#!/usr/bin/python3

from abc import ABC, abstractmethod
import datetime


class Strategy(ABC):
    @abstractmethod
    def send_message(self, message: str):
        pass


class ConsoleStrategy(Strategy):
    def send_message(self, message):
        print(f'[{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] {message}')


class FileStrategy(Strategy):
    def __init__(self, file_path):
        self.file_path = file_path

    def send_message(self, message):
        with open(self.file_path, 'a') as file:
            file.write(f'[{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] {message}\n')
