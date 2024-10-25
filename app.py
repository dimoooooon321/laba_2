import sys
import math
import re

from PySide6.QtWidgets import QApplication, QMainWindow
from Calculator import Ui_MainWindow

class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.entry = self.ui.lineEdit
        self.temp = self.ui.lineEdit_2
        self.entry.setText("")  # Начальное пустое поле

        # Числовые кнопки
        for i in range(10):
            getattr(self.ui, f'pushButton_{i}').clicked.connect(self.add_digit)

        # Кнопки операций
        self.ui.pushButton_clear.clicked.connect(self.clear_all)
        self.ui.pushButton_point.clicked.connect(self.add_point)
        self.ui.pushButton_negate.clicked.connect(self.negate)
        self.ui.pushButton_backspace.clicked.connect(self.backspace)
        self.ui.pushButton_bracket_opening.clicked.connect(self.add_bracket_opening)
        self.ui.pushButton_bracket_closing.clicked.connect(self.add_bracket_closing)

        # Математические операции
        self.ui.pushButton_equals.clicked.connect(self.calculate)
        self.ui.pushButton_plus.clicked.connect(lambda: self.add_operation('+'))
        self.ui.pushButton_minus.clicked.connect(lambda: self.add_operation('-'))
        self.ui.pushButton_mul.clicked.connect(lambda: self.add_operation('*'))
        self.ui.pushButton_divide.clicked.connect(lambda: self.add_operation('/'))
        self.ui.pushButton_power.clicked.connect(lambda: self.add_operation('**'))
        self.ui.pushButton_percent.clicked.connect(lambda: self.add_operation('%'))



        # Константы и тригонометрические функции
        self.ui.pushButton_E.clicked.connect(lambda: self.add_constant(math.e))
        self.ui.pushButton_PI.clicked.connect(lambda: self.add_constant(math.pi))
        self.ui.pushButton_sqrt.clicked.connect(lambda: self.add_function("sqrt"))
        self.ui.pushButton_sin.clicked.connect(lambda: self.add_function("sin"))
        self.ui.pushButton_cos.clicked.connect(lambda: self.add_function("cos"))
        self.ui.pushButton_tan.clicked.connect(lambda: self.add_function("tan"))
        self.ui.pushButton_cot.clicked.connect(lambda: self.add_function("cot"))
        self.ui.pushButton_arcsin.clicked.connect(lambda: self.add_function("arcsin"))
        self.ui.pushButton_arccos.clicked.connect(lambda: self.add_function("arccos"))
        self.ui.pushButton_arctan.clicked.connect(lambda: self.add_function("arctan"))
        self.ui.pushButton_arccot.clicked.connect(lambda: self.add_function("arccot"))
        self.ui.pushButton_ln.clicked.connect(lambda: self.add_function("ln"))
        self.ui.pushButton_log.clicked.connect(lambda: self.add_function("log"))
        self.ui.pushButton_mod.clicked.connect(lambda: self.add_function("mod"))

    def add_digit(self):
        self.clear_temp_if_equality()
        btn = self.sender()
        self.entry.setText(self.entry.text() + btn.text())

    def add_function(self, function: str):
        self.clear_temp_if_equality()
        self.entry.setText(self.entry.text() + f"{function}(")

    def add_operation(self, operation: str):
        self.clear_temp_if_equality()
        current_text = self.entry.text()
        if current_text and current_text[-1] not in "+-*/**":
            self.entry.setText(current_text + operation)

    def add_point(self):
        self.clear_temp_if_equality()
        if '.' not in self.entry.text():
            if not self.entry.text():
                self.entry.setText("0.")
            else:
                self.entry.setText(self.entry.text() + '.')

    def add_bracket_opening(self) -> None:
        self.entry.setText(self.entry.text() + '(')

    def add_bracket_closing(self) -> None:
        self.entry.setText(self.entry.text() + ')')

    def negate(self):
        entry = self.entry.text()
        if entry and entry[0] != '-':
            self.entry.setText('-' + entry)
        elif entry:
            self.entry.setText(entry[1:])

    def backspace(self):
        self.clear_temp_if_equality()
        entry = self.entry.text()
        if entry:
            self.entry.setText(entry[:-1])

    def clear_all(self):
        self.entry.setText("")
        self.temp.clear()

    def add_constant(self, constant: float):
        self.clear_temp_if_equality()
        self.entry.setText(self.entry.text() + str(constant))

    def clear_temp_if_equality(self):
        if '=' in self.temp.text():
            self.temp.clear()

    def calculate(self):
        expression = self.entry.text()
        self.temp.setText(expression)  # Отображаем выражение в temp

        # Заменяем проценты, например, "50%" на "50*0.01"
        expression = re.sub(r'(\d+(\.\d+)?)%', r'(\1*0.01)', expression)

        # Контекст для функций
        context = {
            "sqrt": math.sqrt,
            "sin": lambda x: math.sin(math.radians(x)),
            "cos": lambda x: math.cos(math.radians(x)),
            "tan": lambda x: math.tan(math.radians(x)),
            "cot": lambda x: 1 / math.tan(math.radians(x)),
            "arcsin": lambda x: math.degrees(math.asin(x)),
            "arccos": lambda x: math.degrees(math.acos(x)),
            "arctan": lambda x: math.degrees(math.atan(x)),
            "arccot": lambda x: 1/ math.degrees(math.atan(x)),
            "ln": math.log,
            "log": lambda x, base=10: math.log(x, base),
            "mod": lambda x : abs(x),
            "pi": math.pi,
            "e": math.e
        }

        try:
            # Вычисляем выражение с помощью eval
            result = eval(expression, {"__builtins__": None}, context)
            self.entry.setText(str(result))
        except ZeroDivisionError:
            self.show_error("Division by zero")
        except Exception:
            self.show_error("Error")

    def show_error(self, text):
        self.entry.setText(text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())
