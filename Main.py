import sys
from PyQt5.QtCore import Qt
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication

from Calculation import *
from NumSysCalc import *

from Calculation import ReversePolishNotationClass


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
        if event.key() == Qt.Key_ParenLeft:
            self.display(' ( ')
        if event.key() == Qt.Key_ParenRight:
            self.display(' ) ')
        if event.key() == Qt.Key_Equal or event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.calculation()
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
        self.pushButton_A.clicked.connect(lambda: self.display("A"))
        self.pushButton_B.clicked.connect(lambda: self.display("B"))
        self.pushButton_C.clicked.connect(lambda: self.display("C"))
        self.pushButton_D.clicked.connect(lambda: self.display("D"))
        self.pushButton_E.clicked.connect(lambda: self.display("E"))
        self.pushButton_F.clicked.connect(lambda: self.display("F"))

        self.pushButton_OK.clicked.connect(self.do)

        self.pushButton_AC.clicked.connect(lambda: self.clear(True))  # кнопка AC
        self.pushButton_del.clicked.connect(lambda: self.clear(False))  # кнопка del

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
        if event.key() == Qt.Key_A:
            self.display('A')
        if event.key() == Qt.Key_B:
            self.display('B')
        if event.key() == Qt.Key_C:
            self.display('C')
        if event.key() == Qt.Key_D:
            self.display('D')
        if event.key() == Qt.Key_E:
            self.display('E')
        if event.key() == Qt.Key_F:
            self.display('F')
        if event.key() == Qt.Key_Period or event.key() == Qt.Key_Comma:
            self.display('.')
        if event.key() == Qt.Key_Delete:
            self.clear(True)
        if event.key() == Qt.Key_Backspace:
            self.clear(False)
        if event.key() == Qt.Key_Equal or event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.do()

    def check(self):
        i = self.from_box.currentText()
        j = self.to_box.currentText()
        return int(i), int(j)

    def do(self):
        text = str(*self.import_display.toPlainText().split())
        i, j = self.check()[0], self.check()[1]
        check = 0
        if i != 16:
            for l in text:
                if l in "ABCDEF" or int(l) >= i:
                    self.export_display.setText("Ошибка. Исходное число не является 2-ичным числом " \
                                                "(символы в числе должны быть от 0 до {})".format(i - 1))
                    check += 1
                    break
        if check == 0:
            rez = convert_base(text, to_base=j, from_base=i)  # self.check() == [i, j]
            self.export_display.setText(str(rez))
            check = 0

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
