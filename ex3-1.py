import sys
from PyQt5.QtWidgets import QApplication, QWidget

class MyApp(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('My App') # 창 제목
        self.move(300, 300) # 위젯 위치 이동
        self.resize(400, 200) # 위젯 크기 조절
        self.show() # 위젯을 스크린에 보여줌

if __name__ == '__main__':
    app = QApplication(sys.argv) # app 객체 생성
    ex = MyApp()
    sys.exit(app.exec_())