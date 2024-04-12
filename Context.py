#!/usr/bin/python3


class Context:
    def __init__(self, strategy=None):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def send_message(self, message):
        self.strategy.send_message(message)


