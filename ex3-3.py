import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class MyApp(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        btn = QPushButton('Quit', self) # 푸시 버튼 객체(텍스트, 표시될 부모 위젯)
        btn.move(50, 50)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)
        
        self.setWindowTitle('Quit Btn') # 창 제목
        self.setGeometry(300, 300, 300, 200) # 창 위치과 크기
        self.show() # 위젯을 스크린에 보여줌

if __name__ == '__main__':
    app = QApplication(sys.argv) # app 객체 생성
    ex = MyApp()
    sys.exit(app.exec_())