import sys

from PyQt4.QtCore import QString, SIGNAL
from PyQt4.QtCore import QTimer
from PyQt4.QtCore import Qt
from PyQt4.QtGui import *
from martianTime import Mars_time
import time


class MyMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.label = QLabel()
        font = self.label.font()
        font.setPointSize(35)
        self.label.setFont(font)
        label = QLabel("Hello from Mars")
        label.setFont(font)

        widget = QWidget(self)
        layout = QVBoxLayout(widget)
        layout.addWidget(label)
        layout.addWidget(self.label)
        layout.setAlignment(self.label, Qt.AlignHCenter)
        layout.setAlignment(label, Qt.AlignHCenter)
        layout.setAlignment(Qt.AlignVCenter)
        self.setCentralWidget(widget)

        self.timer = QTimer()
        self.timer.setInterval(370)
        self.connect(self.timer, SIGNAL("timeout()"), self.update_label)
        self.timer.start()

    def update_label(self):
        myTime = Mars_time(float(time.time()))
        self.label.setText(self.get_martian_time_string())

    def get_martian_time_string(self):
        mTime = Mars_time(float(time.time()))
        return QString("Year %1 Month %3 Sol %2 Hour %4").arg(mTime.getYear()).arg(mTime.getSol()).arg(
            mTime.getMonth()).arg(QString.number(mTime.getHour(), 'f', 4))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = MyMainWindow()
    mainwindow.setWindowTitle("Marscroft")
    mainwindow.showFullScreen()
    app.exec_()
