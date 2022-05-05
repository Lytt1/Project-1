from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Remote(object):
    def setupUi(self, Remote):
        Remote.setObjectName("Remote")
        Remote.resize(452, 835)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        Remote.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(Remote)
        self.centralwidget.setObjectName("centralwidget")
        self.power_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.toggle_power())
        self.power_button.setGeometry(QtCore.QRect(324, 20, 101, 81))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.power_button.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.power_button.setFont(font)
        self.power_button.setObjectName("power_button")
        self.volume_up_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.volume_up())
        self.volume_up_button.setGeometry(QtCore.QRect(180, 230, 101, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.volume_up_button.setFont(font)
        self.volume_up_button.setObjectName("volume_up_button")
        self.volume_down_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.volume_down())
        self.volume_down_button.setGeometry(QtCore.QRect(180, 360, 101, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.volume_down_button.setFont(font)
        self.volume_down_button.setObjectName("volume_down_button")
        self.prev_channel_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.prev_channel())
        self.prev_channel_button.setGeometry(QtCore.QRect(80, 300, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.prev_channel_button.setFont(font)
        self.prev_channel_button.setObjectName("prev_channel_button")
        self.next_channel_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.next_channel())
        self.next_channel_button.setGeometry(QtCore.QRect(284, 300, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.next_channel_button.setFont(font)
        self.next_channel_button.setObjectName("next_channel_button")
        self.zero_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.channel_zero())
        self.zero_button.setGeometry(QtCore.QRect(190, 762, 75, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.zero_button.setFont(font)
        self.zero_button.setObjectName("zero_button")
        self.one_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.channel_one())
        self.one_button.setGeometry(QtCore.QRect(80, 712, 75, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.one_button.setFont(font)
        self.one_button.setObjectName("one_button")
        self.two_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.channel_two())
        self.two_button.setGeometry(QtCore.QRect(190, 712, 75, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.two_button.setFont(font)
        self.two_button.setObjectName("two_button")
        self.three_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.channel_three())
        self.three_button.setGeometry(QtCore.QRect(300, 712, 75, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.three_button.setFont(font)
        self.three_button.setObjectName("three_button")
        self.four_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.channel_four())
        self.four_button.setGeometry(QtCore.QRect(80, 662, 75, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.four_button.setFont(font)
        self.four_button.setObjectName("four_button")
        self.five_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.channel_five())
        self.five_button.setGeometry(QtCore.QRect(190, 662, 75, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.five_button.setFont(font)
        self.five_button.setObjectName("five_button")
        self.six_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.channel_six())
        self.six_button.setGeometry(QtCore.QRect(300, 662, 75, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.six_button.setFont(font)
        self.six_button.setObjectName("six_button")
        self.seven_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.channel_seven())
        self.seven_button.setGeometry(QtCore.QRect(80, 610, 75, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.seven_button.setFont(font)
        self.seven_button.setObjectName("seven_button")
        self.eight_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.channel_eight())
        self.eight_button.setGeometry(QtCore.QRect(190, 610, 75, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.eight_button.setFont(font)
        self.eight_button.setObjectName("eight_button")
        self.nine_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.channel_nine())
        self.nine_button.setGeometry(QtCore.QRect(300, 610, 75, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.nine_button.setFont(font)
        self.nine_button.setObjectName("nine_button")
        Remote.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Remote)
        self.statusbar.setObjectName("statusbar")
        Remote.setStatusBar(self.statusbar)

        self.retranslateUi(Remote)
        QtCore.QMetaObject.connectSlotsByName(Remote)

    def retranslateUi(self, Remote):
        _translate = QtCore.QCoreApplication.translate
        Remote.setWindowTitle(_translate("Remote", "TV Remote"))
        self.power_button.setText(_translate("Remote", "POWER"))
        self.volume_up_button.setText(_translate("Remote", "VOLUME UP"))
        self.volume_down_button.setText(_translate("Remote", "VOLUME DOWN"))
        self.prev_channel_button.setText(_translate("Remote", "PREV CHANNEL"))
        self.next_channel_button.setText(_translate("Remote", "NEXT CHANNEL"))
        self.zero_button.setText(_translate("Remote", "0"))
        self.one_button.setText(_translate("Remote", "1"))
        self.two_button.setText(_translate("Remote", "2"))
        self.three_button.setText(_translate("Remote", "3"))
        self.four_button.setText(_translate("Remote", "4"))
        self.five_button.setText(_translate("Remote", "5"))
        self.six_button.setText(_translate("Remote", "6"))
        self.seven_button.setText(_translate("Remote", "7"))
        self.eight_button.setText(_translate("Remote", "8"))
        self.nine_button.setText(_translate("Remote", "9"))

class Television:

    def __init__(self):
        self.channel = 0
        self.volume = 0
        self.on = False
        pass

    def toggle_power(self):
        if self.on == False:
            self.on = True
        else:
            self.on = False
        pass

    def volume_up(self):
        if self.on == True:
            if self.volume < 20:
                self.volume += 1
        pass

    def volume_down(self):
        if self.on == True:
            if self.volume > 0:
                self.volume -= 1
        pass

    def next_channel(self):
        if self.on == True:
            if self.channel == 9:
                self.channel = 0
            else:
                self.channel += 1
        pass

    def prev_channel(self):
        if self.on == True:
            if self.channel == 0:
                self.channel = 9
            else:
                self.channel -= 1
        pass

    def channel_zero(self):
        if self.on == True:
            self.channel = 0
        pass

    def channel_one(self):
        if self.on == True:
            self.channel = 1
        pass

    def channel_two(self):
        if self.on == True:
            self.channel = 2
        pass

    def channel_three(self):
        if self.on == True:
            self.channel = 3
        pass

    def channel_four(self):
        if self.on == True:
            self.channel = 4
        pass

    def channel_five(self):
        if self.on == True:
            self.channel = 5
        pass

    def channel_six(self):
        if self.on == True:
            self.channel = 6
        pass

    def channel_seven(self):
        if self.on == True:
            self.channel = 7
        pass

    def channel_eight(self):
        if self.on == True:
            self.channel = 8
        pass

    def channel_nine(self):
        if self.on == True:
            self.channel = 9
        pass

    def __str__(self):
        return ("Diagnostics: Is on = {}, Channel = {}, Volume = {}".format(self.on, self.channel, self.volume))
        pass


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Remote = QtWidgets.QMainWindow()
    ui = Ui_Remote()
    ui.setupUi(Remote)
    Remote.show()
    sys.exit(app.exec_())

