
import sys
from PySide6 import QtCore, QtGui
from PySide6.QtWidgets import QApplication, QPushButton,QTabWidget,QTextEdit,QVBoxLayout,QHBoxLayout,QGridLayout,QLineEdit
from PySide6.QtCore import Slot  
import re

result = ''
       
class MyWidget(QTabWidget):
    def __init__(self):
        super().__init__()

        self.text_edit =  QLineEdit()
        # self.text_edit.resize(100,100)
        self.button1_1 =  QPushButton('(')
        self.button1_2 =  QPushButton(')')
        self.button1_3 =  QPushButton('%')
        self.button1_4 =  QPushButton('AC')
    
        self.button2_1 =  QPushButton('7')
        self.button2_2 =  QPushButton('8')
        self.button2_3 =  QPushButton('9')
        self.button2_4 =  QPushButton('/')

        self.button3_1 =  QPushButton('4')
        self.button3_2 =  QPushButton('5')
        self.button3_3 =  QPushButton('6')
        self.button3_4 =  QPushButton('X')

        self.button4_1 =  QPushButton('1')
        self.button4_2 =  QPushButton('2')
        self.button4_3 =  QPushButton('3')
        self.button4_4 =  QPushButton('-')

        self.button5_1 =  QPushButton('0')
        self.button5_2 =  QPushButton('.')
        self.button5_3 =  QPushButton('=')
        self.button5_4 =  QPushButton('+')

        self.button1_1.setObjectName('(')
        self.button1_2.setObjectName(')')
        self.button1_3.setObjectName('%')
        self.button1_4.setObjectName('AC')
        self.button2_1.setObjectName('7')
        self.button2_2.setObjectName('8')
        self.button2_3.setObjectName('9')
        self.button2_4.setObjectName('/')
        self.button3_1.setObjectName('4')
        self.button3_2.setObjectName('5')
        self.button3_3.setObjectName('6')
        self.button3_4.setObjectName('X')
        self.button4_1.setObjectName('1')
        self.button4_2.setObjectName('2')
        self.button4_3.setObjectName('3')
        self.button4_4.setObjectName('-')
        self.button5_1.setObjectName('0')
        self.button5_2.setObjectName('.')
        self.button5_3.setObjectName('=')
        self.button5_4.setObjectName('+') 

        layout1 =  QVBoxLayout(self)
        layout_Number = QGridLayout()
        
        layout1.addWidget(self.text_edit)
        
        layout_Number.addWidget(self.button1_1,0,0)
        layout_Number.addWidget(self.button1_2,0,1)
        layout_Number.addWidget(self.button1_3,0,2)
        layout_Number.addWidget(self.button1_4,0,3)
        
        layout_Number.addWidget(self.button2_1,1,0)
        layout_Number.addWidget(self.button2_2,1,1)
        layout_Number.addWidget(self.button2_3,1,2)
        layout_Number.addWidget(self.button2_4,1,3)
                
        layout_Number.addWidget(self.button3_1,2,0)
        layout_Number.addWidget(self.button3_2,2,1)
        layout_Number.addWidget(self.button3_3,2,2)
        layout_Number.addWidget(self.button3_4,2,3)
        
        layout_Number.addWidget(self.button4_1,3,0)
        layout_Number.addWidget(self.button4_2,3,1)
        layout_Number.addWidget(self.button4_3,3,2)
        layout_Number.addWidget(self.button4_4,3,3)
        
        layout_Number.addWidget(self.button5_1,4,0)
        layout_Number.addWidget(self.button5_2,4,1)
        layout_Number.addWidget(self.button5_3,4,2)
        layout_Number.addWidget(self.button5_4,4,3)
        
        layout1.addLayout(layout_Number)

        self.button1_1.clicked.connect(self.onCheck)
        self.button1_2.clicked.connect(self.onCheck)
        self.button1_3.clicked.connect(self.onCheck)
        self.button1_4.clicked.connect(self.onCheck)
        self.button2_1.clicked.connect(self.onCheck)
        self.button2_2.clicked.connect(self.onCheck)
        self.button2_3.clicked.connect(self.onCheck)
        self.button2_4.clicked.connect(self.onCheck)
        self.button3_1.clicked.connect(self.onCheck)
        self.button3_2.clicked.connect(self.onCheck)
        self.button3_3.clicked.connect(self.onCheck)
        self.button3_4.clicked.connect(self.onCheck)
        self.button4_1.clicked.connect(self.onCheck)
        self.button4_2.clicked.connect(self.onCheck)
        self.button4_3.clicked.connect(self.onCheck)
        self.button4_4.clicked.connect(self.onCheck)
        self.button5_1.clicked.connect(self.onCheck)
        self.button5_2.clicked.connect(self.onCheck)
        self.button5_3.clicked.connect(self.onCheck)
        self.button5_4.clicked.connect(self.onCheck)
        
        print(self.button1_1.objectName())    

    def onCheck(self):    
        global result
        sender = self.sender()
        # print(self.button1_1)
        if sender is self.button1_1:
            print(self.button1_1.objectName())   
            temp = self.button1_1.objectName()
            result = result + temp
            self.text_edit.setText(result)
        elif sender is self.button1_2:     
            print(self.button1_2.objectName())   
            temp = self.button1_2.objectName()
            result = result + temp
            self.text_edit.setText(result)
        elif sender is self.button1_3:     
            print(self.button1_3.objectName())   
            temp = self.button1_3.objectName()
            result = result + temp
            self.text_edit.setText(result)
        elif sender is self.button1_4:     
            print(self.button1_4.objectName())   
            temp = self.button1_4.objectName()
            # result = result + temp
            self.text_edit.clear()
            result = ""
        elif sender is self.button2_1:
            print(self.button2_1.objectName())   
            temp = self.button2_1.objectName()
            result = result + temp
            self.text_edit.setText(result)
        elif sender is self.button2_2:     
            print(self.button2_2.objectName())   
            temp = self.button2_2.objectName()
            result = result + temp
            self.text_edit.setText(result)
        elif sender is self.button2_3:     
            print(self.button2_3.objectName())   
            temp = self.button2_3.objectName()
            result = result + temp
            self.text_edit.setText(result)
        elif sender is self.button2_4:     
            print(self.button2_4.objectName())   
            temp = self.button2_4.objectName()
            result = result + temp
            self.text_edit.setText(result)
        elif sender is self.button3_1:
            print(self.button3_1.objectName())   
            temp = self.button3_1.objectName()
            result = result + temp
            self.text_edit.setText(result)
        elif sender is self.button3_2:     
            print(self.button3_2.objectName())   
            temp = self.button3_2.objectName()
            result = result + temp
            self.text_edit.setText(result)
        elif sender is self.button3_3:     
            print(self.button3_3.objectName())   
            temp = self.button3_3.objectName()
            result = result + temp
            self.text_edit.setText(result)
        elif sender is self.button3_4:     
            print(self.button3_4.objectName())   
            temp = self.button3_4.objectName()
            result = result + temp
            self.text_edit.setText(result)
        elif sender is self.button4_1:
            print(self.button4_1.objectName())   
            temp = self.button4_1.objectName()
            result = result + temp
            self.text_edit.setText(result)
        elif sender is self.button4_2:     
            print(self.button4_2.objectName())   
            temp = self.button4_2.objectName()
            result = result + temp
            self.text_edit.setText(result)
        elif sender is self.button4_3:     
            print(self.button4_3.objectName())   
            temp = self.button4_3.objectName()
            result = result + temp
            self.text_edit.setText(result)
        elif sender is self.button4_4:     
            print(self.button4_4.objectName())   
            temp = self.button4_4.objectName()
            result = result + temp
            self.text_edit.setText(result)    
        elif sender is self.button5_1:
            print(self.button5_1.objectName())   
            temp = self.button5_1.objectName()
            result = result + temp
            self.text_edit.setText(result)
        elif sender is self.button5_2:     
            print(self.button5_2.objectName())   
            temp = self.button5_2.objectName()
            result = result + temp
            self.text_edit.setText(result)
        elif sender is self.button5_3:                
            print(self.button5_3.objectName())   
            temp = self.button5_3.objectName()
            result1 = result.replace(" " , "")
            result1 = result1 + temp
            result = result + temp
            
            print(result1)
            numbers_1 = int(re.findall('\d+', result1)[0])
            numbers_2 = int(re.findall('\d+', result1)[1])
            if "X" in result1:
                temp = numbers_1*numbers_2
                print(numbers_1*numbers_2)
                # result = result + temp
            if "+" in result1:
                temp = numbers_1+numbers_2
                print(numbers_1+numbers_2)
            if "-" in result1:
                temp = numbers_1-numbers_2
                print(numbers_1-numbers_2)
            if "/" in result1:
                temp = numbers_1/numbers_2
                print(numbers_1/numbers_2)
                        
            result1 = result1 + str(temp)
            result = result + str(temp)            

            self.text_edit.setText(result)
        elif sender is self.button5_4:     
            print(self.button5_4.objectName())   
            temp = self.button5_4.objectName()
            result = result + temp
            self.text_edit.setText(result)    
                
        # ????????? display ?????? ?????? ?????? ?????????
        result = result + " "
            
 
if __name__ == "__main__":
    app =  QApplication()
   
    widget = MyWidget()
    widget.resize(200, 200)
    widget.setWindowTitle("Caculate by KKD")
    widget.show()  
    
    sys.exit(app.exec())
