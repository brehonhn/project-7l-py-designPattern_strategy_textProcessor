from abc import ABC, abstractmethod

class PrintStrategy(ABC):

    @abstractmethod
    def print_text(self, text: str):
        pass
