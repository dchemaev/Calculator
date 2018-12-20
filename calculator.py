import sys


from PyQt5 import QtGui, uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit


class CalculatorClass(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("calculatorDesigne.ui", self)
        self.initUI()
        self.pushButton_0.clicked.connect(lambda: self.display("0"))
        self.pushButton_1.clicked.connect(lambda: self.display("1"))
        self.pushButton_2.clicked.connect(lambda: self.display("2"))
        self.pushButton_3.clicked.connect(lambda: self.display("3"))
        self.pushButton_4.clicked.connect(lambda: self.display("4"))
        self.pushButton_5.clicked.connect(lambda: self.display("5"))
        self.pushButton_6.clicked.connect(lambda: self.display("6"))
        self.pushButton_7.clicked.connect(lambda: self.display("7"))
        self.pushButton_8.clicked.connect(lambda: self.display("8"))
        self.pushButton_9.clicked.connect(lambda: self.display("9"))

        self.pushButton_plus.clicked.connect(lambda: self.display(" + "))
        self.pushButton_min.clicked.connect(lambda: self.display(" - "))
        self.pushButton_umnozhit.clicked.connect(lambda: self.display(" * "))
        self.pushButton_delenie.clicked.connect(lambda: self.display(" / "))
        self.pushButton_dot.clicked.connect(lambda: self.display('.'))

        self.pushButton_ravno.clicked.connect(self.calculation)

        self.result_show.setReadOnly(True)  # Нельзя ничего добавить в дисплей с клавиатуры

        #  self.pushButton_del.clicked.connect(self.display.clear)  # Нужно сделать очистку экрана

    def initUI(self):
        uic.loadUi("calculatorDesigne.ui", self)

    def display(self, value):  # Показывает вводимые символы на "экранчик"
        self.result_show.setText(self.result_show.toPlainText() + value)  # Последовательный ввод символов

    def calculation(self):  # Получаем значение переменных с "Экранчика"
        expression = CalculationClass()
        expression.set_text(self.result_show.toPlainText().split(" "))
        expression.read_text()
        self.result_show.setText(str(expression.result))


class CalculationClass:             # класс вычисляющий значения
    def __init__(self):
        super().__init__()
        self.result = 0
        self.value1 = 0
        self.value2 = 0
        self.operator = ''

    def set_text(self, text):       # задаем выражение для вычисления в виде списка
        self.text = text

    def math(self):                 # вычисляем значения
        if self.operator is "+":
            self.result = self.value1 + self.value2
            print(self.result)
        elif self.operator is "-":
            self.result = self.value1 - self.value2
        elif self.operator is "/":
            self.result = self.value1 / self.value2
        elif self.operator is "*":
            self.result = self.value1 * self.value2
        self.value1 = self.result

    def read_text(self):            # разбираем сложное выражение на простые
        try:
            for i in range(len(self.text)):
                if i % 2 == 0:
                    if self.value2 == 0:
                        self.value2 = float(self.text[i])
                    else:
                        if self.value1 == 0:
                            self.value1 = self.value2
                        self.value2 = float(self.text[i])
                        self.math()
                else:
                    if self.operator == '':
                        self.operator = self.text[i]
                    else:
                        self.operator = self.text[i]
                print(self.result, self.value1, self.value2, self.operator)

        except Exception:
            self.result = 'ERROR'


if __name__ == "__main__":   # Обработка клацаний юзера
    app = QApplication(sys.argv)
    calc = CalculatorClass()
    calc.show()
    sys.exit(app.exec())
