# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(464, 264)
        MainWindow.setMinimumSize(QtCore.QSize(464, 264))
        MainWindow.setMaximumSize(QtCore.QSize(464, 264))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.toggleswitch = QtGui.QPushButton(self.centralwidget)
        self.toggleswitch.setGeometry(QtCore.QRect(20, 30, 75, 23))
        self.toggleswitch.setObjectName(_fromUtf8("toggleswitch"))
        self.Spang = QtGui.QRadioButton(self.centralwidget)
        self.Spang.setGeometry(QtCore.QRect(40, 90, 131, 21))
        self.Spang.setObjectName(_fromUtf8("Spang"))
        self.aesthetics = QtGui.QRadioButton(self.centralwidget)
        self.aesthetics.setGeometry(QtCore.QRect(40, 120, 151, 21))
        self.aesthetics.setObjectName(_fromUtf8("aesthetics"))
        self.zalgo = QtGui.QRadioButton(self.centralwidget)
        self.zalgo.setGeometry(QtCore.QRect(40, 140, 261, 41))
        self.zalgo.setObjectName(_fromUtf8("zalgo"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 55, 91, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.owo = QtGui.QRadioButton(self.centralwidget)
        self.owo.setGeometry(QtCore.QRect(40, 180, 211, 21))
        self.owo.setObjectName(_fromUtf8("owo"))
        self.aestheticsSettings = QtGui.QComboBox(self.centralwidget)
        self.aestheticsSettings.setGeometry(QtCore.QRect(310, 120, 131, 20))
        self.aestheticsSettings.setObjectName(_fromUtf8("aestheticsSettings"))
        self.zalgoSettings = QtGui.QComboBox(self.centralwidget)
        self.zalgoSettings.setGeometry(QtCore.QRect(310, 150, 131, 20))
        self.zalgoSettings.setObjectName(_fromUtf8("zalgoSettings"))
        self.owoSettings = QtGui.QComboBox(self.centralwidget)
        self.owoSettings.setGeometry(QtCore.QRect(310, 180, 131, 20))
        self.owoSettings.setMinimumSize(QtCore.QSize(131, 20))
        self.owoSettings.setMaximumSize(QtCore.QSize(131, 20))
        self.owoSettings.setObjectName(_fromUtf8("owoSettings"))
        self.Killme = QtGui.QPushButton(self.centralwidget)
        self.Killme.setGeometry(QtCore.QRect(370, 30, 71, 23))
        self.Killme.setObjectName(_fromUtf8("Killme"))
        self.endisable = QtGui.QLabel(self.centralwidget)
        self.endisable.setGeometry(QtCore.QRect(100, 30, 261, 21))
        self.endisable.setAlignment(QtCore.Qt.AlignCenter)
        self.endisable.setObjectName(_fromUtf8("endisable"))
        self.Start = QtGui.QPushButton(self.centralwidget)
        self.Start.setGeometry(QtCore.QRect(20, 212, 421, 41))
        self.Start.setObjectName(_fromUtf8("Start"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "There\'s a reason I shouldn\'t know how to program.exe", None))
        self.toggleswitch.setToolTip(_translate("MainWindow", "Click to set/change toggle key", None))
        self.toggleswitch.setText(_translate("MainWindow", "Toggle:", None))
        self.Spang.setText(_translate("MainWindow", "SpAnGeBeB", None))
        self.aesthetics.setText(_translate("MainWindow", "( ( ( A E S T H E T I C S ) ) )", None))
        self.zalgo.setText(_translate("MainWindow", "Ḫ̗͔͕̖̘ͥ͂͒̒ͬ͝E͖̳̤̘͇̭͇ͦ̅ͨͭͧ̒ ̤̘͕ͫͪ̂̌̍ͧ͝C̗͖̗̖̦̆̐̔̾ͯ̄̿͟Ȍ̴̺͌ͨ̇͋̉̕͡M̸͕͍̳͔̻̿̒͞Ẻ̞̭̖ͣ̀͑ͨͥ̀͝S͔̖͈̜̤͔̻͛ͯ̇ͦ̀͠  (PLEASE BE PATIENT WITH THIS)", None))
        self.label.setText(_translate("MainWindow", "Style of meme:", None))
        self.owo.setText(_translate("MainWindow", "*Notices radio button* OwO wuts dis?", None))
        self.Killme.setText(_translate("MainWindow", "Kill Switch", None))
        self.endisable.setText(_translate("MainWindow", "Disabled", None))
        self.Start.setText(_translate("MainWindow", "Let\'s start this cancer", None))

