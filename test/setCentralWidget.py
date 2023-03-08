import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit

app = QApplication(sys.argv)
window = QMainWindow()

text_edit = QTextEdit()
text_edit.setText("This is the central widget")

window.setCentralWidget(text_edit)
window.show()

sys.exit(app.exec_())
