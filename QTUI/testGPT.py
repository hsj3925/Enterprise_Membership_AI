import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QDialog
from PyQt5.uic import loadUi
from customer import MyDialog
from sss import InventoryForm

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # .ui 파일 로드
        loadUi('mainWindow.ui', self)

        # 메뉴 액션 생성
        self.actionCustomer.triggered.connect(self.openDialogCustomer)
        self.actionInput_Stock.triggered.connect(self.openDialogInputStock)

    def openDialogCustomer(self):
        dialog = MyDialog()
        dialog.exec_()
    
    def openDialogInputStock(self):
        dialog = InventoryForm()
        
if __name__ == '__main__':
    # QApplication 인스턴스 생성
    app = QApplication(sys.argv)

    # MyWindow 인스턴스 생성
    window = MyWindow()

    # 창 보이기
    window.show()

    # 이벤트 루프 진입
    sys.exit(app.exec_())
