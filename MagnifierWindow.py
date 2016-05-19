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
from PyQt4.QtCore import QEvent
from PyQt4.QtGui import *
import os.path
from qgis.core import *
from qgis.gui import *
import shutil
from PyQt4 import QtCore, QtGui
from About import AboutDialog
from GlassTool import *
from gui.generated.ui_Magnifier import Ui_MagnifierDock

try:
    import sys
    from pydevd import *
except:
    None
            
class MagnifierDock(QDockWidget, Ui_MagnifierDock):
    def __init__(self, iface):
        QDockWidget.__init__(self)
        self.setupUi(self)     
        self.settings = QSettings()
        self.iface = iface
        self.mapGlass=None
        self.mc = self.iface.mapCanvas()
        self.load=False
        self.s = QSettings()
 
        self.BaseMaps = {
                         
            "OSM" : "",
            "OSM Mapnik" : "http://a.tile.openstreetmap.org/{}/{}/{}.png",
            "OSM Mapnik (de)" : "http://tile.openstreetmap.de/tiles/osmde/{}/{}/{}.png",
            "OSM Mapnik (humanitarian)" : "http://a.tile.openstreetmap.fr/hot/{}/{}/{}.png",
            "OSM Toner" : "http://a.tile.stamen.com/toner/{}/{}/{}.png",
            "OSM CycleMap" : "http://a.tile.opencyclemap.org/cycle/{}/{}/{}.png",
            "OSM OEPNV" : "http://tile.memomaps.de/tilegen/{}/{}/{}.png",
            "OSM Hike&Bike" : "http://a.www.toolserver.org/tiles/hikebike/{}/{}/{}.png",
            "OSM Wanderreitkarte" : "http://www.wanderreitkarte.de/topo/{}/{}/{}.png",
            "OSM OpenSnowmap" : "http://www.opensnowmap.org/opensnowmap-overlay/{}/{}/{}.png",
            "OSM OpenTopoMap" : "http://a.tile.opentopomap.org/{}/{}/{}.png",
            "OSM Pioneer Road" : "https://b.tile.thunderforest.com/pioneer/{}/{}/{}.png",
            "OSM No Labels" : "https://tiles.wmflabs.org/osm-no-labels/{}/{}/{}.png",
            "OSM Water Colors" : "http://b.tile.stamen.com/watercolor/{}/{}/{}.png",
            "OSM SE Hydda Full" : "http://a.tile.openstreetmap.se/hydda/full/{}/{}/{}.png",
 
            "MapQuest" : "",
            "Mapquest (OSM)" : "http://otile1.mqcdn.com/tiles/1.0.0/map/{}/{}/{}.png",
            "MapQuest Open Aerial" : "http://otile1.mqcdn.com/tiles/1.0.0/sat/{}/{}/{}.png",
        
            "CartoDB" : "",
            "CartoDB Dark Matter (OSM)" : "http://b.basemaps.cartocdn.com/dark_all/{}/{}/{}.png",
            "CartoDB Positron (OSM)" : "http://b.basemaps.cartocdn.com/light_all/{}/{}/{}.png",
     
            "Mapbox" :"",
            "Mapbox Hybrid" : "https://b.tiles.mapbox.com/v3/tmcw.map-j5fsp01s/{}/{}/{}.png",
             
            "Map1eu" : "",
            "Map1eu (OSM)"  : "http://beta.map1.eu/tiles/{}/{}/{}.png",
        
            "Relief" : "",
            "Relief STRM" : "http://maps-for-free.com/layer/relief/{}/{}/{}.png"
   
        }    
 
        self.PopulateCombos(self.CmbNomalMap)
        self.PopulateCombos(self.CmbGlassMap)
 
        self.CmbNomalMap.setCurrentIndex(2)
        self.CmbGlassMap.setCurrentIndex(3)
        
        self.load=True
        
        NormalUrl = self.CmbNomalMap.itemData(self.CmbNomalMap.currentIndex())
        GlassUrl=self.CmbGlassMap.itemData(self.CmbGlassMap.currentIndex())
        
        self.UpdateTool(NormalUrl,GlassUrl,15,40.4167754,-3.7037902)
 
    #Update/Create Maps
    def UpdateTool(self,NormalUrl,GlassUrl,zoom,latitude,longitude):
 
        try:
            self.mapGlass.parent=None 
            #self.CanvasLayout.removeWidget(self.mapGlass) 
        except:
            None
 
        self.mapGlass = LightMaps(self,NormalUrl=NormalUrl,GlassUrl=GlassUrl,width=10, height=10, zoom=zoom, latitude=latitude, longitude=longitude)
        self.CanvasLayout.addWidget(self.mapGlass, 0, 0, 1, 7 ) 
        self.mapGlass.setFocus()
        return
    
    #Change base maps (Glass tool and Nomal Map)
    def ChangeBaseMap(self,index):
        sender = QObject.sender(self)
        if sender.objectName()=="CmbNomalMap":
            NormalUrl = sender.itemData(index) 
            GlassUrl=self.CmbGlassMap.itemData(self.CmbGlassMap.currentIndex())
        else:
            NormalUrl = self.CmbNomalMap.itemData(self.CmbNomalMap.currentIndex())
            GlassUrl=sender.itemData(index)
        
        if self.load== True:
            zoom=int(self.s.value("MagnifyingGlass/zoom"))
            latitude=float(self.s.value("MagnifyingGlass/latitude"))
            longitude=float(self.s.value("MagnifyingGlass/longitude"))
            self.UpdateTool(NormalUrl,GlassUrl,zoom,latitude,longitude) 
 
    #LLenamos los combobox
    def PopulateCombos(self,combo):
        combo.clear() 
        combo.addItem("", None)
        i = 1
        for k in sorted(self.BaseMaps.iterkeys()):  
            v=self.BaseMaps[k]
            if v=="":
                combo.addItem(k,v)   
                combo.setItemData(i,QFont("DejaVu Sans", 10, QFont.Bold), Qt.FontRole);
                combo.setItemData(i,0, Qt.UserRole - 1);
            else:
                k="    "+k
                combo.addItem(k,v)   
                combo.setItemData(i,QColor("#151515"), Qt.TextColorRole)
                combo.setItemData(i,v,Qt.UserRole)
            
            i = i + 1 
        return
 
    #Open About dialog 
    def About(self):
        self.About = AboutDialog(self.iface)
        self.About.setWindowFlags(Qt.WindowSystemMenuHint | Qt.WindowTitleHint)
        self.About.exec_()