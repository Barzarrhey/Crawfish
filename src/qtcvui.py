# -*- coding: utf-8 -*-
# Created by barzarrhey on 2018/6/3

# Form implementation generated from reading ui file './ui/pyqt5_opencv.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1184, 719)
        MainWindow.setMouseTracking(False)
        MainWindow.setStatusTip("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.buttonLoad = QtWidgets.QPushButton(self.centralwidget)
        self.buttonLoad.setGeometry(QtCore.QRect(150, 680, 100, 27))
        self.buttonLoad.setObjectName("buttonLoad")
        self.buttonStart = QtWidgets.QPushButton(self.centralwidget)
        self.buttonStart.setGeometry(QtCore.QRect(930, 680, 100, 27))
        self.buttonStart.setObjectName("buttonStart")
        self.buttonPause = QtWidgets.QPushButton(self.centralwidget)
        self.buttonPause.setGeometry(QtCore.QRect(1060, 680, 100, 27))
        self.buttonPause.setObjectName("buttonPause")
        self.buttonCamera = QtWidgets.QPushButton(self.centralwidget)
        self.buttonCamera.setGeometry(QtCore.QRect(20, 680, 100, 27))
        self.buttonCamera.setObjectName("buttonCamera")
        self.videoWidget = QtWidgets.QLabel(self.centralwidget)
        self.videoWidget.setGeometry(QtCore.QRect(0, 0, 1184, 666))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.videoWidget.setFont(font)
        self.videoWidget.setMouseTracking(True)
        self.videoWidget.setAutoFillBackground(True)
        self.videoWidget.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.videoWidget.setObjectName("videoWidget")
        self.labelTrack = QtWidgets.QLabel(self.centralwidget)
        self.labelTrack.setGeometry(QtCore.QRect(635, 20, 531, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelTrack.setFont(font)
        self.labelTrack.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelTrack.setObjectName("labelTrack")
        self.buttonCal = QtWidgets.QPushButton(self.centralwidget)
        self.buttonCal.setGeometry(QtCore.QRect(800, 680, 100, 27))
        self.buttonCal.setObjectName("buttonCal")
        self.labelPos = QtWidgets.QLabel(self.centralwidget)
        self.labelPos.setGeometry(QtCore.QRect(630, 60, 531, 19))
        self.labelPos.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelPos.setObjectName("labelPos")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "OpenCV"))
        self.buttonLoad.setText(_translate("MainWindow", "Load Video"))
        self.buttonStart.setText(_translate("MainWindow", "Start"))
        self.buttonPause.setText(_translate("MainWindow", "Pause"))
        self.buttonCamera.setText(_translate("MainWindow", "Camera"))
        self.videoWidget.setText(_translate("MainWindow", "<html><head/><body><p><br/></p><p>How to use it?<br/>1. Start camera or select a video file.</p><p><br/></p><p>2. hold down the left mouse button to draw a rectangle which contain all the object.</p><p><br/></p><p>3. (optional)Calibrate is used when you need the truth length, hold down the left mouse button to draw a line and provide its true length.</p><p><br/></p><p>Attention:</p><p><br/></p><p>· keep the carema parallel to the plane of the object</p><p><br/></p><p>· keep the background clean and keep a high contrast to the color of the object to be observed.</p><p><br/></p><p>version:0.9(本软件基于MIT协议开源免费)</p><p>                    Designed By Barzarrhey &amp; Cookie<br/></p></body></html>"))
        self.labelTrack.setText(_translate("MainWindow", "<font color=\'green\'>(x, y)</font>"))
        self.buttonCal.setText(_translate("MainWindow", "Calibrate"))
        self.labelPos.setText(_translate("MainWindow", "(x, y) m"))

