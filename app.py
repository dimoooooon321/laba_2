import sys
from typing import Union, Optional
from operator import add, sub, mul, truediv

from PySide6.QtWidgets import QApplication, QMainWindow

from Calculator import Ui_MainWindow

operations = {
        '+': add,
        '-': sub,
        '×': mul,
        '/': truediv
}

error_zero_div = 'Division by zero'
error_undefined = 'Result in undefined'

class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.entry = self.ui.lineEdit
        self.temp = self.ui.lineEdit_2

        self.entry_max_len = self.entry.maxLength()

        # числа
        self.ui.pushButton_0.clicked.connect(self.add_digit)
        self.ui.pushButton_1.clicked.connect(self.add_digit)
        self.ui.pushButton_2.clicked.connect(self.add_digit)
        self.ui.pushButton_3.clicked.connect(self.add_digit)
        self.ui.pushButton_4.clicked.connect(self.add_digit)
        self.ui.pushButton_5.clicked.connect(self.add_digit)
        self.ui.pushButton_6.clicked.connect(self.add_digit)
        self.ui.pushButton_7.clicked.connect(self.add_digit)
        self.ui.pushButton_8.clicked.connect(self.add_digit)
        self.ui.pushButton_9.clicked.connect(self.add_digit)

    #действия
        self.ui.pushButton_clear.clicked.connect(self.clear_all)
        self.ui.pushButton_point.clicked.connect(self.add_point)
        self.ui.pushButton_negate.clicked.connect(self.negate)
        self.ui.pushButton_backspace.clicked.connect(self.backspace)
    #математика
        self.ui.pushButton_equals.clicked.connect(self.calculate)
        self.ui.pushButton_plus.clicked.connect(self.math_operation)
        self.ui.pushButton_minus.clicked.connect(self.math_operation)
        self.ui.pushButton_mul.clicked.connect(self.math_operation)
        self.ui.pushButton_divivde.clicked.connect(self.math_operation)



    def add_digit(self,btn_text: str) -> None:
        self.remove_error()
        self.clear_temp_if_equality()
        btn = self.sender()

        digit_buttons = ('pushButton_0', 'pushButton_1', 'pushButton_2', 'pushButton_3', 'pushButton_4', 'pushButton_5',
                         'pushButton_6', 'pushButton_7', 'pushButton_8', 'pushButton_9' )

        if btn.objectName() in digit_buttons:
            if self.entry.text() == '0':
                self.entry.setText(btn.text())
            else:
                self.entry.setText(self.entry.text() + btn.text())

    def add_point(self) -> None:
        self.clear_temp_if_equality()
        if '.' not in self.entry.text():
            self.entry.setText(self.entry.text() + '.')

    def negate(self):
        self.clear_temp_if_equality()
        entry = self.entry.text()

        if '-' not in entry:
            if entry != '0':
                entry = '-' + entry
        else:
            entry = entry[1:]

        if len(entry) == self.entry_max_len + 1 and '-' in entry:
            self.entry.setMaxLength(self.entry_max_len + 1)
        else:
            self.entry.setMaxLength(self.entry_max_len)

        self.entry.setText(entry)

    def backspace(self) -> None:
        self.remove_error()
        self.clear_temp_if_equality()
        entry = self.entry.text()

        if len(entry) != 1:
            if len(entry) == 2 and '-' in entry:
                self.entry.setTtext('0')
            else:
                self.entry.setText(entry[:-1])
        else:
            self.entry.setText('0')

    def clear_all(self) -> None:
        self.remove_error()
        self.entry.setText('0')
        self.temp.clear()

    def clear_entry(self) -> None:
        self.remove_error()
        self.clear_temp_if_equality()
        self.entry.setText('0')


    def add_temp(self):
        btn = self.sender()
        entry = self.remove_trailing_zeros(self.entry.text())

        if not self.temp.text() or self.get_math_sign() == '=':
            self.temp.setText(entry + f' {btn.text()} ')
            self.entry.setText('0')

    def get_entry_num(self) -> Union[int, float]:
        entry = self.entry.text().strip('.')

        return float(entry) if '.' in entry else int(entry)

    def get_temp_num(self) -> Union[int, float, None]:
        if self.temp.text():
            temp = self.temp.text().strip('.').split()[0]
            return float(temp) if '.' in temp else int(temp)

    def get_math_sign(self) -> Optional[str]:
        if self.temp.text():
            return self.temp.text().strip('.').split()[-1]

    def calculate(self) -> Optional[str]:
        entry = self.entry.text()
        temp = self.temp.text()

        if temp:
            try:
                result = self.remove_trailing_zeros(
                    str(operations[self.get_math_sign()](self.get_temp_num(), self.get_entry_num()))
                    )
                self.temp.setText(temp + self.remove_trailing_zeros(entry) +  ' =')
                self.entry.setText(result)
                return result

            except KeyError:
                pass

            except ZeroDivisionError:
                if self.get_temp_num() == 0:
                    self.show_error(error_undefined)
                else:
                    self.show_error(error_zero_div)
    def math_operation(self) -> None:
        temp = self.temp.text()
        btn = self.sender()

        try:
            if not temp:
                self.add_temp()
            else:
                if self.get_math_sign() != btn.text():
                    if self.get_math_sign() == '=':
                        self.add_temp()
                    else:
                        self.temp.setText(temp[:-2] + f'{btn.text()}')
                else:
                    self.temp.setText(self.calculate() + f'{btn.text()}')
        except TypeError:
            pass

    def show_error(self, text: str) -> None:
        self.entry.setMaxLength(len(text))
        self.entry.setText(text)
        self.disable_buttons(True)

    def remove_error(self) -> None:
        if self.entry.text() in (error_undefined,error_zero_div):
            self.entry.setMaxLength(self.entry_max_len)
            self.entry.setText('0')
            self.disable_buttons(False)

    def disable_buttons(self,disable: bool) -> None:
        self.ui.pushButton_equals.setDisabled(disable)
        self.ui.pushButton_plus.setDisabled(disable)
        self.ui.pushButton_minus.setDisabled(disable)
        self.ui.pushButton_mul.setDisabled(disable)
        self.ui.pushButton_divivde.setDisabled(disable)
        self.ui.pushButton_negate.setDisabled(disable)
        self.ui.pushButton_point.setDisabled(disable)

    #     self.change_buttons_color('color: #888;')
    #
    # def change_buttons_color(self, css_color: str) -> None:
    #     self.ui.pushButton_equals.setDisabled(css_color)
    #     self.ui.pushButton_plus.setDisabled(css_color)
    #     self.ui.pushButton_minus.setDisabled(css_color)
    #     self.ui.pushButton_mul.setDisabled(css_color)
    #     self.ui.pushButton_divivde.setDisabled(css_color)
    #     self.ui.pushButton_negate.setDisabled(css_color)
    #     self.ui.pushButton_point.setDisabled(css_color)

    def clear_temp_if_equality(self) -> None:
        if self.get_math_sign() == '=':
            self.temp.clear()

    @staticmethod
    def remove_trailing_zeros(num: str) -> str:
        n = str(float(num))
        return n[:-2] if n[-2:] == '.0' else n

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Calculator()
    window.show()
    sys.exit(app.exec())