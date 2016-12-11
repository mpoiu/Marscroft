# -*- coding: utf-8 -*-
import sys

from PyQt4.QtCore import QString, SIGNAL
from PyQt4.QtCore import QTimer
from PyQt4.QtCore import Qt
from PyQt4.QtGui import *
from martianTime import Mars_time
import time

from martianWeather import MarsWeather


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
        font.setPointSize(100)
        self.labelHour.setFont(font)
        font.setPointSize(60)
        self.labelYear.setFont(font)
        labelDash1.setFont(font)
        self.labelMonth.setFont(font)
        labelDash2.setFont(font)
        self.labelDay.setFont(font)
        font.setPointSize(20)
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

        weather_widget = QWidget()
        grid_weather = QGridLayout(weather_widget)
        self.label_min_temp = QLabel()
        self.label_max_temp = QLabel()
        self.label_pressure = QLabel()
        self.label_wind_speed = QLabel()
        self.label_min_temp.setStyleSheet(style)
        self.label_max_temp.setStyleSheet(style)
        self.label_pressure.setStyleSheet(style)
        self.label_wind_speed.setStyleSheet(style)
        self.label_min_temp.setFont(font)
        self.label_max_temp.setFont(font)
        self.label_pressure.setFont(font)
        self.label_wind_speed.setFont(font)
        grid_weather.addWidget(self.label_min_temp, 0, 0)
        grid_weather.addWidget(self.label_max_temp, 0, 1)
        grid_weather.addWidget(self.label_pressure, 1, 0)
        grid_weather.addWidget(self.label_wind_speed, 1, 1)
        grid_weather.setSpacing(20)

        widget = QWidget(self)
        widget.setStyleSheet("QWidget { background-color: #FF6625 }")
        layout = QVBoxLayout(widget)
        button = QPushButton("Autodestruction")
        button.setStyleSheet("QPushButton{color:white;background-color:black}")
        layout.addWidget(button)
        layout.setAlignment(button, Qt.AlignRight | Qt.AlignTop)
        layout.addWidget(self.labelHour)
        layout.addWidget(grid_widget)
        myFrame = QFrame()
        myFrame.setFrameShape(QFrame.HLine)
        myFrame.setStyleSheet("QFrame { color: white }")
        layout.addWidget(myFrame)
        layout.addWidget(weather_widget)
        layout.setAlignment(self.labelHour, Qt.AlignHCenter)
        layout.setAlignment(grid_widget, Qt.AlignHCenter)
        layout.setAlignment(weather_widget, Qt.AlignHCenter)
        layout.setAlignment(Qt.AlignVCenter)

        self.setCentralWidget(widget)

        self.timer = QTimer()
        self.timer.setInterval(370)
        self.connect(self.timer, SIGNAL("timeout()"), self.update_labels)
        self.timer.start()

        self.weather_timer = QTimer()
        self.weather_timer.setInterval(300000)
        self.connect(self.timer, SIGNAL("timeout()"), self.update_weather)
        self.weather_timer.start()

    def update_labels(self):
        mTime = Mars_time(float(time.time()))
        self.labelHour.setText(QString.number(mTime.getHour(), 'f', 4))
        self.labelYear.setText(QString.number(mTime.getYear()))
        self.labelMonth.setText(QString.number(mTime.getMonth()))
        self.labelDay.setText(QString.number(mTime.getSol()))

    def update_weather(self):
        weather = MarsWeather()
        min_temp = weather.getMinTemp()
        min_temp_string = QString("Min. Temp: ")
        if min_temp != None:
            min_temp_string.append(QString(u"%1 °C").arg(min_temp))
        else:
            min_temp_string.append("No data")
        self.label_min_temp.setText(min_temp_string)

        max_temp = weather.getMaxTemp()
        max_temp_string = QString("Max. Temp: ")
        if max_temp != None:
            max_temp_string.append(QString(u"%1 °C").arg(max_temp))
        else:
            max_temp_string.append("No data")
        self.label_max_temp.setText(max_temp_string)

        pressure = weather.getPressure()
        pressure_string = QString("Pressure: ")
        if pressure != None:
            pressure_string.append(QString("%1 Pa").arg(pressure))
        else:
            pressure_string.append("No data")
        self.label_pressure.setText(pressure_string)

        wind_speed = weather.getWindSpeed()
        wind_speed_string = QString("Wind speed: ")
        if wind_speed != None:
            wind_speed_string.append(QString("%1 km/h").arg(wind_speed))
        else:
            wind_speed_string.append("No data")
        self.label_wind_speed.setText(wind_speed_string)


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
