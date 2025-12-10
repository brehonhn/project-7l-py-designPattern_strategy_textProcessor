from strategies.PrintStrategy import PrintStrategy


class NormalPrintStrategy(PrintStrategy):
    def print_text(self, text: str):
        return text
