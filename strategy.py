from abc import ABC, abstractmethod

class OutputStrategy(ABC):
    @abstractmethod
    def send(self, row: dict):
        pass