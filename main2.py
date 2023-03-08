import sys
from PySide6 import QtCore, QtGui

from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QWidget, QGridLayout, QLabel
from PySide6.QtCore import Slot, Qt

import re

# 결과값 변수 지정 result
# 계산후( = 입력후) 숫자 입력시 text line clear하기 위해 변수 추가 result_state
# Memory number 저장 변수 지정 MS_number

result = ''
result_state = False
count = 0
MS_number = 0

# parent QMainWindow class를 불러와서 초기화함 class 선언시 괄호 안에 넣으면 부모 class가 되고 super로 하면 초기화 된다.


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        # 외형 사이즈 지정 가로 300 세로 600
        # setFixedSize fuction은 QWidget class 안에 있다.
        self.setFixedSize(300, 600)

        # 윈도우 title 명 지정
        self.setWindowTitle("Caculate by KKD")

        # create display
        # 결과값 display text line 지정(초기화) text_edit
        # Memory Storage에 저장된 값 지정(초기화) text_edit2

        self.text_edit = QLineEdit("", self)
        self.text_edit2 = QLineEdit("", self)
        # text 창 사이즈 지정
        self.text_edit.setFixedSize(280, 40)
        self.text_edit2.setFixedSize(100, 20)

        # Memory Storage Label 지정
        # text_lable font size 지정 10으로
        # text_edit fone size 지정 15로
        self.text_label = QLabel("Memory Number")
        font = self.text_label.font()
        font.setPointSize(10)
        self.text_label.setFont(font)
        font = self.text_edit.font()
        font.setPointSize(15)
        self.text_edit.setFont(font)
        # text_edit창 두개 display 오른쪽 정렬
        self.text_edit.setAlignment(Qt.AlignRight)
        self.text_edit2.setAlignment(Qt.AlignRight)
        # 읽기만 가능하게(수정하지 못하게)
        self.text_edit.setReadOnly(True)
        self.text_edit2.setReadOnly(True)

        # button 만드는 fuction 실행
        self.createButtons()

        # set main layout

        # main_layout을 수직으로(vertical) 지정
        # main_layout을 수평으로(horizone) 지정
        main_layout = QVBoxLayout()
        main_layout2 = QHBoxLayout()
        # main_layout에 text_edit 추가
        # main_layout2에 text_label,text_edit2를 추가
        main_layout.addWidget(self.text_edit)
        main_layout2.addWidget(self.text_label)
        main_layout2.addWidget(self.text_edit2)
        # main_layout에 main_layout2 추가
        main_layout.addLayout(main_layout2)
        # main_layout에 buttons_layout을 추가 및 windows에 추가해서 나타나게 함
        main_layout.addLayout(self.buttons_layout)
# central_widget = QWidget(self): This creates a new widget object central_widget with the self argument passed as its parent. self typically refers to the main window object that is calling this code.

# central_widget.setLayout(main_layout): This sets the layout of central_widget to main_layout. A layout is a way of arranging child widgets within a parent widget. There are several different layout types available in PyQt/PySide, such as QHBoxLayout, QVBoxLayout, QGridLayout, etc.

# self.setCentralWidget(central_widget): This sets central_widget as the central widget of the main window. The central widget takes up the majority of the space within the main window and typically contains the main content of the application.

# By using a central widget with a layout, you can easily add and arrange child widgets within the main window. The layout takes care of positioning and sizing the child widgets automatically based on the rules defined by the layout.


# 번역된것
# central_widget = QWidget(self): self 인자를 부모 위젯으로 지정하여 central_widget 객체를 생성합니다. self는 일반적으로 이 코드를 호출하는 주 창 객체를 가리킵니다.

# central_widget.setLayout(main_layout): central_widget의 레이아웃을 main_layout으로 설정합니다. 레이아웃은 부모 위젯 내에서 자식 위젯을 배열하는 방법입니다. PyQt/PySide에서는 QHBoxLayout, QVBoxLayout, QGridLayout 등 다양한 레이아웃 타입이 제공됩니다.

# self.setCentralWidget(central_widget): central_widget을 주 창의 중앙 위젯으로 설정합니다. 중앙 위젯은 일반적으로 애플리케이션의 주요 내용이 들어가는 영역입니다.

# 중앙 위젯과 레이아웃을 사용하면 주 창 내에서 자식 위젯을 쉽게 추가하고 배열할 수 있습니다. 레이아웃은 레이아웃에서 정의한 규칙에 따라 자동으로 자식 위젯을 위치 및 크기를 조정합니다.
        central_widget = QWidget(self)
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def createButtons(self):
        global count
        # buttons을 dictionary로 지정, (key,위치)
        self.buttons = {
            "MC": (0, 0),
            "MR": (0, 1),
            "MS": (0, 2),
            "BS": (0, 3),
            "(": (0, 4),
            "(": (1, 0),
            ")": (1, 1),
            "%": (1, 2),
            "AC": (1, 3),
            "7": (2, 0),
            "8": (2, 1),
            "9": (2, 2),
            "/": (2, 3),
            "4": (3, 0),
            "5": (3, 1),
            "6": (3, 2),
            "*": (3, 3),
            "1": (4, 0),
            "2": (4, 1),
            "3": (4, 2),
            "-": (4, 3),
            "0": (5, 0),
            ".": (5, 1),
            "=": (5, 2),
            "+": (5, 3)
        }

        # buttons_layout을 grid layout으로 지정

        self.buttons_layout = QGridLayout()
        # for문을 이용하여 button 각 위치를 지정
        for btn_text, pos in self.buttons.items():
            # key 값으로 버튼 생성
            button = QPushButton(btn_text)
            # button입력시 hanle_button 함수 실행
            button.clicked.connect(self.handle_button)
            # 각 buttons 위치 추가(value값을 가지고)
            self.buttons_layout.addWidget(button, pos[0], pos[1])
            # buttons 사이즈 지정(50,50)
            button.setFixedSize(50, 50)
            # button 글씨 사이즈 지정(15)
            font = button.font()
            font.setPointSize(15)
            button.setFont(font)

    def handle_button(self):
        # 전역 변수 사용 result_state,MS_number
        global result_state
        global MS_number

        button = self.sender()
        # = 입력시 결과값 나오게
        if button.text() == "=":
            try:
                temp = self.text_edit.text()
                # eval fuction을 이용하여 문자를 계산식으로 변경해서 결과값을 나오게 함
                result = eval(self.text_edit.text())
                # 기존에 있는 text에 button입력 문자(=)과 결과값을 display함
                self.text_edit.setText(temp + button.text() + str(result))
                # "=" 입력시 result_state값을 True로 변경 다음 숫자 입력시 display clear하기 위해(결과 나온디 숫자 입력시 화면 지우기)
                result_state = True
            # eval로 계산시 에러가 발생시 실행(Error display)
            except:
                self.text_edit.setText("Error")
        # "AC" 입력시 display 화면 clear
        elif button.text() == "AC":
            self.text_edit.clear()
        # "BS" 입력시 back space 실행(맨뒤 한개 숫자씩 지우는 기능)
        elif button.text() == "BS":
            text = self.text_edit.text()
            # text 문자 길이가 0 보다 길때 맨위 문자 지움
            if len(text) > 0:
                # [:-1]은 한 글자씩 지우는 방법
                self.text_edit.setText(text[:-1])
                # "MS" 입력시 "="문자 오른쪽 글까를 MS_number에 저장하고 화면을 clear하고, text_edit2에 display힘
        elif button.text() == "MS":
            result_state = False
            MS_number = self.text_edit.text()
            # "=" 글자 이후 글자를 value에 저장함
            # "="이후 글자 다음 글자부터 나머지 다
            value = MS_number[MS_number.index("=")+1:]
            # 화면 지우기
            self.text_edit.clear()
            self.text_edit2.setText(value)
            # 저장된 글자를 text_edit2에 저장함
            MS_number = value
        # "MR" 입력시 "MS"에 입력시 저장된 문자를 불러와서 display에 표시한다.
        elif button.text() == "MR":
            print(MS_number)
            result_state = False
            self.text_edit.setText(self.text_edit.text() + MS_number)
        # "MC" 입력시 "MS"에 저장도니 문자를 지운다.
        elif button.text() == "MC":
            MS_number = ''
            print(MS_number)
            self.text_edit2.setText(MS_number)
        # 위 문자 입력을 제외하고는 입력된 button의 key값을 display한다.
        else:
            # "=" 입력해서 결과가 나온후에 화면을 clear하고 입력된 문자를 입력한다.
            if result_state == True:
                self.text_edit.clear()
                self.text_edit.setText(self.text_edit.text() + button.text())
                result_state = False
            # "=" 입력하기 전이기 때문에 button입력하는 key값을 display한다(기존 화면에 추가해서)
            else:
                self.text_edit.setText(self.text_edit.text() + button.text())

# 위 코드에서 QApplication 클래스는 PyQt 프레임워크에서 GUI 애플리케이션의 제어 흐름과 주요 설정을 관리하는 기본 클래스입니다. MyWidget 클래스는 QWidget 클래스를 상속받은 사용자 정의 클래스로, PyQt에서 사용되는 모든 UI 객체의 기본 클래스입니다.

# if __name__ == "__main__":은 현재 모듈이 메인 프로그램으로 실행되는지 확인하기 위한 일반적인 Python 관용구입니다.

# QApplication 인스턴스는 app 변수에 할당되고, MyWidget 클래스의 새 인스턴스는 widget 변수에 할당됩니다. 그리고 show() 메서드가 widget 객체에 호출되어 화면에 표시됩니다.

# 이후, app.exec() 메서드가 app 객체에 호출되어 애플리케이션 이벤트 루프를 시작합니다. 이벤트 루프는 마우스 클릭 및 키보드 입력과 같은 이벤트를 수신하고 처리합니다. sys.exit() 함수는 app.exec()이 반환한 값을 인수로 사용하여 애플리케이션이 적절하게 종료되도록 보장합니다.

# 총괄적으로, 위 코드는 GUI 애플리케이션의 기본 구조를 설정하고 사용자가 상호 작용할 수 있는 MyWidget 위젯을 화면에 표시합니다. 또한, 사용자가 창을 닫거나 이벤트 루프가 종료될 때 애플리케이션이 적절하게 종료되도록 보장합니다.
if __name__ == "__main__":
    app = QApplication()

    widget = MyWidget()

    widget.show()

    sys.exit(app.exec())
