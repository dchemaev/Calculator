import sys
import math
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("calculatorDesign.ui", self)
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

        self.pushButton_del.clicked.connect(lambda: self.clear(True))  # Нужно сделать очистку экрана
        self.pushButton_del_2.clicked.connect(lambda: self.clear(False))

    def initUI(self):
        uic.loadUi("calculatorDesign.ui", self)

    def display(self, value):  # Показывает вводимые символы на "экранчик"
        self.result_show.setText(self.result_show.toPlainText() + value)  # Последовательный ввод символов

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
        else:  # функция del
            txt = self.result_show.toPlainText().split()  # запоминаем выражение с экранчика
            txt = txt[:-1]  # удаляем послений элемент
            if len(txt) > 0:  # меняем значение на экранчике
                self.result_show.setText("")
                for i in txt:
                    self.result_show.setText(self.result_show.toPlainText() + i + ' ')
            else:
                self.clear(True)


class CalculationClass:  # класс вычисляющий значения
    def fast_degree(self, a, n):
        if n == 0:
            return 1
        if n % 2 == 0:
            return self.fast_degree(a * a, n // 2)
        else:
            return a * self.fast_degree(a, n - 1)

    def prime_function(self, val1, val2, operator):  # вычисляем значения выражений с двумя переменными
        result = 0
        try:
            if operator == '+':
                result = val1 + val2
            elif operator == '-':
                result = val1 - val2
            elif operator == '/':
                result = val1 / val2
            elif operator == '*':
                result = val1 * val2
            elif operator == '^':
                if val2 == abs(int(val2)):
                    result = self.fast_degree(val1, val2)
                else:
                    result = val1 ** val2
            if result == int(result):  # Убираем ненужный 0 при выводе целого числа
                return int(result)
            else:
                return self.round(result)
        except Exception:
            return "ERROR"

    def hard_function(self, val3, operator):  # вычисляем значения выражений с одной переменной
        if operator == 'sin':
            result = math.sin(math.radians(val3))
        if operator == 'cos':
            result = math.cos(math.radians(val3))
        if operator == 'tg':
            result = math.tan(math.radians(val3))
        if operator == 'ctg':
            result = 1 / math.tan(math.radians(val3))  # radians - перевод из градусов в радианы

        if operator == 'arccos':
            result = math.acos(val3)
        if operator == 'arcsin':
            result = math.asin(val3)
        if operator == 'arctg':
            result = math.atan(val3)
        if operator == 'arcctg':
            result = (math.pi / 2) - math.atan(val3)

        if operator == '!':
            result = math.factorial(val3)
        if operator == '%':
            result = self.prime_function(val3, 100, '/')
        if operator == '√':
            result = math.sqrt(val3)
        return self.round(result)

    def round(self, result):  # округляем значение
        return round(result, 7)


class ReversePolishNotationClass:
    def __init__(self, text):
        super().__init__()
        self.set_text = text
        self.total = []
        self.stack = []
        self.text = []

    def process_1(self):  # превращаем -а в 0-а
        try:
            for i in range(len(self.set_text)):
                if i == 0 and (self.set_text[i] == '-' or self.set_text[i] == "+"):
                    self.text.append('0')
                    self.text.append(self.set_text[i])
                elif (self.set_text[i] == '+' or self.set_text[i] == '-') and self.set_text[i - 1] == '(':
                    self.text.append('0')
                    self.text.append(self.set_text[i])
                else:
                    self.text.append(self.set_text[i])
        except Exception:
            return "ERROR"

    def process_2(self):  # перевод примера в ОПН
        try:
            for i in self.text:
                if i.isdigit() or '.' in i:
                    self.total.append(float(i))
                elif i == '(':
                    self.stack.append(i)
                elif i in '+-' and len(self.stack) != 0:
                    if self.stack[-1] in '+-':
                        self.total.append(self.stack[-1])
                        self.stack[-1] = i
                    elif self.stack[-1] in '*/^':
                        while len(self.stack) > 0 and self.stack[-1] != '(':
                            self.total.append(self.stack.pop())
                        self.stack.append(i)
                    else:
                        self.stack.append(i)
                elif i == ')':
                    while self.stack[-1] != '(':
                        self.total.append(self.stack.pop())
                    self.stack.pop()
                    if len(self.stack) > 0:
                        if self.stack[-1] in 'sin tg ctg cos √ arcsin arccos arctg arcctg':
                            self.total.append(self.stack.pop())
                elif i in '*/^' and len(self.stack) != 0:
                    if self.stack[-1] in '*/^':
                        self.total.append(self.stack.pop())
                        self.stack.append(i)
                    else:
                        self.stack.append(i)
                elif i in '! %':
                    self.total.append(i)
                elif i in 'sin tg ctg cos √ arcsin arccos arctg arcctg':
                    self.stack.append(i)
                else:
                    self.stack.append(i)
            while len(self.stack) > 0:
                self.total.append(self.stack.pop())
        except Exception:
            return "ERROR"
        return self.total


class ReaderClass(CalculationClass):
    def __init__(self):
        super().__init__()
        self.operator = ''
        self.val1 = 0
        self.val2 = 0
        self.val3 = 0

    def set_expression(self, rpn):
        self.RPN = rpn

    def reader(self):  # читаем пример написсанный в ОПН
        try:
            i = 0
            while i < len(self.RPN) > 1:
                if not str(self.RPN[i]).isdigit() and '.' not in str(self.RPN[i]):
                    if self.RPN[i] in '+ - * / ^':  # вычисляем значения выражений с двумя переменными
                        self.val1 = self.RPN[i - 2]
                        self.val2 = self.RPN[i - 1]
                        self.operator = self.RPN[i]
                        self.RPN.pop(i)
                        self.RPN.pop(i - 1)
                        self.RPN.pop(i - 2)
                        self.RPN.insert(i - 2, self.prime_function(self.val1, self.val2, self.operator))
                        i -= 2
                    elif self.RPN[i] in 'sin cos tg ctg √ ! % ' \
                                        'arcsin arccos arctg arcctg':  # вычисляем значения выражений с одной переменной
                        self.val3 = self.RPN[i - 1]
                        self.operator = self.RPN[i]
                        self.RPN.pop(i)
                        self.RPN.pop(i - 1)
                        self.RPN.insert(i - 1, self.hard_function(self.val3, self.operator))
                        i -= 1
                i += 1
            return self.RPN
        except Exception:
            return 'Syntax ERROR'


if __name__ == "__main__":  # Обработка клацаний юзера
    app = QApplication(sys.argv)
    calc = Main()
    calc.show()
    sys.exit(app.exec())
