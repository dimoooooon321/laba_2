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

class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # числа
        self.ui.pushButton_0.clicked.connect(lambda: self.add_digit('0'))
        self.ui.pushButton_1.clicked.connect(lambda: self.add_digit('1'))
        self.ui.pushButton_2.clicked.connect(lambda: self.add_digit('2'))
        self.ui.pushButton_3.clicked.connect(lambda: self.add_digit('3'))
        self.ui.pushButton_4.clicked.connect(lambda: self.add_digit('4'))
        self.ui.pushButton_5.clicked.connect(lambda: self.add_digit('5'))
        self.ui.pushButton_6.clicked.connect(lambda: self.add_digit('6'))
        self.ui.pushButton_7.clicked.connect(lambda: self.add_digit('7'))
        self.ui.pushButton_8.clicked.connect(lambda: self.add_digit('8'))
        self.ui.pushButton_9.clicked.connect(lambda: self.add_digit('9'))

    #действия
        self.ui.pushButton_clear.clicked.connect(self.clear_all)
        self.ui.pushButton_point.clicked.connect(self.add_point)


    #математика
        self.ui.pushButton_equals.clicked.connect(self.calculate)
        self.ui.pushButton_plus.clicked.connect(lambda: self.add_temp('+'))
        self.ui.pushButton_minus.clicked.connect(lambda: self.add_temp('-'))
        self.ui.pushButton_mul.clicked.connect(lambda: self.add_temp('×'))
        self.ui.pushButton_divivde.clicked.connect(lambda: self.add_temp('/'))



    def add_digit(self,btn_text: str) -> None:
        if self.ui.lineEdit.text() == '0':
            self.ui.lineEdit.setText(btn_text)
        else:
            self.ui.lineEdit.setText(self.ui.lineEdit.text() + btn_text)

    def add_point(self) -> None:
        if '.' not in self.ui.lineEdit.text():
            self.ui.lineEdit.setText(self.ui.lineEdit.text() + '.')

    def clear_all(self) -> None:
        self.ui.lineEdit.setText('0')
        self.ui.lineEdit_2.clear()

    def add_temp(self, math_sign: str):
        if not self.ui.lineEdit_2.text() or self.get_math_sign() == '=':
            self.ui.lineEdit_2.setText(f"{self.remove_trailing_zeros(self.ui.lineEdit.text())} {math_sign}")
            self.ui.lineEdit.setText('0')

    def get_entry_num(self) -> Union[int, float]:
        entry = self.ui.lineEdit.text().strip('.')

        return float(entry) if '.' in entry else int(entry)

    def get_temp_num(self) -> Union[int, float, None]:
        if self.ui.lineEdit_2.text():
            temp = self.ui.lineEdit_2.text().strip('.').split()[0]
            return float(temp) if '.' in temp else int(temp)

    def get_math_sign(self) -> Optional[str]:
        if self.ui.lineEdit_2.text():
            return self.ui.lineEdit_2.text().strip('.').split()[-1]

    def calculate(self) -> Optional[str]:
        entry = self.ui.lineEdit.text()
        temp = self.ui.lineEdit_2.text()

        if temp:
            result = self.remove_trailing_zeros(
                str(operations[self.get_math_sign()](self.get_temp_num(), self.get_entry_num()))
                )
            self.ui.lineEdit_2.setText(temp + self.remove_trailing_zeros(entry) +  ' =')
            self.ui.lineEdit.setText(result)
            return result

    def math_operation(self,math_sign: str):
        temp = self.ui.lineEdit_2.text()

        if not temp:
            self.add_temp(math_sign)
        else:
            if self.get_math_sign() != math_sign:
                if self.get_math_sign() == '=':
                    self.add_temp(math_sign)
                else:
                    self.ui.lineEdit_2.setText(temp[:-2] + f'{math_sign}')
            else:
                self.ui.lineEdit_2.setText(self.calculate() + f'{math_sign}')


    @staticmethod
    def remove_trailing_zeros(num: str) -> str:
        n = str(float(num))
        return n[:-2] if n[-2:] == '.0' else n

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Calculator()
    window.show()
    sys.exit(app.exec())