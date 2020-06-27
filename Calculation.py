import math


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
