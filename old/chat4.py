import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QWidget,QGridLayout
from PySide6.QtCore import Slot,Qt

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setFixedSize(400, 300)
        
        # create display
        self.display = QLineEdit()
        self.display.setFixedHeight(50)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        
        # create buttons
        self.create_buttons()
        
        # set main layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.display)
        main_layout.addLayout(self.buttons_layout)
        central_widget = QWidget(self)
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def create_buttons(self):
        self.buttons = {
            "7": (0, 0),
            "8": (0, 1),
            "9": (0, 2),
            "/": (0, 3),
            "4": (1, 0),
            "5": (1, 1),
            "6": (1, 2),
            "*": (1, 3),
            "1": (2, 0),
            "2": (2, 1),
            "3": (2, 2),
            "-": (2, 3),
            "0": (3, 0),
            "C": (3, 1),
            "=": (3, 2),
            "+": (3, 3),
        }
        self.buttons_layout = QGridLayout()
        for btn_text, pos in self.buttons.items():
            button = QPushButton(btn_text)
            button.clicked.connect(self.handle_button)
            self.buttons_layout.addWidget(button, pos[0], pos[1])
    
    def handle_button(self):
        button = self.sender()
        if button.text() == "=":
            try:
                result = eval(self.display.text())
                self.display.setText(str(result))
            except:
                self.display.setText("Error")
        elif button.text() == "C":
            self.display.clear()
        else:
            self.display.setText(self.display.text() + button.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())
