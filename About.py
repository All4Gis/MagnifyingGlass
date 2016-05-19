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
import os.path
import subprocess

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from gui.generated.About import Ui_About
from qgis.core import *
from qgis.gui import *
from qgis.gui import QgsMessageBar


try:
    import sys
    from pydevd import *
except:
    None
 
class AboutDialog(QtGui.QDialog, Ui_About):
    def __init__(self, iface):      
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.iface = iface
        self.plugin_dir = os.path.dirname(__file__) 
        self.video = self.plugin_dir + '//example//ExampleUse.mp4'
    
    # Example
    def ShowVideo(self): 
        if os.path.exists(self.video):
             
            if sys.platform.startswith('dar'):
                subprocess.call(['open', self.video])
            elif sys.platform.startswith('lin'):
                subprocess.call(['xdg-open', self.video])
            elif sys.platform.startswith('win'):
                os.startfile(self.video)
            else:   
                pass
             
        else:
            self.iface.messageBar().pushMessage("Error: ", "Could not open video file: " + self.video, level=QgsMessageBar.CRITICAL, duration=3) 
            return
