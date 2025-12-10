from strategies.PrintStrategy import PrintStrategy


class TextPrinter:
    def __init__(self, strategy: PrintStrategy = None):
        self.strategy = strategy

    def set_strategy(self, strategy: PrintStrategy):
        self.strategy = strategy

    def print(self, text: str):
        return self.strategy.print_text(text)
