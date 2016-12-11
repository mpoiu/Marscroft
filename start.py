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
        self.label1 = QLabel()
        self.label2 = QLabel()
        font = self.label1.font()
        font.setPointSize(35)
        self.label1.setFont(font)
        self.label2.setFont(font)
        style = "QLabel { color: white }"
        self.label1.setStyleSheet(style)
        self.label2.setStyleSheet(style)

        widget = QWidget(self)
        widget.setStyleSheet("QWidget { background-color: orange }")
        layout = QVBoxLayout(widget)
        layout.addWidget(self.label1)
        layout.addWidget(self.label2)
        layout.setAlignment(self.label1, Qt.AlignHCenter)
        layout.setAlignment(self.label2, Qt.AlignHCenter)
        layout.setAlignment(Qt.AlignVCenter)
        self.setCentralWidget(widget)

        self.timer = QTimer()
        self.timer.setInterval(370)
        self.connect(self.timer, SIGNAL("timeout()"), self.update_labels)
        self.timer.start()

    def update_labels(self):
        self.label1.setText(self.get_martian_hour_string())
        self.label2.setText(self.get_martian_date_string())

    def get_martian_date_string(self):
        mTime = Mars_time(float(time.time()))
        return QString("%1-%3-%2").arg(mTime.getYear()).arg(mTime.getSol()).arg(
            mTime.getMonth())

    def get_martian_hour_string(self):
        mTime = Mars_time(float(time.time()))
        return QString.number(mTime.getHour(), 'f', 4)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = MyMainWindow()
    mainwindow.setWindowTitle("Marscroft")
    mainwindow.showFullScreen()
    app.exec_()
