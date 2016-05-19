# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Magnifying Glass
                                 A QGIS plugin
 Magnifying Glass Tool for Qgis
                             -------------------
        begin                : 2016-05-19
        copyright            : (C) 2016 All4Gis.
        email                : franka1986@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 #   any later version.                                                    *
 *                                                                         *
 ***************************************************************************/
"""
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import os.path
import qgis.utils
from qgis.core import *
from About import AboutDialog
from PyQt4.QtCore import pyqtSignal, QObject, QEvent
from MagnifierWindow import MagnifierDock
import gui.generated.resources_rc

try:
    import sys
    from pydevd import *
except:
    None;
    
class Magnifier:
 
    def __init__(self, iface):      
        self.iface = iface

    def initGui(self):
 
        self.action = QAction(QIcon(":/imgMagnifier/images/icon.png"), u"Magnifying Glass", self.iface.mainWindow())
        self.action.triggered.connect(self.run)
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&Magnifying Glass", self.action)
        self.wgt=self.action.associatedWidgets()
        for a in self.wgt:
            if isinstance(a, QToolButton):
                a.setStyleSheet("QToolButton {border-radius: 3px} QToolButton:hover {background-color: #FFFFFF}");
                
                
        self.actionAbout = QAction(QIcon(":/imgMagnifier/images/info.png"), u"About", self.iface.mainWindow())
        self.iface.addPluginToMenu(u"&Magnifying Glass", self.actionAbout)
        self.actionAbout.triggered.connect(self.About)
  
    def unload(self):
        self.iface.removePluginMenu(u"&Magnifying Glass", self.action)
        self.iface.removePluginMenu(u"&Magnifying Glass", self.actionAbout)
        self.iface.removeToolBarIcon(self.action)
 
    def About(self):
        self.About = AboutDialog(self.iface)
        self.About.setWindowFlags(Qt.WindowSystemMenuHint | Qt.WindowTitleHint)
        self.About.exec_()


    def run(self):
        MagnifyingGlass = qgis.utils.plugins["MagnifyingGlass"] 
        try:
            if (MagnifyingGlass.dock):
                if(MagnifyingGlass.dock.isVisible()==False):
                    self.dock = MagnifierDock(self.iface)
                    self.dock.setWindowFlags(Qt.WindowSystemMenuHint | Qt.WindowTitleHint)
                    self.iface.addDockWidget( Qt.RightDockWidgetArea, self.dock )
                return
        except:
            self.dock = MagnifierDock(self.iface)
            self.dock.setWindowFlags(Qt.WindowSystemMenuHint | Qt.WindowTitleHint)
            self.iface.addDockWidget( Qt.RightDockWidgetArea, self.dock )
            None