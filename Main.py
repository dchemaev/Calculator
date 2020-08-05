import sys
from PyQt5.QtCore import Qt
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets

from Calculation import *
from NumSysCalc import NumSysCalculation

from Calculator.Calculation import ReversePolishNotationClass


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.setWindowIcon(QIcon("Images/calc_Icon.png"))

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
        self.pushButton_multiply.clicked.connect(lambda: self.display(" * "))
        self.pushButton_delenie.clicked.connect(lambda: self.display(" / "))

        self.pushButton_sin.clicked.connect(lambda: self.display('sin ( '))
        self.pushButton_cos.clicked.connect(lambda: self.display('cos ( '))
        self.pushButton_tan.clicked.connect(lambda: self.display('tg ( '))
        self.pushButton_cot.clicked.connect(lambda: self.display('ctg ( '))

        self.pushButton_asin.clicked.connect(lambda: self.display('arcsin ( '))
        self.pushButton_acos.clicked.connect(lambda: self.display('arccos ( '))
        self.pushButton_atan.clicked.connect(lambda: self.display('arctg ( '))
        self.pushButton_acot.clicked.connect(lambda: self.display('arcctg ( '))

        self.pushButton_inverse_bracket.clicked.connect(lambda: self.display(' ) '))
        self.pushButton_bracket.clicked.connect(lambda: self.display(' ( '))
        self.pushButton_dot.clicked.connect(lambda: self.display('.'))

        self.pushButton_fact.clicked.connect(lambda: self.display(' ! '))
        self.pushButton_step2.clicked.connect(lambda: self.display(' ^ 2'))
        self.pushButton_step3.clicked.connect(lambda: self.display(' ^ 3'))
        self.pushButton_stepn.clicked.connect(lambda: self.display(' ^ '))
        self.pushButton_percent.clicked.connect(lambda: self.display(' % '))
        self.pushButton_koren.clicked.connect(lambda: self.display(' √ '))

        self.pushButton_equal.clicked.connect(self.calculation)

        self.result_show.setReadOnly(True)  # Нельзя ничего добавить в дисплей с клавиатуры

        self.pushButton_AC.clicked.connect(lambda: self.clear(True))  # кнопка AC
        self.pushButton_del.clicked.connect(lambda: self.clear(False))  # кнопка del

        self.pushButton_NumSysCalc.clicked.connect(self.openDialog)

    def openDialog(self):
        dialog = NumSystemWindow(self)
        dialog.show()

    def initUI(self):
        uic.loadUi("UI/calculatorDesign.ui", self)

    def display(self, value):  # Показывает вводимые символы на "экранчик"
        # self.result_show.insert(value)
        self.result_show.setText(self.result_show.toPlainText() + value)  # Последовательный ввод символов

    def keyPressEvent(self, event):  # интеграция окна калькулятора с клавиатурой и NumPad
        if event.key() == Qt.Key_1:
            self.display('1')
        if event.key() == Qt.Key_2:
            self.display('2')
        if event.key() == Qt.Key_3:
            self.display('3')
        if event.key() == Qt.Key_4:
            self.display('4')
        if event.key() == Qt.Key_5:
            self.display('5')
        if event.key() == Qt.Key_6:
            self.display('6')
        if event.key() == Qt.Key_7:
            self.display('7')
        if event.key() == Qt.Key_8:
            self.display('8')
        if event.key() == Qt.Key_9:
            self.display('9')
        if event.key() == Qt.Key_0:
            self.display('0')
        if event.key() == Qt.Key_Slash:
            self.display(' / ')
        if event.key() == Qt.Key_Plus:
            self.display(' + ')
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Equal:
            self.calculation()
        if event.key() == Qt.Key_Minus:
            self.display(' - ')
        if event.key() == Qt.Key_Asterisk:
            self.display(' * ')
        if event.key() == Qt.Key_Period or event.key() == Qt.Key_Comma:
            self.display('.')
        if event.key() == Qt.Key_Delete:
            self.clear(True)
        if event.key() == Qt.Key_Backspace:
            self.clear(False)

    def calculation(self):  # Получаем значение переменных с "Экранчика"
        text = ReversePolishNotationClass(self.result_show.toPlainText().split())
        # создает список для обработи обратной польской натации
        # ОПН - Обратная Польская Нотация
        text.process_1()  # в ReversePolishNotationClass производим предворительную обработку для ОПН
        text = text.process_2()  # производим обработку списка ОПН
        expression = ReaderClass()  # создаем список для чтения и вычисления выражения на ОПН
        expression.set_expression(text)  # в список кладем выражение на ОПН
        rez = expression.reader()  # читаем, по ходу чтения вычисляем значеия действий

        if rez == ['ERROR']:  # Если есть вычислительная ошибка
            self.result_show.setText(str(*rez))  # Выводим "ERROR" на экран
        elif rez == 'Syntax ERROR' or rez == 'ERROR':  # Если есть синтаксическая ошибка
            self.result_show.setText(str(rez))  # Выводим "ERROR" на экран
        elif float(*rez) == int(*rez):  # При отсутсвии какого-либо действия с чеслом
            self.result_show.setText(str(int(*rez)))  # выводим это же число на экран
        else:
            self.result_show.setText(str(*rez))  # Выводим  ответ на экран

    def clear(self, rez):  # очистка дисплейчика
        if rez:  # функция AC
            self.result_show.setText("")
        elif not rez:  # функция del
            txt = []
            for i in self.result_show.toPlainText():
                txt.append(i)
            txt = txt[:-1]  # удаляем послений элемент
            if len(txt) > 0:  # меняем значение на экранчике
                self.result_show.setText("")
                for j in txt:
                    self.result_show.setText(self.result_show.toPlainText() + j)
            else:
                self.clear(True)


class NumSystemWindow(QMainWindow):
    def __init__(self, parent=None):
        super(NumSystemWindow, self).__init__(parent)

        self.initUI()
        self.setWindowIcon(QIcon("Images/calc_Icon.png"))

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

        self.pushButton_OK.clicked.connect(self.do)
        self.import_display.setReadOnly(True)
        self.export_display.setReadOnly(True)

        self.pushButton_AC.clicked.connect(lambda: self.clear(True))  # кнопка AC
        self.pushButton_del.clicked.connect(lambda: self.clear(False))  # кнопка del

    def check(self):
        if self.import_rbt_2.isChecked():
            i = 2
        if self.import_rbt_3.isChecked():
            i = 3
        if self.import_rbt_4.isChecked():
            i = 4
        if self.import_rbt_5.isChecked():
            i = 5
        if self.import_rbt_6.isChecked():
            i = 6
        if self.import_rbt_7.isChecked():
            i = 7
        if self.import_rbt_8.isChecked():
            i = 8
        if self.import_rbt_9.isChecked():
            i = 9
        if self.import_rbt_10.isChecked():
            i = 10

        if self.export_rbt_2.isChecked():
            j = 2
        if self.export_rbt_3.isChecked():
            j = 3
        if self.export_rbt_4.isChecked():
            j = 4
        if self.export_rbt_5.isChecked():
            j = 5
        if self.export_rbt_6.isChecked():
            j = 6
        if self.export_rbt_7.isChecked():
            j = 7
        if self.export_rbt_8.isChecked():
            j = 8
        if self.export_rbt_9.isChecked():
            j = 9
        if self.export_rbt_10.isChecked():
            j = 10

        print(i, j)
        return i, j

    def do(self):
        text = NumSysCalculation(self.import_display.toPlainText().split())
        rez = text.calculation(*self.check())

        self.export_display.setText(str(int(*rez)))

    def initUI(self):
        uic.loadUi("UI/NumSystem.ui", self)

    def display(self, value):  # Показывает вводимые символы на "экранчик"
        # self.result_show.insert(value)
        self.import_display.setText(self.import_display.toPlainText() + value)  # Последовательный ввод символов

    def clear(self, rez):  # очистка дисплейчика
        if rez:  # функция AC
            self.import_display.setText("")
        elif not rez:  # функция del
            txt = []
            for i in self.import_display.toPlainText():
                txt.append(i)
            txt = txt[:-1]  # удаляем послений элемент
            if len(txt) > 0:  # меняем значение на экранчике
                self.import_display.setText("")
                for j in txt:
                    self.import_display.setText(self.import_display.toPlainText() + j)
            else:
                self.clear(True)


if __name__ == "__main__":  # Обработка клацаний юзера
    app = QApplication(sys.argv)
    calc = MainWindow()
    calc.show()
    sys.exit(app.exec())
