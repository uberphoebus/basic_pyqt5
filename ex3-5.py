import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtWidgets import QPushButton, QToolTip
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication

class MyApp(QMainWindow): # 메인 창
    
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.statusBar().showMessage('ready') # 상태바 메세지 설정
        
        QToolTip.setFont(QFont('SansSefit', 10)) # 폰트, 크기
        self.setToolTip('This is a <b>Qwidget</b> widget') # 툴팁
        
        btn0 = QPushButton('Btn', self)
        btn0.setToolTip('This is a <b>QPushBtn</b> widget')
        btn0.move(50, 50) # 버튼 위치
        btn0.resize(btn0.sizeHint()) # 버튼 크기(적절하게)
        
        btn1 = QPushButton('Quit', self) # 푸시 버튼 객체(텍스트, 표시될 부모 위젯)
        btn1.move(200, 50)
        btn1.resize(btn1.sizeHint())
        btn1.clicked.connect(QCoreApplication.instance().quit)
        
        self.setWindowTitle('Quit Btn') # 창 제목
        self.setGeometry(300, 300, 300, 200) # 창 위치과 크기
        self.show() # 위젯을 스크린에 보여줌

if __name__ == '__main__':
    app = QApplication(sys.argv) # app 객체 생성
    ex = MyApp()
    sys.exit(app.exec_())