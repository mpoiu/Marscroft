import sys
from PyQt4.QtGui import *

class MyMainWindow(QMainWindow):
    def __init__(self, parent = None):
        super(MyMainWindow, self).__init__(parent)
        self.label = QLabel("Hello from Mars", self)
        self.setCentralWidget(self.label)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = MyMainWindow()
    mainwindow.setWindowTitle("Marscroft")
    mainwindow.show()
    app.exec_()