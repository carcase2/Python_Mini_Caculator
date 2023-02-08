import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Calculator")
        self.display = QLineEdit("", self)
        self.display.setGeometry(10, 10, 280, 40)
        self.createButtons()

    def createButtons(self):
        button_names = ["7", "8", "9", "/", "4", "5", "6", "*", "1", "2", "3", "-", "0", ".", "=", "+"]
        x_coord = 10
        y_coord = 60
        for name in button_names:
            button = QPushButton(name, self)
            button.setGeometry(x_coord, y_coord, 50, 40)
            button.clicked.connect(lambda: self.buttonClicked(name))
            x_coord += 60
            if x_coord >= 250:
                x_coord = 10
                y_coord += 50

    def buttonClicked(self, text):
        if text == "=":
            try:
                result = eval(self.display.text())
                self.display.setText(str(result))
            except:
                self.display.setText("Error")
        else:
            self.display.setText(self.display.text() + text)

app = QApplication(sys.argv)
calc = Calculator()
calc.show()
sys.exit(app.exec_())
