import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class MyApp(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('Icon') # 창 제목
        self.setWindowIcon(QIcon('web.png')) # app 아이콘
        self.setGeometry(300, 300, 300, 200) # 창 위치과 크기
        self.show() # 위젯을 스크린에 보여줌

if __name__ == '__main__':
    app = QApplication(sys.argv) # app 객체 생성
    ex = MyApp()
    sys.exit(app.exec_())