from abc import ABC, abstractmethod

class IPresentation(ABC):
    @abstractmethod
    def start(self): pass

class ConsoleUI(IPresentation):
    def __init__(self, service):
        self.service = service

    def start(self):
        print("Система готова. Починаю імпорт...")
        self.service.import_from_file("data.csv")