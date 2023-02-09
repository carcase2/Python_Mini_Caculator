
import sys
from PySide6 import QtCore, QtGui

from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QWidget, QGridLayout
from PySide6.QtCore import Slot, Qt

import re

result = ''
result_state = False
count = 0

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(300, 300)
        self.setWindowTitle("Caculate by KKD")

        # create display
        self.text_edit = QLineEdit("", self)
        self.text_edit.setFixedSize(280, 40)
        # 오른쪽 정렬
        self.text_edit.setAlignment(Qt.AlignRight)
        # 읽기만 가능하게
        self.text_edit.setReadOnly(True)

        # button 만들기
        self.createButtons()

        # set main layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.text_edit)
        main_layout.addLayout(self.buttons_layout)
        central_widget = QWidget(self)
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def createButtons(self):
        global count
        self.buttons = {
            "(": (0, 0),
            ")": (0, 1),
            "%": (0, 2),
            "AC": (0, 3),
            "7": (1, 0),
            "8": (1, 1),
            "9": (1, 2),
            "/": (1, 3),
            "4": (2, 0),
            "5": (2, 1),
            "6": (2, 2),
            "*": (2, 3),
            "1": (3, 0),
            "2": (3, 1),
            "3": (3, 2),
            "-": (3, 3),
            "0": (4, 0),
            ".": (4, 1),
            "=": (4, 2),
            "+": (4, 3)
        }
        # print(self.buttons.items())
        # print(type(self.buttons.items()))

        self.buttons_layout = QGridLayout()
        for btn_text, pos in self.buttons.items():
            print("btn_text = ",btn_text)
            print("pos = ",pos)
            button = QPushButton(btn_text)
            print(type(button))
            button.clicked.connect(self.handle_button)
            self.buttons_layout.addWidget(button, pos[0], pos[1])

    def handle_button(self):
        global result_state
        print(result_state)
        button = self.sender()
        if button.text() == "=":
            try:
                temp = self.text_edit.text()
                result = eval(self.text_edit.text())
                self.text_edit.setText(temp + button.text() + str(result))
                result_state = True
            except:
                self.text_edit.setText("Error")
        elif button.text() == "AC":
            self.text_edit.clear()
        else:
            if result_state == True:
                self.text_edit.clear()
                self.text_edit.setText(self.text_edit.text() + button.text())
                result_state = False
            else:
                self.text_edit.setText(self.text_edit.text() + button.text())


if __name__ == "__main__":
    app = QApplication()

    widget = MyWidget()

    widget.show()

    sys.exit(app.exec())
