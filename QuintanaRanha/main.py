from ventMain import *
import sys

class Main(QtWidgets.QMainWindow):
    def __int__(self):
        super(Main, self).__int__()
        self.ui = Ui_ventMain
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())


