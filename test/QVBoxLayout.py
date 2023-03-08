import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel

app = QApplication(sys.argv)
window = QMainWindow()

layout = QVBoxLayout()

label1 = QLabel("Label 1")
label2 = QLabel("Label 2")

layout.addWidget(label1)
layout.addWidget(label2)

window.setLayout(layout)
window.show()

sys.exit(app.exec_())
