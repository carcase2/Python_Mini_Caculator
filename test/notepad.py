import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog
from PySide6.QtWidgets import QAction

class Notepad(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)

        self.statusBar()

        openFile = QAction('Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.triggered.connect(self.open)

        saveFile = QAction('Save', self)
        saveFile.setShortcut('Ctrl+S')
        saveFile.triggered.connect(self.save)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)
        fileMenu.addAction(saveFile)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Notepad')
        self.show()

    def open(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, 'Open File', '', 'Text Files (*.txt);;All Files (*)', options=options)
        if fileName:
            with open(fileName, 'r') as f:
                text = f.read()
                self.textEdit.setText(text)

    def save(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, 'Save File', '', 'Text Files (*.txt);;All Files (*)', options=options)
        if fileName:
            with open(fileName, 'w') as f:
                text = self.textEdit.toPlainText()
                f.write(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    notepad = Notepad()
    sys.exit(app.exec())
