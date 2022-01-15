import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtWidgets import QPushButton, QToolTip
from PyQt5.QtWidgets import QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication

class MyApp(QMainWindow): # 메인 창
    
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        
        exitAction = QAction(QIcon('exit.png'), 'Exit', self) # 아이콘과 액션 생성
        exitAction.setShortcut('Ctrl+Q') # 액션의 단축키 정의
        exitAction.setStatusTip('Exit App') # 메뉴에 마우스를 올렸을 때 상태바에 표시
        exitAction.triggered.connect(qApp.quit) # 동작을 선택했을 때 위젯의 메서드에 연결
        
        self.statusBar()
        
        self.toolbar = self.addToolBar('Exit') # 툴바를 만듦
        self.toolbar.addAction(exitAction) # 툴바에 액션 연결
        
        menubar = self.menuBar() # 메뉴바 생성
        menubar.setNativeMenuBar(False) # 맥에서 윈도우 형식으로 다루도록
        filemenu = menubar.addMenu('&File') # 메뉴를 만들고 간편단축키 설정
        filemenu.addAction(exitAction) # 파일메뉴에 액션 추가
        
        QToolTip.setFont(QFont('SansSefit', 10)) # 폰트, 크기
        self.setToolTip('This is a <b>Qwidget</b> widget') # 툴팁
        
        btn0 = QPushButton('Btn', self)
        btn0.setToolTip('This is a <b>QPushBtn</b> widget')
        btn0.move(50, 100) # 버튼 위치
        btn0.resize(btn0.sizeHint()) # 버튼 크기(적절하게)
        
        btn1 = QPushButton('Quit', self) # 푸시 버튼 객체(텍스트, 표시될 부모 위젯)
        btn1.move(200, 100)
        btn1.resize(btn1.sizeHint())
        btn1.clicked.connect(QCoreApplication.instance().quit)
        
        self.setWindowTitle('Quit Btn') # 창 제목
        self.setGeometry(300, 300, 300, 200) # 창 위치과 크기
        self.show() # 위젯을 스크린에 보여줌

if __name__ == '__main__':
    app = QApplication(sys.argv) # app 객체 생성
    ex = MyApp()
    sys.exit(app.exec_())