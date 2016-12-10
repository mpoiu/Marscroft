import sys

from PyQt4.QtCore import QString
from PyQt4.QtGui import *
from martianTime import Mars_time
import time


class MyMainWindow(QMainWindow):
    def __init__(self, parent = None):
        super(MyMainWindow, self).__init__(parent)
        myTime = Mars_time(int(time.time()))
        self.label = QLabel(QString( "Hello from Mars Year %1 Month %3 Sol %2 Hour %4" ).arg( myTime.getYear()).arg(myTime.getSol()) .arg(myTime.getMonth()) .arg(myTime.getHour()), self)
        self.setCentralWidget(self.label)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = MyMainWindow()
    mainwindow.setWindowTitle("Marscroft")
    mainwindow.show()
    app.exec_()



