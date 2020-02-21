# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(681, 467)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icn/volume-2.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.back_toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.back_toolButton.setToolTipDuration(5)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icn/corner-up-left.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back_toolButton.setIcon(icon1)
        self.back_toolButton.setObjectName("back_toolButton")
        self.horizontalLayout.addWidget(self.back_toolButton)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout.addWidget(self.progressBar)
        self.folder_toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.folder_toolButton.setToolTipDuration(5)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icn/plus-square.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.folder_toolButton.setIcon(icon2)
        self.folder_toolButton.setObjectName("folder_toolButton")
        self.horizontalLayout.addWidget(self.folder_toolButton)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.speed_slider = QtWidgets.QSlider(self.centralwidget)
        self.speed_slider.setToolTipDuration(5)
        self.speed_slider.setMinimum(50)
        self.speed_slider.setMaximum(200)
        self.speed_slider.setSingleStep(10)
        self.speed_slider.setPageStep(100)
        self.speed_slider.setProperty("value", 100)
        self.speed_slider.setSliderPosition(100)
        self.speed_slider.setOrientation(QtCore.Qt.Horizontal)
        self.speed_slider.setObjectName("speed_slider")
        self.gridLayout.addWidget(self.speed_slider, 3, 1, 2, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.toss_toolButton = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toss_toolButton.sizePolicy().hasHeightForWidth())
        self.toss_toolButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.toss_toolButton.setFont(font)
        self.toss_toolButton.setToolTipDuration(5)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icn/x.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toss_toolButton.setIcon(icon3)
        self.toss_toolButton.setIconSize(QtCore.QSize(75, 75))
        self.toss_toolButton.setObjectName("toss_toolButton")
        self.horizontalLayout_5.addWidget(self.toss_toolButton)
        self.keep_toolButton = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.keep_toolButton.sizePolicy().hasHeightForWidth())
        self.keep_toolButton.setSizePolicy(sizePolicy)
        self.keep_toolButton.setToolTipDuration(5)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icn/check.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.keep_toolButton.setIcon(icon4)
        self.keep_toolButton.setIconSize(QtCore.QSize(75, 75))
        self.keep_toolButton.setObjectName("keep_toolButton")
        self.horizontalLayout_5.addWidget(self.keep_toolButton)
        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 0, 1, 4)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 4, 1, 1)
        self.vol_slider = QtWidgets.QSlider(self.centralwidget)
        self.vol_slider.setMaximum(100)
        self.vol_slider.setProperty("value", 75)
        self.vol_slider.setOrientation(QtCore.Qt.Vertical)
        self.vol_slider.setInvertedAppearance(False)
        self.vol_slider.setInvertedControls(False)
        self.vol_slider.setTickInterval(10)
        self.vol_slider.setObjectName("vol_slider")
        self.gridLayout.addWidget(self.vol_slider, 3, 0, 3, 1)
        self.play_toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.play_toolButton.setToolTipDuration(5)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icn/play.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play_toolButton.setIcon(icon5)
        self.play_toolButton.setObjectName("play_toolButton")
        self.gridLayout.addWidget(self.play_toolButton, 5, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 0, 4, 1, 1)
        self.name_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(35)
        font.setItalic(True)
        font.setUnderline(True)
        self.name_label.setFont(font)
        self.name_label.setText("")
        self.name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.name_label.setObjectName("name_label")
        self.gridLayout.addWidget(self.name_label, 0, 0, 1, 4)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 2, 1, 3)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 7, 0, 1, 2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.gridLayout.addLayout(self.horizontalLayout_6, 2, 1, 1, 3)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 7, 2, 1, 3)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 2, 1, 1)
        self.skip_toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.skip_toolButton.setToolTipDuration(5)
        self.skip_toolButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icn/skip-forward.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.skip_toolButton.setIcon(icon6)
        self.skip_toolButton.setObjectName("skip_toolButton")
        self.gridLayout.addWidget(self.skip_toolButton, 5, 3, 1, 1)
        self.playback_speed_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.playback_speed_label.setFont(font)
        self.playback_speed_label.setObjectName("playback_speed_label")
        self.gridLayout.addWidget(self.playback_speed_label, 4, 3, 1, 2)
        self.play_entire_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.play_entire_checkBox.setObjectName("play_entire_checkBox")
        self.gridLayout.addWidget(self.play_entire_checkBox, 6, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.vol_slider.valueChanged['int'].connect(MainWindow.set_vol)
        self.speed_slider.valueChanged['int'].connect(MainWindow.set_playback)
        self.play_entire_checkBox.stateChanged['int'].connect(MainWindow.toggle_play_entire)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Audio Sifter"))
        self.back_toolButton.setToolTip(_translate("MainWindow", "Back"))
        self.back_toolButton.setText(_translate("MainWindow", "..."))
        self.folder_toolButton.setToolTip(_translate("MainWindow", "Select Folder"))
        self.folder_toolButton.setText(_translate("MainWindow", "..."))
        self.speed_slider.setToolTip(_translate("MainWindow", "Playback Speed"))
        self.toss_toolButton.setToolTip(_translate("MainWindow", "Toss It"))
        self.toss_toolButton.setText(_translate("MainWindow", "(left arrow)"))
        self.toss_toolButton.setShortcut(_translate("MainWindow", "Left"))
        self.keep_toolButton.setToolTip(_translate("MainWindow", "Keep It"))
        self.keep_toolButton.setText(_translate("MainWindow", "(right arrow)"))
        self.keep_toolButton.setShortcut(_translate("MainWindow", "Right"))
        self.play_toolButton.setToolTip(_translate("MainWindow", "Replay"))
        self.play_toolButton.setText(_translate("MainWindow", "..."))
        self.play_toolButton.setShortcut(_translate("MainWindow", "Down"))
        self.label_2.setText(_translate("MainWindow", "Playback Multiplier"))
        self.label_5.setText(_translate("MainWindow", "Down Arrow Key"))
        self.label.setText(_translate("MainWindow", "Left Arrow Key"))
        self.label_3.setText(_translate("MainWindow", "Right Arrow Key"))
        self.label_6.setText(_translate("MainWindow", "Up Arrow Key"))
        self.label_4.setText(_translate("MainWindow", "X"))
        self.skip_toolButton.setToolTip(_translate("MainWindow", "Skip"))
        self.skip_toolButton.setText(_translate("MainWindow", "..."))
        self.skip_toolButton.setShortcut(_translate("MainWindow", "Up"))
        self.playback_speed_label.setText(_translate("MainWindow", "1.00"))
        self.play_entire_checkBox.setText(_translate("MainWindow", "Play Entire Clip"))
from . import resources_rc
