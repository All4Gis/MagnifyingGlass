# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.resources\Ui_Magnifier.ui'
#
# Created: Thu May 19 16:23:17 2016
#      by: PyQt4 UI code generator 4.11.3
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

class Ui_MagnifierDock(object):
    def setupUi(self, MagnifierDock):
        MagnifierDock.setObjectName(_fromUtf8("MagnifierDock"))
        MagnifierDock.resize(300, 300)
        MagnifierDock.setMinimumSize(QtCore.QSize(300, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/imgMagnifier/images/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MagnifierDock.setWindowIcon(icon)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.infoButton = QtGui.QPushButton(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.infoButton.sizePolicy().hasHeightForWidth())
        self.infoButton.setSizePolicy(sizePolicy)
        self.infoButton.setMinimumSize(QtCore.QSize(0, 20))
        self.infoButton.setMaximumSize(QtCore.QSize(16777215, 20))
        self.infoButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.infoButton.setStyleSheet(_fromUtf8("QPushButton {border-radius: 3px} QPushButton:hover {background-color: #FFFFFF}"))
        self.infoButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/imgMagnifier/images/info.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.infoButton.setIcon(icon1)
        self.infoButton.setFlat(False)
        self.infoButton.setObjectName(_fromUtf8("infoButton"))
        self.verticalLayout.addWidget(self.infoButton)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.groupBox = QtGui.QGroupBox(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.CmbNomalMap = QtGui.QComboBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CmbNomalMap.sizePolicy().hasHeightForWidth())
        self.CmbNomalMap.setSizePolicy(sizePolicy)
        self.CmbNomalMap.setMouseTracking(True)
        self.CmbNomalMap.setObjectName(_fromUtf8("CmbNomalMap"))
        self.verticalLayout_2.addWidget(self.CmbNomalMap)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.CmbGlassMap = QtGui.QComboBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CmbGlassMap.sizePolicy().hasHeightForWidth())
        self.CmbGlassMap.setSizePolicy(sizePolicy)
        self.CmbGlassMap.setMouseTracking(True)
        self.CmbGlassMap.setObjectName(_fromUtf8("CmbGlassMap"))
        self.verticalLayout_3.addWidget(self.CmbGlassMap)
        self.horizontalLayout_2.addWidget(self.groupBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.CanvasLayout = QtGui.QGridLayout()
        self.CanvasLayout.setObjectName(_fromUtf8("CanvasLayout"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.CanvasLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.CanvasLayout)
        self.check_sync = QtGui.QCheckBox(self.dockWidgetContents)
        self.check_sync.setEnabled(False)
        self.check_sync.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.check_sync.setCheckable(True)
        self.check_sync.setChecked(False)
        self.check_sync.setObjectName(_fromUtf8("check_sync"))
        self.verticalLayout.addWidget(self.check_sync)
        MagnifierDock.setWidget(self.dockWidgetContents)

        self.retranslateUi(MagnifierDock)
        self.CmbNomalMap.setCurrentIndex(-1)
        self.CmbGlassMap.setCurrentIndex(-1)
        QtCore.QObject.connect(self.CmbNomalMap, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), MagnifierDock.ChangeBaseMap)
        QtCore.QObject.connect(self.CmbGlassMap, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), MagnifierDock.ChangeBaseMap)
        QtCore.QObject.connect(self.infoButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MagnifierDock.About)
        QtCore.QMetaObject.connectSlotsByName(MagnifierDock)

    def retranslateUi(self, MagnifierDock):
        MagnifierDock.setWindowTitle(_translate("MagnifierDock", "Magnifying Glass", None))
        self.infoButton.setToolTip(_translate("MagnifierDock", "Info", None))
        self.groupBox.setTitle(_translate("MagnifierDock", "Normal Map", None))
        self.groupBox_2.setTitle(_translate("MagnifierDock", "Glass Map", None))
        self.check_sync.setText(_translate("MagnifierDock", "Sync Canvas Extend", None))

import resources_rc
