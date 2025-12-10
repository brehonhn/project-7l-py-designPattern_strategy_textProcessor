
---

# 📄 **README.md**

```markdown
# 🧩 Strategy Pattern — Text Printer Example (Python)

این پروژه یک نمونه ساده از **الگوی طراحی Strategy** در زبان پایتون است.  
برنامه یک جمله از کاربر دریافت می‌کند و بسته به انتخاب کاربر، آن را به صورت **معمولی** یا **معکوس** چاپ می‌کند.

---

## 📌 دربارهٔ الگوی Strategy

الگوی **Strategy** زمانی استفاده می‌شود که چند رفتار مختلف برای یک عملیات وجود داشته باشد و بخواهیم بتوانیم این رفتار را **در زمان اجرا** تغییر دهیم؛ بدون اینکه کد اصلی برنامه تغییر کند.

در این پروژه دو استراتژی وجود دارد:

- **NormalPrintStrategy** → چاپ جمله به صورت معمولی  
- **ReversePrintStrategy** → چاپ جمله به صورت برعکس  

---

## 🗂 ساختار پروژه

```

project/
│
├── strategies/
│   ├── base.py
│   ├── normal.py
│   └── reverse.py
│
├── printer.py
├── main.py
└── README.md

````

---

## 📜 کدهای اصلی

### ✨ Strategy پایه

```python
from abc import ABC, abstractmethod

class PrintStrategy(ABC):

    @abstractmethod
    def print_text(self, text: str):
        pass
````

### ✨ چاپ معمولی

```python
class NormalPrintStrategy(PrintStrategy):
    def print_text(self, text: str):
        return text
```

### ✨ چاپ معکوس

```python
class ReversePrintStrategy(PrintStrategy):
    def print_text(self, text: str):
        return text[::-1]
```

### ✨ کلاس Context

```python
class TextPrinter:
    def __init__(self, strategy: PrintStrategy = None):
        self.strategy = strategy

    def set_strategy(self, strategy: PrintStrategy):
        self.strategy = strategy

    def print(self, text: str):
        return self.strategy.print_text(text)
```

### ✨ برنامه اصلی

```python
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
```

---

## ▶️ اجرای پروژه

برای اجرای برنامه کافی است دستور زیر را اجرا کنید:

```bash
python main.py
```

---

## 🧪 نمونه اجرا

ورودی:

```
یک جمله وارد کنید: سلام دنیا
نوع چاپ:
1. چاپ معمولی
2. چاپ معکوس
انتخاب: 2
```

خروجی:

```
نتیجه: یناد مالس
```

---

## 🎯 نتیجه‌گیری

این پروژه نشان می‌دهد که چگونه می‌توان رفتارهای مختلف (چاپ معمولی یا معکوس) را با کمک **الگوی Strategy** جدا کرد و در زمان اجرا انتخاب نمود.
این روش باعث تمیزی کد، خوانایی بالاتر و قابلیت توسعه بهتر می‌شود.

---

## 📘 لایسنس

این پروژه آزاد است و می‌توانید هرگونه تغییر یا توسعه‌ای روی آن انجام دهید.

