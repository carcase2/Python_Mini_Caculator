import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setFixedSize(400,400)

        # Create display and buttons
        self.display = QLineEdit(self)
        self.display.move(20, 20)
        self.display.resize(360, 60)
        self.createButtons()

    def createButtons(self):
        button_list = ['7', '8', '9', '/', '4', '5', '6', '*', '1', '2', '3', '-', '0', '.', '=', '+']
        pos_x = 20
        pos_y = 100
        for button_text in button_list:
            button = QPushButton(button_text, self)
            button.resize(80, 60)
            button.move(pos_x, pos_y)
            pos_x += 100
            if pos_x == 420:
                pos_x = 20
                pos_y += 80

            # Connect buttons to functions
            if button_text == '=':
                button.clicked.connect(self.calculateResult)
            else:
                print(button_text)
                button.clicked.connect(lambda state, b=button_text: self.addToDisplay(b))

    def addToDisplay(self, button_text):
        current_text = self.display.text()
        new_text = current_text + button_text
        self.display.setText(new_text)

    def calculateResult(self):
        result = eval(self.display.text())
        self.display.setText(str(result))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec())
