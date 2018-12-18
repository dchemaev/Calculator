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

        self.pushButton_ravno.clicked.connect(self.calculation)

        self.result_show.setReadOnly(True)  # Нельзя ничего добавить в дисплей с клавиатуры

        #  self.pushButton_del.clicked.connect(self.display.clear)  # Нужно сделать очистку экрана

    def initUI(self):
        uic.loadUi("calculatorDesigne.ui", self)

    def display(self, value):  # Показывает вводимые символы на "экранчик"
        self.result_show.setText(self.result_show.toPlainText() + value)  # Последовательный ввод символов

    def calculation(self):  # Получаем значение переменных с "Экранчика"
        screen_value = self.result_show.toPlainText().split(" ")
        val1 = float(screen_value[0])
        operator = screen_value[1]
        val2 = float(screen_value[2])
        result = self.maths(val1, val2, operator)
        if result == int(result):
            result = int(result)
        self.result_show.setText(str(result))

    def maths(self, val1, val2, operator):  # Рассчёты
        val1 = float(val1)
        val2 = float(val2)
        if operator is "+":
            return val1 + val2
        elif operator is "-":
            return val1 - val2
        elif operator is "/":
            return val1 / val2
        elif operator is "*":
            return val1 * val2



if __name__ == "__main__":   # Обработка клацаний юзера
    app = QApplication(sys.argv)
    calc = CalculatorClass()
    calc.show()
    sys.exit(app.exec())
