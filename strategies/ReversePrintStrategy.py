from strategies.PrintStrategy import PrintStrategy


class ReversePrintStrategy(PrintStrategy):
    def print_text(self, text: str):
        return text[::-1]
