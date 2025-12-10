from TextPrinter import TextPrinter
from strategies.NormalPrintStrategy import NormalPrintStrategy
from strategies.ReversePrintStrategy import ReversePrintStrategy


def main():
    text = input("یک جمله وارد کنید: ")

    print("نوع چاپ را انتخاب کنید:")
    print("1. چاپ معمولی")
    print("2. چاپ معکوس")

    choice = input("انتخاب شما: ")

    printer = TextPrinter()

    if choice == "1":
        printer.set_strategy(NormalPrintStrategy())
    elif choice == "2":
        printer.set_strategy(ReversePrintStrategy())
    else:
        print("انتخاب نامعتبر!")
        return

    result = printer.print(text)
    print("نتیجه:", result)


if __name__ == "__main__":
    main()
