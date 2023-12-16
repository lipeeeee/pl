# Defines an abstract interface required to use on each model

from abc import ABC

class PLModel(ABC):
    def __init__(self) -> None:
        ...

    def train(self, data, reset_weights=False):
        pass

    def predict(self, data):
        pass

    def __str__(self) -> str:
        return "<pl.PLModel>"
