"""""
__author1__ == "Danil Chemaev"
__author2__ ==
"""""


import sys

from PyQt5 import QtGui, uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QTextEdit

class CalculatorClass(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("calculatorDesigne.ui", self)
        self.initUI()
        self.display("25424")

    def initUI(self):
        uic.loadUi("calculatorDesigne.ui", self)

    def display(self, value):  # Показывает вводимые символы на "экранчик"
        self.result_show.setText(value)

    def calculation(self, val1, val2, operator):
        val1 = float(val1)
        val2 = float(val2)
        if operator is "sum":
            return val1 + val2
        elif operator is "min":
            return val1 - val2
        elif operator is "del":
            return val1 / val2
        elif operator is "umn":
            return val1 * val2


if __name__ == "__main__":   # Обработка клацаний юзера
    app = QApplication(sys.argv)
    calc = CalculatorClass()
    calc.show()
    sys.exit(app.exec()