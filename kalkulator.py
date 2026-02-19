import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi

class CalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('kalkulator.ui', self)

        self.setWindowTitle('Kalkulator')
        self.setFixedSize(291, 421)

        self.num_buttons = [self.btn_0, self.btn_00, self.btn_1, self.btn_2, self.btn_3, self.btn_4,self.btn_5, self.btn_6, self.btn_7, self.btn_8, self.btn_9]
        self.operator_buttons = [self.btn_add, self.btn_subtract, self.btn_multiply, self.btn_divide]
        self.btn_clear.clicked.connect(self.clear)
        self.btn_equal.clicked.connect(self.calculate)

        for button in self.num_buttons:
            button.clicked.connect(self.append_number)

        for button in self.operator_buttons:
            button.clicked.connect(self.append_operator)

        self.clear()

    def append_number(self):
        button = self.sender()
        self.current_value = self.current_value + button.text()
        self.update_display()

    def append_operator(self):
        button = self.sender()
        self.current_operator = button.text()
        self.current_value += ' ' + self.current_operator + ' '
        self.update_display()

    def clear(self):
        self.current_value = ''
        self.current_operator = ''
        self.update_display()

    def calculate(self):
        try:
            result = eval(self.current_value)
            self.current_value = str(result)
            self.update_display()
        except Exception as e:
            self.current_value = 'Error'
            self.clear()
            self.update_display()

    def update_display(self):
        self.label.setText(self.current_value)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    sys.exit(app.exec_())
