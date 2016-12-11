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
        self.labelHour = QLabel()
        self.labelYear = QLabel()
        labelDash1 = QLabel("-")
        self.labelMonth = QLabel()
        labelDash2 = QLabel("-")
        self.labelDay = QLabel()
        labelYearS = QLabel("Year")
        labelMonthS = QLabel("Month")
        labelDayS = QLabel("Day")

        font = self.labelHour.font()
        font.setPointSize(120)
        self.labelHour.setFont(font)
        font.setPointSize(70)
        self.labelYear.setFont(font)
        labelDash1.setFont(font)
        self.labelMonth.setFont(font)
        labelDash2.setFont(font)
        self.labelDay.setFont(font)
        font.setPointSize(30)
        labelYearS.setFont(font)
        labelMonthS.setFont(font)
        labelDayS.setFont(font)

        style = "QLabel { color: white }"
        self.labelHour.setStyleSheet(style)
        self.labelYear.setStyleSheet(style)
        labelDash1.setStyleSheet(style)
        self.labelMonth.setStyleSheet(style)
        labelDash2.setStyleSheet(style)
        self.labelDay.setStyleSheet(style)
        labelYearS.setStyleSheet(style)
        labelMonthS.setStyleSheet(style)
        labelDayS.setStyleSheet(style)

        grid_widget = QWidget()
        grid_layout = QGridLayout(grid_widget)
        grid_layout.setAlignment(Qt.AlignHCenter)
        grid_layout.addWidget(self.labelYear, 0, 0)
        grid_layout.addWidget(labelDash1, 0, 1)
        grid_layout.addWidget(self.labelMonth, 0, 2)
        grid_layout.addWidget(labelDash2, 0, 3)
        grid_layout.addWidget(self.labelDay, 0, 4)
        grid_layout.addWidget(labelYearS, 1, 0)
        grid_layout.addWidget(labelMonthS, 1, 2)
        grid_layout.addWidget(labelDayS, 1, 4)

        widget = QWidget(self)
        widget.setStyleSheet("QWidget { background-color: #FF6625 }")
        layout = QVBoxLayout(widget)
        layout.addWidget(self.labelHour)
        layout.addWidget(grid_widget)
        layout.setAlignment(self.labelHour, Qt.AlignHCenter)
        layout.setAlignment(grid_widget, Qt.AlignHCenter)
        layout.setAlignment(Qt.AlignVCenter)
        self.setCentralWidget(widget)
        self.timer = QTimer()
        self.timer.setInterval(370)
        self.connect(self.timer, SIGNAL("timeout()"), self.update_labels)
        self.timer.start()

    def update_labels(self):
        mTime = Mars_time(float(time.time()))
        self.labelHour.setText(QString.number(mTime.getHour(), 'f', 4))
        self.labelYear.setText(QString.number(mTime.getYear()))
        self.labelMonth.setText(QString.number(mTime.getMonth()))
        self.labelDay.setText(QString.number(mTime.getSol()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = MyMainWindow()
    mainwindow.setWindowTitle("Marscroft")

    rec = QDesktopWidget().screenGeometry()
    height = rec.height()
    width = rec.width()
    if height <= 600 and width <= 800:
        mainwindow.showFullScreen()
    else:
        mainwindow.setFixedSize(800, 600)
        mainwindow.show()
    app.exec_()
