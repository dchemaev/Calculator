# in process
class NumSysCalculation:
    def __init__(self, text):
        super().__init__()
        self.set_text = text
        self.total = int
        self.stack = []
        self.text = []

    def calculation(self, i, j):  # set_text == [""]
        if i == j:
            self.total = self.set_text
        if i == 2:
            if j == 3:
                self.total = ["23"]
            if j == 4:
                self.total = ["24"]
            if j == 5:
                self.total = ["25"]
            if j == 6:
                self.total = ["26"]
            if j == 7:
                self.total = ["27"]
            if j == 8:
                self.total = ["28"]
            if j == 9:
                self.total = ["29"]
            if j == 10:
                self.total = ["20"]
        if i == 3:
            if j == 2:
                self.total = ["32"]
            if j == 4:
                self.total = ["34"]
            if j == 5:
                self.total = ["35"]
            if j == 6:
                self.total = ["36"]
            if j == 7:
                self.total = ["37"]
            if j == 8:
                self.total = ["38"]
            if j == 9:
                self.total = ["39"]
            if j == 10:
                self.total = ["30"]
        # do the same shit with 4...10
        # i wanna sleep bitch
        return self.total
