# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.resources\About.ui'
#
# Created: Fri May 20 11:59:17 2016
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

class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName(_fromUtf8("About"))
        About.resize(600, 300)
        About.setMinimumSize(QtCore.QSize(600, 300))
        About.setMaximumSize(QtCore.QSize(600, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/images/info.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        About.setWindowIcon(icon)
        self.label = QtGui.QLabel(About)
        self.label.setGeometry(QtCore.QRect(20, 20, 91, 91))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/imgMagnifier/images/icon.png")))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.textEdit = QtGui.QTextEdit(About)
        self.textEdit.setEnabled(True)
        self.textEdit.setGeometry(QtCore.QRect(140, 10, 451, 251))
        self.textEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textEdit.setFrameShape(QtGui.QFrame.NoFrame)
        self.textEdit.setFrameShadow(QtGui.QFrame.Raised)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.pushButton_2 = QtGui.QPushButton(About)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 270, 451, 23))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.retranslateUi(About)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), About.ShowVideo)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        About.setWindowTitle(_translate("About", "About", None))
        self.textEdit.setHtml(_translate("About", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Magnifying Glass</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">2016-Francisco Raga</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Maps with a Magnifying Glass Tool for Qgis.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">This plugin provides the “</span><span style=\" font-size:8pt; font-weight:600;\">magnifying glass</span><span style=\" font-size:8pt;\">” tool to compare maps from different providers. The idea is quite simple, but if you don’t want to dig into the code, here is the trick.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Two </span><span style=\" font-size:8pt; font-weight:600;\">SlippyMaps</span><span style=\" font-size:8pt;\"> are created, the first one serves as an on-top map and the second is rendered below the first and it is the one that is used as “</span><span style=\" font-size:8pt; font-weight:600;\">magnifying glass</span><span style=\" font-size:8pt;\">” clipped to the shape of a circle. Simple, isn’t it? Of course, you can still move the maps by dragging the mouse and you can change the maps.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">How It Works</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">To activate the magnifier you simply have to press &quot;</span><span style=\" font-size:8pt; font-weight:600;\">left-click</span><span style=\" font-size:8pt;\">&quot; and </span><span style=\" font-size:8pt; font-weight:600;\">hold</span><span style=\" font-size:8pt;\"> it down while moving around the map.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">You can also leave a magnifying glass fixed with a simple &quot;</span><span style=\" font-size:8pt; font-weight:600;\">left-click</span><span style=\" font-size:8pt;\">&quot; and move it over the map with the arrow keys of your keyboard to remove it, you have to press &quot;</span><span style=\" font-size:8pt; font-weight:600;\">right-click</span><span style=\" font-size:8pt;\">&quot;.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Finally, through the combos above, you can choose the base maps to show both in the map and in the magnifying glass.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/imgMagnifier/images/Screenshot.png\" width=\"400\" height=\"700\" /></p></body></html>", None))
        self.pushButton_2.setText(_translate("About", "Show Video example", None))

import resources_rc
